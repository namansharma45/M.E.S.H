# DASHBOARD SPECIFICATION — SARTHAK

## Product role

The MESH dashboard is an engineer-facing decision-support interface. It is not a marketing website.

## Primary workflow

```text
Select real asset/run/window
        ↓
Inspect measured sensor evidence
        ↓
Request prediction
        ↓
Inspect supported target outputs
        ↓
Inspect uncertainty/calibration
        ↓
Inspect modality attention / attribution
        ↓
Toggle a real sensor offline
        ↓
Run the model again
        ↓
Compare before/after
```

## Required sections

### 1. Overview

Show only information with an operational purpose:

- selected asset/run/window;
- supported prediction(s);
- uncertainty/calibration;
- model version;
- data version;
- inference latency.

### 2. Sensor evidence

Show the actual selected source window.

For each available modality:

- native name;
- unit;
- recent measured values or trend;
- source/run/window reference;
- availability status.

### 3. Missing-sensor experiment

The engineer can mark a supported modality unavailable.

The toggle must:

1. change the actual mask;
2. send a real inference request;
3. receive a new result;
4. compare before/after;
5. state that the modality is unavailable.

### 4. Explanation

Show:

- modality attention;
- feature attribution;
- relevant source window;
- explanation method.

### 5. Research/evaluation

For authorized development/research use:

- baseline metrics;
- ablation results;
- missing-modality results;
- calibration results;
- experiment identifiers.

Do not mix research metrics with a live asset prediction in a way that makes them look like machine telemetry.

## API minimum

The service should support at least:

```text
GET  /health
GET  /model
POST /predict
POST /compare/missing-modality
```

Exact paths may be finalized in the versioned API contract.

## Real-data rule

A dashboard page must never generate its own sensor values or prediction values.

## No "live" claim

If the system is replaying a stored dataset window, label it as a stored/replayed dataset window. Do not call it a live machine feed.
