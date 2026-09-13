import torch
import torch.nn as nn
from typing import Dict, List, Tuple
from ml.models.encoders import ModalityEncoder
from ml.models.temporal import TemporalRefiner
from ml.models.heads import RULHead, FaultClassificationHead, AnomalyHead

class SingleModalityBaseline(nn.Module):
    """
    BASELINE MODEL: Evaluates a single sensor modality without any fusion.
    """
    def __init__(
        self,
        modality_name: str,
        native_modalities: List[str],
        in_channels: int,
        encoder_config: dict,
        temporal_config: dict,
        heads_config: dict,
        dropout_p: float = 0.15
    ):
        super().__init__()
        self.modality_name = modality_name
        self.modality_idx = native_modalities.index(modality_name)
        
        self.encoder = ModalityEncoder(
            in_channels=in_channels,
            cnn_out_channels=encoder_config['cnn_out_channels'],
            cnn_kernel_size=encoder_config['cnn_kernel_size'],
            bilstm_hidden_size=encoder_config['bilstm_hidden_size'],
            dropout_p=dropout_p
        )
        
        self.temporal_refiner = TemporalRefiner(
            d_model=temporal_config['d_model'],
            nhead=temporal_config['nhead'],
            num_layers=temporal_config['num_layers'],
            dim_feedforward=temporal_config['dim_feedforward'],
            dropout=temporal_config['dropout']
        )
        
        d_model = temporal_config['d_model']
        self.rul_head = RULHead(d_model, heads_config['rul_hidden_dim'], dropout_p) if heads_config.get('rul_hidden_dim') else None
        self.fault_head = FaultClassificationHead(d_model, heads_config['fault_hidden_dim'], heads_config['num_fault_classes'], dropout_p) if heads_config.get('num_fault_classes', 0) > 0 else None
        self.anomaly_head = AnomalyHead(d_model, heads_config['anomaly_hidden_dim'], dropout_p) if heads_config.get('anomaly_hidden_dim') else None

    def forward(self, modality_values: Dict[str, torch.Tensor], mask: torch.Tensor = None):
        if self.modality_name in modality_values:
            x = modality_values[self.modality_name]
        else:
            ref_tensor = next(iter(modality_values.values()))
            x = torch.zeros((ref_tensor.size(0), ref_tensor.size(1), self.encoder.cnn.in_channels), device=ref_tensor.device)
            
        h = self.encoder(x)
        
        if mask is not None:
            m = mask[:, self.modality_idx].view(-1, 1, 1)
            h = h * m
            
        refined = self.temporal_refiner(h)
        final_repr = refined[:, -1, :]
        
        predictions = {}
        if self.rul_head:
            mean, variance = self.rul_head(final_repr)
            predictions['rul_mean'] = mean
            predictions['rul_variance'] = variance
        if self.fault_head:
            predictions['fault_logits'] = self.fault_head(final_repr)
        if self.anomaly_head:
            predictions['anomaly_logit'] = self.anomaly_head(final_repr)
            
        return predictions, None  # No attention weights



class ConcatenationBaseline(nn.Module):
    """
    BASELINE MODEL: Fuses modalities via simple feature concatenation (no cross-attention).
    Optionally applies the mask by zeroing out the embeddings of missing modalities.
    """
    def __init__(
        self,
        native_modalities: List[str],
        cnn_in_channels_map: Dict[str, int],
        encoder_config: dict,
        temporal_config: dict,
        heads_config: dict,
        use_mask: bool = False,
        dropout_p: float = 0.15
    ):
        super().__init__()
        self.native_modalities = native_modalities
        self.use_mask = use_mask
        
        self.encoders = nn.ModuleDict({
            mod: ModalityEncoder(
                in_channels=cnn_in_channels_map.get(mod, 1),
                cnn_out_channels=encoder_config['cnn_out_channels'],
                cnn_kernel_size=encoder_config['cnn_kernel_size'],
                bilstm_hidden_size=encoder_config['bilstm_hidden_size'],
                dropout_p=dropout_p
            ) for mod in native_modalities
        })
        
        # We concatenate all modality embeddings. 
        # Total dimension = num_modalities * embed_dim
        embed_dim = encoder_config['out_dim']
        concat_dim = len(native_modalities) * embed_dim
        
        # We need a projection layer to reduce back to d_model for the temporal refiner
        self.proj = nn.Linear(concat_dim, temporal_config['d_model'])
        
        self.temporal_refiner = TemporalRefiner(
            d_model=temporal_config['d_model'],
            nhead=temporal_config['nhead'],
            num_layers=temporal_config['num_layers'],
            dim_feedforward=temporal_config['dim_feedforward'],
            dropout=temporal_config['dropout']
        )
        
        d_model = temporal_config['d_model']
        self.rul_head = RULHead(d_model, heads_config['rul_hidden_dim'], dropout_p) if heads_config.get('rul_hidden_dim') else None
        self.fault_head = FaultClassificationHead(d_model, heads_config['fault_hidden_dim'], heads_config['num_fault_classes'], dropout_p) if heads_config.get('num_fault_classes', 0) > 0 else None
        self.anomaly_head = AnomalyHead(d_model, heads_config['anomaly_hidden_dim'], dropout_p) if heads_config.get('anomaly_hidden_dim') else None

    def forward(self, modality_values: Dict[str, torch.Tensor], modality_mask: torch.Tensor):
        encoded_modalities = []
        for i, mod in enumerate(self.native_modalities):
            if mod in modality_values:
                x = modality_values[mod]
            else:
                ref_tensor = next(iter(modality_values.values()))
                x = torch.zeros((ref_tensor.size(0), ref_tensor.size(1), self.encoders[mod].cnn.in_channels), device=ref_tensor.device)
                
            h = self.encoders[mod](x) # [batch, seq_len, embed_dim]
            
            # Apply mask if this is the masked baseline
            if self.use_mask:
                # modality_mask[:, i] is [batch] -> reshape to [batch, 1, 1]
                m = modality_mask[:, i].view(-1, 1, 1)
                h = h * m
                
            encoded_modalities.append(h)
            
        # Concatenate along the feature dimension
        # Shape: [batch, seq_len, num_modalities * embed_dim]
        concat_h = torch.cat(encoded_modalities, dim=-1)
        
        # Project to d_model
        projected = self.proj(concat_h)
        
        refined = self.temporal_refiner(projected)
        final_repr = refined[:, -1, :]
        
        predictions = {}
        if self.rul_head:
            mean, variance = self.rul_head(final_repr)
            predictions['rul_mean'] = mean
            predictions['rul_variance'] = variance
        if self.fault_head:
            predictions['fault_logits'] = self.fault_head(final_repr)
        if self.anomaly_head:
            predictions['anomaly_logit'] = self.anomaly_head(final_repr)
            
        return predictions, None
