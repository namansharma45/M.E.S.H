# SARTHAK — API + DASHBOARD + INTEGRATION OWNER

## Mission

Build the engineer-facing application, expose the trained artifact through a stable API, and make the full system runnable without inventing data.

## Own

```text
backend/**
frontend/**        # if used by the final repository; DA1 specifies Streamlit
app/**
api/**
deployment/**
pipelines/integration/**
tests/integration/**
tests/end_to_end/**
```

## Required stack

The DA1 architecture specifies:

- FastAPI/lightweight Python backend;
- Streamlit dashboard;
- PyTorch inference engine.

Do not introduce another frontend framework without a documented architecture decision.

## API minimum

```text
GET  /health
GET  /model
POST /predict
POST /compare/missing-modality
```

## Dashboard

Build:

1. overview;
2. sensor evidence;
3. missing-sensor experiment;
4. explanation;
5. research/evaluation view.

## Missing-sensor control

The control must:

1. change the actual modality mask;
2. call inference;
3. receive new output;
4. compare before/after;
5. show the modality as unavailable.

## Traceability

Show where relevant:

- dataset/run;
- source window/timestamp;
- sensor availability;
- data/preprocessor version;
- model version;
- uncertainty semantics;
- inference latency.

## Do not touch

- Naman's preprocessing internals;
- Prathamesh's model/training internals.

## UI rule

Read `docs/product/UI_NO_VIBE_CODE_RULES.md` before building any interface.
