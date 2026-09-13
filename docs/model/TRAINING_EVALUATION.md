# TRAINING AND EVALUATION — PRATHAMESH

## Evaluation principle

The proposed model must be compared against simpler baselines under the same data split and preprocessing contract.

## Baselines

At minimum, where task-valid:

1. single-modality RUL model;
2. single-modality classifier;
3. concatenation fusion using the same encoders;
4. masked concatenation baseline.

## Splits

Use asset/run-level splits whenever possible.

Do not split overlapping windows from the same physical run across train and test.

## Metrics

### RUL

- RMSE;
- NASA asymmetric score when applicable to the dataset/protocol.

### Classification

- macro-F1;
- per-class recall;
- confusion matrix.

Plain accuracy must not be the only classification metric because rare failure classes can make it misleading.

### Robustness

Report full-modality versus each supported single-modality drop.

### Calibration

Report a calibration metric appropriate to the uncertainty representation, such as coverage/reliability or a documented probabilistic calibration error.

## DA1 target criteria

The report states the intended target:

- RUL RMSE degradation within 10% of the stated single-sensor LSTM baseline under a single dropped modality;
- fault classification macro-F1 within 5% of the full-modality model.

These are **success criteria**, not claimed results.

## Ablations

Run:

- proposed fusion vs concatenation;
- full modality vs each supported modality dropped;
- multi-task vs single-task where valid;
- modality dropout vs no modality dropout;
- temporal refiner depth variants where justified;
- calibration on/off or method comparison where meaningful.

## Seeds

Major comparisons should use three random seeds and report mean ± standard deviation, following the DA1 plan.

## Experiment record

Every run stores:

```text
experiment_id
git_commit
dataset_version
split_version
preprocessor_version
config_version
seed
metrics
checkpoint
notes
```

## Claim discipline

Never write:

> MESH achieves X%

unless the corresponding experiment artifact actually contains X%.
