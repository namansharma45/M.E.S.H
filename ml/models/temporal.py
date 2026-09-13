import torch
import torch.nn as nn

class TemporalRefiner(nn.Module):
    """
    A lightweight Transformer encoder to relate the current fused window 
    to a short history of windows, particularly useful for RUL/degradation trends.
    """
    def __init__(self, d_model: int, nhead: int, num_layers: int, dim_feedforward: int, dropout: float = 0.15):
        super().__init__()
        
        # We use a standard Transformer Encoder
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            activation='relu',
            batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer=encoder_layer,
            num_layers=num_layers
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Tensor of shape [batch_size, seq_len, d_model]
               This is the fused sequence across timesteps.
        Returns:
            refiner_out: Tensor of shape [batch_size, seq_len, d_model]
        """
        # [batch_size, seq_len, d_model] -> passed directly since batch_first=True
        refiner_out = self.transformer_encoder(x)
        return refiner_out
