# DATA PIPELINE — Naman

## Goal

Convert approved measured data into reproducible model-ready representations without changing physical meaning.

## Pipeline

```text
RAW SOURCE
  ↓
Integrity verification
  ↓
Dataset-specific parser
  ↓
Physical metadata / units / sampling
  ↓
Run + timestamp ordering
  ↓
Missing-value / bad-segment handling
  ↓
Asset/run-level split
  ↓
Train-only normalization
  ↓
Sliding windows
  ↓
Documented feature derivation
  ↓
Modality masks
  ↓
Processed artifact + manifest
```

## Starting window configuration

The DA1 report specifies overlapping windows of **20 timesteps with stride 5** as the starting configuration. This must remain explicit and versioned rather than hard-coded invisibly.

## Canonical sample concept

```text
sample_id
source_dataset
dataset_version
run_id
machine_id (if available)
window_start
window_end
sampling_interval_seconds
native_modalities
modality_values
modality_mask
static_features (only when verified)
target_rul (nullable)
target_fault_class (nullable)
target_degradation (nullable)
preprocessor_version
scaler_version
```

## Missing value vs missing modality

**Missing value:** part of an otherwise available sensor stream is absent/corrupt.

**Missing modality:** the whole sensor modality is unavailable for the inference window.

**Sensor failure:** source evidence indicates acquisition hardware failure.

These states must not be collapsed into one field.

## Cleaning

Allowed:
- unit conversion supported by source metadata;
- chronological ordering;
- documented duplicate handling;
- documented invalid-range handling;
- preservation of run boundaries;
- explicit handling of corrupted segments.

Forbidden:
- smoothing away failure signatures just to improve metrics;
- arbitrary failure thresholds;
- row-position RUL unless physically supported by the dataset protocol;
- random window splits across the same run.

## Feature engineering

The DA1 report proposes rolling mean, standard deviation, and rate-of-change features alongside raw channels. These are allowed only when calculated without future leakage.

## Normalization

Fit per-modality z-score scalers on training data only. Save and version the resulting scaler artifacts.

## Modality mask

```text
1 = modality available
0 = modality unavailable
```

When controlled modality dropout is used, the normalized values may be zeroed, but the mask is authoritative for fusion.

## Handoff gate

Naman hands off only after providing:

- dataset manifest;
- schema version;
- processed sample;
- split manifest;
- scaler/preprocessor artifact;
- missingness example;
- leakage test;
- data-quality report.
