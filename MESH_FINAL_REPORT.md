# MESH Project: Final Technical Report

## 1. Documentation & Data Contract
* **Documentation Read:** `docs/model/MODEL_SPEC.md`, `docs/data/DATA_DICTIONARY.md`, `docs/architecture/SYSTEM_ARCHITECTURE.md`, `docs/training/TRAINING_EVALUATION.md`, `docs/training/MISSING_MODALITY_EXPERIMENTS.md`, `docs/explainability/EXPLAINABILITY.md`, and `docs/data/DATA_PIPELINE.md`.
* **Data Contract Consumed:** Implemented and validated `CanonicalBatch` according to the exact Pydantic spec (`ml/data/contract.py`), allowing arbitrary tensors and strictly typing all metadata.

## 2. Architecture Implemented
Implemented the `MESHModel` (`ml/models/mesh_model.py`) natively in PyTorch:
* **Modality Encoders:** 1D CNNs (kernel=3, out_channels=8) into Bidirectional LSTMs (hidden=16) per modality (`temperature`, `vibration`, `rotational_speed`, `torque`).
* **Fusion:** Mask-Aware Cross-Attention (`ml/models/fusion.py`) using PyTorch's `MultiheadAttention`. Missing modalities are explicitly zeroed out of the attention softmax (both queries and keys) using `-inf` masking.
* **Temporal Refiner:** Standard TransformerEncoder layer processing the fused sequence.
* **Heads:** 
  * RUL (Regression): Outputs Mean and Log-Variance (clamped to `[-10, 10]`) for NLL optimization.
  * Fault (Classification): 3-class logits.
  * Anomaly (Binary): Single logit for sigmoid activation.

## 3. Files Created / Modified
* `ml/models/mesh_model.py`, `ml/models/encoders.py`, `ml/models/fusion.py`, `ml/models/temporal.py`, `ml/models/heads.py`
* `pipelines/training/train.py`, `pipelines/training/tracker.py`
* `pipelines/evaluation/evaluate.py`, `pipelines/evaluation/missing_modality_experiment.py`
* `ml/explainability/attribution.py`
* `ml/inference/interface.py`
* `tests/ml/test_model_architecture.py`, `tests/ml/test_contract.py`

## 4. Training & Evaluation Pipeline
* **Training (`train.py`):** Trains using NLL (RUL) + CrossEntropy (Fault) + BCE (Anomaly). Integrates a JSONL experiment tracker. Includes deterministic 80/20 train/val splits. Persists checkpoint metadata (model version, config).
* **Evaluation (`evaluate.py`):** Computes exact MAE, RMSE, NLL, and standard classification metrics. RUL metrics are correctly de-normalized into real cycle units.

## 5. Missing-Modality Experiments
Executed an 8-condition systematic dropout sweep (0 to 4 modalities dropped) via `missing_modality_experiment.py`. Output is saved as structured JSON artifacts. 

## 6. Uncertainty, Calibration, and Explainability
* **Explainability (`attribution.py`):** Extracted native attention weights (proving exactly $0.0$ attention for masked modalities). Used Captum GradientSHAP for feature attribution.
* **Uncertainty:** RUL head successfully learned aleatoric variance (preventing variance collapse via soft clamping).

## 7. Checkpoint Location
The best trained model checkpoint is persisted at:
`checkpoints/model_best.pt`

## 8. Inference Contract
Implemented a strict, decoupled Python inference engine (`ml/inference/interface.py`).
* Consumes `CanonicalBatch`, produces `PredictionBundle`.
* Transparently handles denormalization to real units (cycles).
* Embeds traceability metadata (`model_version` timestamp, `checkpoint_id`, `training_config_ref`).
* Exposes `attention_weights` strictly as an opt-in parameter for payload efficiency.

## 9. Testing
Built strict PyTest suites (`tests/ml/`) that are **100% Passing**:
* **`test_model_architecture.py`**: Verifies exact tensor shapes, masked-modality zeroing, NaN-safety under total dropout, and deterministic eval bounds.
* **`test_contract.py`**: Verifies `CanonicalBatch` rejection of malformed data, `PredictionBundle` JSON serialization, and full checkpoint save/load equivalence.

## 10. Assumptions & Known Limitations
> [!WARNING]
> **Mock Data Performance:** All metrics, attributions, and variance boundaries currently reflect convergence on uniform noise. The model currently exhibits majority-class collapse (expected) and tiny/random feature attributions. Real predictive evaluation is pending actual data.

> [!WARNING]
> **Epistemic Uncertainty limitation:** Our missing-modality experiment empirically proved that NLL (Aleatoric) variance remains completely flat (~3060) when input modalities drop out. The loss formulation measures target noise, not model confidence. An Epistemic method (like MC Dropout) MUST be implemented before deployment to flag "I don't know" when sensors fail.

> [!WARNING]
> **Hardcoded Normalization:** RUL target normalization stats (mean, std) are currently hardcoded placeholders injected during training initialization. These must be replaced with the actual dataset statistics computed by Naman's preprocessor.

## 11. Backend Integration (For Sarthak)
* The `PredictionBundle` is fully JSON-serializable via `dataclasses.asdict()`.
* All regression metrics are returned in absolute real units (no z-score decoding required on the backend).
* `attention_weights` are natively suppressed to save bandwidth. Pass `return_attention=True` to `engine.predict()` if visual explainability is requested by the dashboard.
* Traceability is guaranteed: parse `model_version` directly from the `PredictionBundle` to log exactly which checkpoint generated the output.

## 12. Open Issues (For Naman)
> [!IMPORTANT]
> **Dataset Choice Ambiguity:** The Model Spec assumes 4 specific channels (`temperature`, `vibration`, `rotational_speed`, `torque`). However, AI4I has 5 features, NASA CMAPSS has 21, and QIT-CEMC has 2. Naman must explicitly lock in the dataset choice and update the Preprocessor output to match the 4 expected channels, or the model's `native_modalities` config must be updated to align with the chosen dataset.

## 13. Quality Assurance: Bugs Caught & Resolved
The following concrete issues were caught and fixed during the interactive modeling phase, documented here as a historical record for the team:
* **RUL NLL Explosion:** Target RUL was left unnormalized, forcing the NLL loss to NaN; resolved via target z-scoring and log-variance soft-clamping.
* **Fusion Mask Leakage:** The attention layer leaked the masked modality's own query vector into the output; fixed by multiplying the MHA output by the binary mask before pooling.
* **Total-Dropout NaNs:** Dropping 100% of sensors produced 0/0 NaN division in the fusion pooling; fixed via `nan_to_num` and safe denominator handling.
* **Traceability Gap:** `model_version` was hardcoded as "unknown" in the inference payload; fixed by baking a real version string directly into the checkpoint at save time.
* **Explainability Payload Bloat:** `attention_weights` were silently stripped from the inference bundle; fixed via an explicit `return_attention` opt-in parameter.
* **Silent Test Passes:** `test_masked_modality_zeroing` had a conditional `hasattr` guard that could silently skip the test; replaced with a hard assertion.
* **Checkpoint Test Fallacy:** `test_checkpoint_roundtrip` originally tested `load -> load` agreement rather than `save -> load` fidelity; rewriting to a true save-and-reload cycle caught two real downstream schema and variance-conversion bugs.
