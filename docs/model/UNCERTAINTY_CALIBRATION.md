# UNCERTAINTY AND CALIBRATION

## Objective

MESH must not display an arbitrary confidence percentage.

The dashboard should communicate how trustworthy a prediction is using a documented method tied to the model and evaluation data.

## Requirements

A chosen uncertainty method must specify:

- mathematical definition;
- training/validation procedure;
- calibration data;
- output interpretation;
- limitations;
- evaluation metric.

## Examples of acceptable directions

The final method may use a documented probabilistic model, ensemble/MC-style estimate, conformal method, or another justified calibration approach. The chosen method must be selected experimentally rather than added as decoration.

## Forbidden

- `confidence = random()`
- confidence based only on model softmax for an RUL number;
- arbitrary multiplication of scores;
- a fixed "AI confidence" percentage with no calibration evidence.

## Dashboard wording

Use concrete language such as:

- prediction interval;
- calibrated probability;
- uncertainty estimate;
- calibration status.

Avoid vague claims such as "the AI is 98% sure" unless that statement is mathematically justified.
