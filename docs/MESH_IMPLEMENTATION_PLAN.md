# MESH IMPLEMENTATION PLAN — FROM DOCUMENTATION TO A WORKING SYSTEM

This document translates the project specification into an implementation order. It is intentionally concrete but does not pretend that an experiment has already succeeded.

## Step 1 — Freeze the data truth

Naman selects the first real dataset for the first end-to-end path.

Required output:
- dataset card;
- raw archive;
- checksum;
- parser;
- native modality list;
- valid targets;
- grouped split;
- data-quality report.

## Step 2 — Build one complete data path

Before adding every dataset, make one dataset flow completely through:

```text
raw
→ parsed
→ validated
→ split
→ normalized
→ windowed
→ masked
→ saved
```

Do not begin by writing a large number of adapters without validating one end-to-end path.

## Step 3 — Establish baselines

Prathamesh trains simple models using the exact processed split.

The baseline is the reference point for the research claim. If the complex model cannot beat or meaningfully match a simple baseline, investigate rather than hiding the result.

## Step 4 — Implement the proposed fusion

Build the modality encoders and mask-aware fusion according to `docs/model/MODEL_SPEC.md`.

Validate tensor shapes and mask behavior with unit tests before long training runs.

## Step 5 — Add temporal refinement

Add the 2-layer/4-head Transformer refiner.

Run the planned depth ablation rather than assuming deeper is better.

## Step 6 — Add task heads only when supported

For a run-to-failure dataset, implement RUL if the target definition is legitimate.

For a labelled fault dataset, implement classification if the labels are valid.

For a dataset with only wear measurements, implement degradation/wear prediction instead of inventing failure classes.

## Step 7 — Evaluate missing modalities

Run every supported sensor-drop experiment.

The core evidence should answer:

> How much does performance change when a real modality is unavailable?

## Step 8 — Calibrate uncertainty

Select and evaluate one defensible uncertainty/calibration approach.

Do not put a confidence gauge into the dashboard before the uncertainty semantics are defined.

## Step 9 — Package inference

Prathamesh packages the model and preprocessing metadata behind a stable inference-facing interface.

Sarthak consumes that interface rather than importing training code.

## Step 10 — Build the API

Sarthak implements:
- health;
- model metadata;
- prediction;
- missing-modality comparison.

The API must validate schema and version identifiers.

## Step 11 — Build the dashboard from the API

The dashboard should not know how the model is trained.

It receives:
- measured sensor window;
- predictions;
- uncertainty;
- modality status;
- explanations;
- metadata.

## Step 12 — Validate end-to-end

Select a fixed real-data test example and record its expected output.

Verify:

```text
offline inference == API inference
```

up to explicitly documented numerical tolerance.

## Step 13 — Add additional datasets

Only after one complete path is reliable, add additional real datasets for external validation and modality-specific experiments.

## Step 14 — Release evidence

The final demonstration should show:

1. real measured data;
2. prediction;
3. uncertainty;
4. model evidence;
5. a real sensor-drop experiment;
6. before/after comparison;
7. dataset/model versions;
8. reproducible run instructions.
