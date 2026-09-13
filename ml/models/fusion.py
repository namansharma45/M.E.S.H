import torch
import torch.nn as nn
import torch.nn.functional as F

class MaskAwareCrossAttention(nn.Module):
    """
    Fuses multiple modality embeddings using mask-aware cross-attention.
    Applies a large negative bias to missing modalities before softmax to exclude them from the fusion.
    """
    def __init__(self, embed_dim: int, num_heads: int, dropout: float = 0.15):
        super().__init__()
        self.num_heads = num_heads
        
        # We can use standard MultiheadAttention, but we need to explicitly provide an attention mask
        self.mha = nn.MultiheadAttention(
            embed_dim=embed_dim,
            num_heads=num_heads,
            dropout=dropout,
            batch_first=True
        )

    def forward(self, embeddings: torch.Tensor, mask: torch.Tensor):
        """
        Args:
            embeddings: Tensor of shape [batch_size, seq_len, num_modalities, embed_dim]
                Wait, for fusion, we want to fuse across modalities at each timestep, or across timesteps?
                DA1 says "mask-aware cross-attention fusion". Usually, this fuses the modalities.
                So if input is [batch_size, seq_len, num_modalities, embed_dim],
                we reshape it to treat (batch_size * seq_len) as the effective batch size,
                or we just transpose to fuse across modalities.
                Let's assume inputs are stacked modalities: 
                [batch_size, num_modalities, seq_len, embed_dim]
                We want to fuse across modalities for each timestep, yielding a single unified sequence 
                [batch_size, seq_len, embed_dim].
                
                Actually, let's just do cross-attention across modalities, where each modality attends to the others.
                Let `x` have shape [B, num_modalities, embed_dim] (for a single timestep).
                We can run MHA over the `num_modalities` sequence. 
                But since we have `seq_len` timesteps, we can flatten `B` and `seq_len`:
                `effective_B = B * seq_len`
                `x` shape = [effective_B, num_modalities, embed_dim]
                
            mask: Tensor of shape [batch_size, num_modalities] (1 = available, 0 = unavailable)
            
        Returns:
            fused: Tensor of shape [batch_size, seq_len, embed_dim]
            attn_weights: Tensor of shape [effective_B, num_heads, num_modalities, num_modalities] (if returned by MHA)
        """
        B, seq_len, num_modalities, embed_dim = embeddings.shape
        
        # Flatten batch and seq_len
        x = embeddings.reshape(B * seq_len, num_modalities, embed_dim)
        
        # Expand mask to match effective batch size
        # mask is [B, num_modalities] -> expand to [B, seq_len, num_modalities] -> [B * seq_len, num_modalities]
        expanded_mask = mask.unsqueeze(1).expand(B, seq_len, num_modalities).reshape(B * seq_len, num_modalities)
        
        # PyTorch MultiheadAttention uses key_padding_mask where True means "ignore"
        # Our mask uses 1 for available, 0 for unavailable. So we invert it.
        # Shape must be [B*seq_len, num_modalities]
        key_padding_mask = (expanded_mask == 0)
        
        # If all modalities are masked for a sequence step, MHA produces NaNs 
        # because softmax over all -inf is undefined. We will nan_to_num it.
        attn_out, attn_weights = self.mha(
            query=x,
            key=x,
            value=x,
            key_padding_mask=key_padding_mask,
            need_weights=True,
            average_attn_weights=False
        )
        attn_out = torch.nan_to_num(attn_out, nan=0.0)
        attn_weights = torch.nan_to_num(attn_weights, nan=0.0)
        
        # Mask out missing modalities before pooling. This explicitly prevents 
        # a masked modality's own "query" output from leaking into the temporal refiner.
        valid_counts = expanded_mask.sum(dim=1, keepdim=True)
        # Prevent division by zero
        safe_counts = torch.where(valid_counts > 0, valid_counts, torch.ones_like(valid_counts))
        
        masked_out = attn_out * expanded_mask.unsqueeze(-1)
        
        # Store for scratch test inspection
        self._last_masked_out = masked_out
        self._last_attn_out = attn_out
        
        fused = masked_out.sum(dim=1) / safe_counts # Shape: [B*seq_len, embed_dim]
        
        # Reshape back to [B, seq_len, embed_dim]
        fused = fused.reshape(B, seq_len, embed_dim)
        
        # Also reshape attention weights to [B, seq_len, num_heads, num_modalities, num_modalities]
        attn_weights = attn_weights.reshape(B, seq_len, self.num_heads, num_modalities, num_modalities)
        
        return fused, attn_weights
