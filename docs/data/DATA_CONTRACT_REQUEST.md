# DATA CONTRACT REQUEST — Naman ↔ Prathamesh

**To: Naman (Data Owner)**  
**From: Prathamesh (Model Owner)**  
**Purpose:** Formal request defining the exact tensor shape, metadata, and data structure the ML layer expects from the data pipeline, as derived from `docs/data/DATA_PIPELINE.md`.

## 1. What ML expects (Confirmed from Docs)

- **Modality handling**: Data should be sliding windows of `20 timesteps with stride 5`.
- **Modality mask**: A binary mask (`1` = available, `0` = unavailable) for each modality per sample.
- **Normalization**: Per-modality z-score scalers fitted on the training data only.
- **Metadata**: We need `sample_id`, `source_dataset`, `dataset_version`, `run_id`, `window_start`, `window_end`, and the `preprocessor_version` / `scaler_version`.

## 2. What ML assumes to unblock implementation (Needs Naman's verification)

To unblock the ML implementation before the data pipeline is complete, I am making the following assumptions in the `CanonicalBatch` definition. Please resolve these or confirm they are acceptable:

1. **Tensor format:** 
   - I am assuming `modality_values` will be provided as a dictionary mapping `modality_name: string` to a PyTorch Tensor of shape `[batch_size, window_size, feature_dim]`.
   - *Example:* `{"temperature": Tensor(B, 20, 1), "vibration": Tensor(B, 20, 3)}`.
2. **Modality mask format:**
   - I am assuming `modality_mask` will be a PyTorch Tensor of shape `[batch_size, num_modalities]` where the order of `num_modalities` strictly matches the `native_modalities` list in the schema.
3. **Targets (Labels):**
   - **RUL:** A continuous PyTorch Tensor of shape `[batch_size, 1]` (e.g., remaining hours/cycles).
   - **Fault Class:** An integer PyTorch Tensor of shape `[batch_size]`.
   - **Anomaly Score:** A float PyTorch Tensor of shape `[batch_size, 1]`.
4. **Dataset ambiguity:**
   - DA1 requests 4 specific channels, but the selected datasets (NASA, QIT-CEMC) do not perfectly align. I have made the model **dataset-native** (it builds encoders dynamically based on the modalities it receives). Please confirm exactly which datasets and modalities will be used so we can test the model correctly.

## 3. Mock Data Fixture

Until the real pipeline is ready, I am using a test fixture in `ml/data/mock_canonical_batch.py` that generates random tensors matching the assumptions above. **This is strictly a test fixture and contains no real data logic.**
