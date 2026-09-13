# READ FIRST — MESH Rules and Build Order

This is the first document every contributor must read.

## 1. Source of truth

The MESH documentation is the working specification. The supplied DA1 report defines the formal problem statement, initial architecture, starting window configuration, metrics, software stack, feasibility assumptions, and contribution matrix. The earlier project documentation adds real-data, provenance, integration, deployment, and anti-vibe rules.

Do not silently replace documented decisions.

## 2. Absolute rules

- Real measured data for real claims.
- No synthetic replacement for missing industrial measurements.
- No invented targets.
- No leakage.
- No silent modality imputation.
- No arbitrary dashboard metrics.
- No fake confidence.
- No achieved-result claims before experiments.
- One shared repository.
- No direct edits to another owner's protected implementation paths.

## 3. Build order

### Stage 0 — Data truth gate — Naman

For every dataset, create a dataset card containing source, license/terms, files, machine type, sensors, units, sampling information, run identity, labels, missingness, target eligibility, and limitations.

### Stage 1 — Data pipeline — Naman

Build adapters, validation, grouped splits, training-only normalization, windowing, masks, manifests, and QA.

### Stage 2 — Baselines — Prathamesh

Build valid single-modality and simple fusion baselines before the proposed architecture.

### Stage 3 — Proposed model — Prathamesh

Implement the documented CNN-BiLSTM encoders, mask-aware fusion, temporal refiner, supported task heads, modality dropout, calibration, and explainability.

### Stage 4 — Inference API — Sarthak

Expose a versioned model artifact through a stable API using the same preprocessing/schema contract as offline inference.

### Stage 5 — Dashboard — Sarthak

Build the engineer workflow from actual API responses and actual source data.

### Stage 6 — Integration — all

Run a stored real-data example through:

```text
source → preprocessing → model → API → dashboard
```

and verify traceability and numerical consistency.

### Stage 7 — Release — all

Release only a versioned combination of code, dataset manifest, preprocessing artifacts, model artifact, calibration metadata, evaluation report, and deployment configuration.

## 4. Stop conditions

Stop and resolve the issue if:

- a target must be fabricated;
- unrelated datasets are joined only to satisfy a model input shape;
- test data influenced scaling or threshold tuning;
- a dashboard number cannot be traced;
- a missing sensor is replaced with an invented signal;
- a teammate changes another owner's protected implementation;
- an unrun experiment is described as a result.
