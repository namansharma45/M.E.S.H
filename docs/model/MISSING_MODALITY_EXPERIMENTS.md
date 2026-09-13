# MISSING-MODALITY EXPERIMENTS

## Research question

Does MESH remain useful when one or more sensor modalities are unavailable at inference time?

## Controlled experiment

For each supported modality:

1. start from a held-out full-modality sample;
2. record the original prediction;
3. set that modality's availability mask to `0`;
4. remove/zero its model input according to the documented masking contract;
5. run the actual model again;
6. record the new prediction and uncertainty;
7. calculate the before/after change;
8. repeat across the test set.

## Invalid experiment

This is invalid:

```text
zero sensor values
but keep mask = 1
```

The model must be told that the modality is unavailable.

## Required comparisons

For each dropped modality:

| Condition | RUL | Fault metrics | Uncertainty | Notes |
|---|---:|---:|---:|---|
| Full modality | | | | |
| Drop modality A | | | | |
| Drop modality B | | | | |
| Drop modality C | | | | |

Use only modalities actually present in the selected dataset.

## Natural vs synthetic missingness

Natural missingness from the source must be reported separately from controlled experimental dropout.

Controlled dropout is an experimental perturbation of real measured data; it is not permission to generate synthetic sensor readings.

## Dashboard requirement

The dashboard sensor toggle must execute the same experiment through the real inference service. A front-end-only visual change is not acceptable.
