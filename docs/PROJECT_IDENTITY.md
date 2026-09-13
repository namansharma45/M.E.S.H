# PROJECT IDENTITY — MESH

## Name

**MESH — Multisensor Engine for System Health**

- **M** — Multisensor
- **E** — Engine
- **S** — System
- **H** — Health

## What MESH is

MESH is a predictive-maintenance research and engineering system that connects:

1. measured sensor data;
2. reproducible data preparation;
3. multimodal temporal ML;
4. explicit missing-modality handling;
5. uncertainty/calibration;
6. explainability;
7. an inference API;
8. an engineer-facing dashboard.

## What MESH is not

MESH is not:

- a synthetic telemetry simulator;
- a generic AI chatbot;
- a decorative analytics dashboard;
- a random health-score generator;
- a collection of unrelated ML demos;
- a system that claims industrial reliability without evidence.

## Core research question

Does mask-aware multimodal fusion provide useful predictive performance and robustness when one or more sensor modalities are unavailable at inference time?

## Engineering question

Can an engineer trace every prediction from the selected real source window through preprocessing, model version, API response, and dashboard display?

## Product principle

The interface should make the evidence understandable without pretending that the model knows more than the data supports.
