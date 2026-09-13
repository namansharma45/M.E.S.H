import torch
import torch.nn as nn
from typing import Dict, List, Optional, Tuple
from ml.models.encoders import ModalityEncoder
from ml.models.fusion import MaskAwareCrossAttention
from ml.models.temporal import TemporalRefiner
from ml.models.heads import RULHead, FaultClassificationHead, AnomalyHead

class MESHModel(nn.Module):
    """
    End-to-End MESH Model Architecture:
    1. Per-modality Encoders (1D-CNN + BiLSTM)
    2. Mask-aware Cross Attention Fusion
    3. Temporal Refiner (Transformer)
    4. Task Heads (RUL, Fault, Anomaly)
    """
    def __init__(
        self,
        native_modalities: List[str],
        cnn_in_channels_map: Dict[str, int],
        encoder_config: dict,
        fusion_config: dict,
        temporal_config: dict,
        heads_config: dict,
        dropout_p: float = 0.15
    ):
        super().__init__()
        self.native_modalities = native_modalities
        
        # 1. Encoders (Dataset-native)
        self.encoders = nn.ModuleDict({
            mod: ModalityEncoder(
                in_channels=cnn_in_channels_map.get(mod, 1),
                cnn_out_channels=encoder_config['cnn_out_channels'],
                cnn_kernel_size=encoder_config['cnn_kernel_size'],
                bilstm_hidden_size=encoder_config['bilstm_hidden_size'],
                dropout_p=dropout_p
            ) for mod in native_modalities
        })
        
        # 2. Fusion
        self.fusion = MaskAwareCrossAttention(
            embed_dim=fusion_config['embed_dim'],
            num_heads=fusion_config['num_heads'],
            dropout=fusion_config['dropout']
        )
        
        # 3. Temporal Refiner
        self.temporal_refiner = TemporalRefiner(
            d_model=temporal_config['d_model'],
            nhead=temporal_config['nhead'],
            num_layers=temporal_config['num_layers'],
            dim_feedforward=temporal_config['dim_feedforward'],
            dropout=temporal_config['dropout']
        )
        
        # 4. Task Heads
        # We extract the last timestep for final predictions or pool.
        # We'll use the last timestep of the refiner output.
        d_model = temporal_config['d_model']
        
        self.rul_head = None
        if heads_config.get('rul_hidden_dim') is not None:
            self.rul_head = RULHead(d_model, heads_config['rul_hidden_dim'], dropout_p)
            
        self.fault_head = None
        if heads_config.get('num_fault_classes', 0) > 0:
            self.fault_head = FaultClassificationHead(
                d_model, heads_config['fault_hidden_dim'], heads_config['num_fault_classes'], dropout_p
            )
            
        self.anomaly_head = None
        if heads_config.get('anomaly_hidden_dim') is not None:
            self.anomaly_head = AnomalyHead(d_model, heads_config['anomaly_hidden_dim'], dropout_p)
            
    def forward(
        self, 
        modality_values: Dict[str, torch.Tensor],
        modality_mask: torch.Tensor
    ) -> Tuple[Dict[str, torch.Tensor], torch.Tensor]:
        """
        Args:
            modality_values: Dictionary mapping modality name to Tensor of shape [batch, window_size, channels]
            modality_mask: Tensor of shape [batch, num_modalities] (1=available, 0=unavailable)
            
        Returns:
            predictions: dict of outputs from heads
            attention_weights: Tensor of shape [batch, seq_len, num_heads, num_modalities, num_modalities]
        """
        encoded_modalities = []
        for i, mod in enumerate(self.native_modalities):
            # If a modality is completely missing in the dict, we feed zeros to the encoder.
            # The mask will ensure it gets ignored during fusion anyway.
            if mod in modality_values:
                x = modality_values[mod]
            else:
                # Infer shape from another tensor
                ref_tensor = next(iter(modality_values.values()))
                batch_size, window_size, _ = ref_tensor.shape
                in_channels = self.encoders[mod].cnn.in_channels
                x = torch.zeros((batch_size, window_size, in_channels), device=ref_tensor.device)
                # Override mask for this modality
                modality_mask[:, i] = 0.0
                
            # x shape: [batch, window_size, channels]
            h = self.encoders[mod](x)  # shape: [batch, window_size, embed_dim]
            encoded_modalities.append(h.unsqueeze(2)) # shape: [batch, window_size, 1, embed_dim]
            
        # Stack modalities: shape [batch, window_size, num_modalities, embed_dim]
        embeddings = torch.cat(encoded_modalities, dim=2)
        
        # Fusion
        fused_seq, attention_weights = self.fusion(embeddings, modality_mask) # [batch, window_size, embed_dim]
        
        # Temporal Refinement
        refined_seq = self.temporal_refiner(fused_seq) # [batch, window_size, embed_dim]
        
        # We take the representation at the final timestep for the prediction heads
        final_repr = refined_seq[:, -1, :] # [batch, embed_dim]
        
        predictions = {}
        
        if self.rul_head is not None:
            mean, variance = self.rul_head(final_repr)
            predictions['rul_mean'] = mean
            predictions['rul_variance'] = variance
            
        if self.fault_head is not None:
            logits = self.fault_head(final_repr)
            predictions['fault_logits'] = logits
            
        if self.anomaly_head is not None:
            anomaly_logit = self.anomaly_head(final_repr)
            predictions['anomaly_logit'] = anomaly_logit
            
        return predictions, attention_weights
