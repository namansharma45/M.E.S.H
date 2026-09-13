# MODEL SPECIFICATION — PRATHAMESH

## Starting architecture

The DA1 report proposes:

```text
Native sensor modalities
        ↓
Per-modality encoders
1D-CNN → BiLSTM
        ↓
Mask-aware cross-attention fusion
        ↓
2-layer / 4-head Transformer temporal refiner
        ↓
Task heads supported by the dataset
```

## 1. Per-modality encoders

Each available modality is encoded independently.

Starting design:
- 1D convolution layers for local temporal patterns;
- BiLSTM for temporal aggregation;
- fixed-size modality embedding.

This is adopted from the literature as an engineering baseline, not claimed as the project's novelty.

## 2. Mask-aware cross-attention — central novelty

A modality availability mask accompanies the embeddings.

Before attention softmax:

```text
present modality → normal attention
missing modality → large negative attention bias
```

This makes unavailable modalities excluded from the weighted combination instead of merely replacing them with zeros and hoping the model learns what zero means.

## 3. Modality dropout

Starting probability:

```text
p = 0.15
```

This is a starting configuration from DA1, not a permanently fixed hyperparameter. Variants must be evaluated rather than assumed optimal.

Natural source missingness and controlled training dropout must remain distinguishable.

## 4. Temporal refiner

Starting design:

- 2 Transformer encoder layers;
- 4 attention heads.

Purpose: relate the current fused window to a short history of windows, especially for degradation/RUL trends.

The depth should be tested because the primary datasets are not large enough to justify unnecessary model complexity.

## 5. Task heads

Only instantiate heads supported by the selected dataset.

### RUL regression

Continuous output with a documented unit/definition.

### Fault classification

Multi-class output only when the dataset provides a valid class label.

### Anomaly output

Only use an anomaly score if its training target or mathematically documented derivation is valid. Do not display an arbitrary "anomaly percentage".

## 6. Multi-task learning

Where a dataset supports multiple targets, the shared fusion backbone may feed:

```text
RUL head
Fault head
Anomaly head
```

with a weighted objective such as:

```text
L = λ_rul L_Huber + λ_fault L_CE + λ_anomaly L_BCE
```

Weights must be documented and tuned using training/validation data only.

## 7. Dataset-native architecture

If a dataset lacks a modality or target, the model must adapt through an explicit schema/configuration. Do not create fake inputs to satisfy the architecture diagram.

## 8. Model outputs

The inference-facing result should expose only meaningful fields, such as:

- supported predictions;
- uncertainty/calibration information;
- modality availability;
- attention evidence;
- feature attribution;
- model/version identifiers;
- inference latency.

No decorative model outputs.
