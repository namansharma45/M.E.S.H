# NO HALLUCINATION / NO-BULLSHIT POLICY

## Purpose

MESH must be credible as an engineering/research system.

## Data rules

Never generate:

- fake sensor streams;
- fake real-time telemetry;
- fake machine identifiers;
- fake timestamps;
- fabricated failure events;
- invented sensor modalities;
- copied measurements from another asset;
- synthetic values disguised as measurements.

Synthetic data may only exist in a clearly isolated, explicitly labelled experiment if the team later documents why it is needed. It must never be presented as real machine evidence.

## Target rules

Never invent:

- RUL labels;
- fault classes;
- failure thresholds;
- degradation stages;
- maintenance outcomes.

If a dataset does not support a target, that target is unavailable for that dataset.

## Dashboard rules

Every displayed value must be:

1. measured source data;
2. deterministic calculation;
3. model output;
4. stored experiment result;
5. traceability metadata.

## Claim rules

Never copy a paper's metric into the project results.

Allowed:
> Paper [X] reported metric Y on dataset Z.

Not allowed:
> MESH achieves metric Y.

unless MESH actually produced it.

## Model rules

Do not call attention weights "causal importance".

Do not call a raw softmax "calibrated confidence".

Do not call a prediction "real-time" unless the system is connected to a real stream.

## UI rules

No decorative values.

No "AI confidence" meter without calibration.

No fake uptime, savings, health, risk, or maintenance counters.

## Failure behavior

When information is unavailable, say:

- unavailable;
- not supported by this dataset;
- not calibrated;
- no prediction available.

Never fill the gap with a plausible-looking number.
