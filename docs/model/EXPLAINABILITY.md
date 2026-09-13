# EXPLAINABILITY

## Purpose

Explain which measured inputs influenced a prediction without pretending that an attribution is physical causality.

## Required evidence

Where supported:

1. per-modality attention weights;
2. feature-level attribution such as SHAP;
3. source window and timestamps;
4. model version;
5. explanation method/version.

## Interpretation rule

Attention is evidence of where the model allocated attention. It is not proof that the sensor caused the failure.

SHAP/feature attribution is an attribution method, not a physical diagnosis.

## Dashboard

The explanation panel should answer:

- Which modality did the model rely on?
- Which input features contributed most?
- Was a modality missing?
- Did the evidence change after a sensor was removed?

Do not display an explanation if the underlying model output or attribution is unavailable.
