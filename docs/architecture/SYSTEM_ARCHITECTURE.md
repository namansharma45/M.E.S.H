# SYSTEM ARCHITECTURE — MESH

## End-to-end

```text
Real dataset / real stored window
        ↓
Naman: ingestion + validation + provenance
        ↓
Canonical native-modality representation
+ scaler/preprocessor
+ modality mask
        ↓
Prathamesh: offline training/evaluation
        ↓
Versioned checkpoint + metadata + calibration
        ↓
Sarthak: FastAPI inference service
        ↓
Sarthak: Streamlit dashboard
        ↓
Engineer decision support
```

The DA1 report explicitly describes a Streamlit front end, lightweight Python backend, and PyTorch inference engine.

## Layer ownership

### Data layer — Naman
Parsing, validation, splits, normalization, windowing, masks, manifests.

### ML layer — Prathamesh
Model architecture, training, evaluation, calibration, explainability.

### Service layer — Sarthak
Request validation, model loading, inference orchestration, response schemas, health checks.

### Product layer — Sarthak
Dashboard, evidence views, missing-sensor experiment, research view.

## Dependency direction

```text
data → model → inference service → dashboard
```

Forbidden:

- dashboard importing training internals;
- model importing Streamlit;
- data loader importing UI code;
- API mutating training data;
- frontend inventing model inputs.

## Inference request concept

```json
{
  "dataset_id": "...",
  "dataset_version": "...",
  "run_id": "...",
  "window": {
    "native_modality": ["real values"]
  },
  "modality_mask": {
    "native_modality": 1
  }
}
```

Exact names and shapes are controlled by the versioned contract.

## Inference response concept

```json
{
  "model_version": "...",
  "dataset_version": "...",
  "prediction": {},
  "uncertainty": {},
  "modality_status": {},
  "attention": {},
  "explanations": [],
  "latency_ms": 0
}
```

Only populate fields that actually exist.

## Release bundle

```text
model checkpoint
scaler/preprocessor artifact
model metadata
label schema
inference configuration
dataset manifest
git commit
evaluation report
calibration metadata
deployment configuration
```
