from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
import torch

class CanonicalBatch(BaseModel):
    """
    Data contract representing a batch of samples processed by Naman's pipeline.
    Arbitrary types (like torch.Tensor) are allowed.
    """
    model_config = {"arbitrary_types_allowed": True}

    sample_id: List[str]
    source_dataset: List[str]
    dataset_version: List[str]
    run_id: List[str]
    machine_id: Optional[List[str]] = None
    window_start: List[float]
    window_end: List[float]
    sampling_interval_seconds: List[float]
    
    # Metadata for interpretation
    native_modalities: List[str]
    preprocessor_version: List[str]
    scaler_version: List[str]
    
    # Tensors
    # A dict mapping modality name (e.g. "temperature") to a Tensor of shape [batch_size, window_size, feature_dim]
    modality_values: Dict[str, torch.Tensor]
    
    # Binary mask of shape [batch_size, num_modalities] (1 = available, 0 = unavailable)
    # The order matches native_modalities
    modality_mask: torch.Tensor
    
    # Optional static features, shape [batch_size, num_static_features]
    static_features: Optional[torch.Tensor] = None
    
    # Targets for training/evaluation
    target_rul: Optional[torch.Tensor] = None  # shape: [batch_size, 1]
    target_fault_class: Optional[torch.Tensor] = None  # shape: [batch_size]
    target_degradation: Optional[torch.Tensor] = None  # shape: [batch_size, 1]

class PredictionBundle(BaseModel):
    """
    Data contract representing the output of the ML model, to be consumed by Sarthak's dashboard.
    """
    model_config = {"arbitrary_types_allowed": True}

    # Model context
    model_version: str
    experiment_id: str

    # Sample context
    sample_id: List[str]
    native_modalities: List[str]
    
    # Inference outputs
    predicted_rul: Optional[torch.Tensor] = None  # shape: [batch_size, 1]
    predicted_fault_class: Optional[torch.Tensor] = None  # shape: [batch_size, num_classes] (logits or probs)
    predicted_anomaly_score: Optional[torch.Tensor] = None  # shape: [batch_size, 1]
    
    # Uncertainty (Aleatoric from RUL head, Epistemic from MC Dropout variance, etc.)
    rul_variance: Optional[torch.Tensor] = None  # shape: [batch_size, 1]
    epistemic_uncertainty: Optional[torch.Tensor] = None # shape: [batch_size, 1]
    
    # Explainability
    # Attention weights from mask-aware cross-attention fusion. Shape: [batch_size, num_heads, num_modalities, num_modalities] or similar.
    attention_weights: Optional[torch.Tensor] = None
    
    # Modality availability (passed through from input for the dashboard's awareness)
    modality_mask: torch.Tensor
