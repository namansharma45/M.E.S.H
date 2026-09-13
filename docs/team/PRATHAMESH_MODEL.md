# PRATHAMESH — MODEL + TRAINING OWNER

## Mission

Build and validate MESH's predictive engine using Naman's canonical data contract and prove whether mask-aware fusion provides measurable value.

## Own

```text
ml/**
pipelines/training/**
pipelines/evaluation/**
configs/model/**
configs/training/**
artifacts/checkpoints/**
artifacts/reports/**
```

## Responsibilities

### Baselines
Implement valid:
- single-modality RUL model;
- classifier;
- concatenation fusion;
- masked concatenation.

### Proposed model
Implement:
- 1D-CNN + BiLSTM modality encoders;
- mask-aware cross-attention;
- 2-layer/4-head Transformer temporal refiner;
- dataset-supported task heads;
- modality dropout;
- uncertainty/calibration;
- explainability.

### Evaluation
Every experiment records:
- commit;
- dataset version;
- split version;
- preprocessor/scaler version;
- config;
- seed;
- metrics;
- checkpoint.

### Missing modality
The model must consume the modality mask. Zeroing values without changing the mask is not a valid missing-modality experiment.

### Handoff
Provide a stable inference-facing interface conceptually:

```python
predict(canonical_batch) -> PredictionBundle
```

Sarthak should not import training internals.

## Do not touch

- Naman's data-processing implementation;
- dashboard;
- API transport;
- deployment.
