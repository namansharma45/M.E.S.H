# NAMAN — DATA ENGINEERING OWNER

## Mission

Turn real source datasets into versioned, trustworthy model inputs without hiding preprocessing decisions or changing physical meaning.

## Own

```text
data/**
pipelines/data/**
configs/data/**
src/data/**     # if this path is used by the implementation
```

## Responsibilities

### Acquisition
- obtain approved public datasets;
- record source, license/terms, checksum;
- preserve immutable raw data;
- maintain versions.

### Dataset adapters
Create one adapter per dataset. Map native fields into the canonical interface without inventing channels.

### Cleaning
Document:
- units;
- ordering;
- duplicates;
- missing values;
- invalid ranges;
- bad segments;
- sampling differences.

### Splits
Create asset/run-level train/validation/test manifests.

### Windowing
Use the starting 20-timestep / stride-5 configuration unless a documented dataset-specific experiment changes it.

### Normalization
Fit per-modality scalers on training data only and version them.

### Missingness
Provide modality masks. Keep natural missingness separate from controlled experiment dropout.

### Targets
Only use source-supported targets. Do not invent thresholds or labels.

## Handoff to Prathamesh

Provide:

- dataset card;
- source manifest;
- canonical schema;
- split manifest;
- processed sample;
- scaler/preprocessor artifact;
- missingness-mask example;
- leakage-test result;
- data-quality report.

## Do not touch

- model/training implementation;
- explainability implementation;
- API transport;
- dashboard;
- deployment.

## Conflict rule

If a model requirement cannot be satisfied by the real dataset, raise a contract change. Never fabricate a column.
