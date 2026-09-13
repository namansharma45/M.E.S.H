# EXECUTION ROADMAP — FULL MESH BUILD

This is the complete project roadmap, not an MVP checklist.

## Phase 1 — Repository discipline
**Lead:** Sarthak; all review.

- one shared repository;
- protected ownership boundaries;
- documentation;
- branch rules;
- contracts;
- test structure.

## Phase 2 — Real data acquisition
**Owner:** Naman.

Acquire and document:
- NASA FEMTO/PRONOSTIA;
- NASA IMS Bearings;
- NASA Milling Wear;
- QIT-CEMC.

Keep AI4I 2020 isolated as benchmark-only.

## Phase 3 — Data pipeline
**Owner:** Naman.

Deliver:
- adapters;
- canonical native-modality schema;
- asset/run-level splits;
- train-only normalization;
- 20-step/stride-5 starting windows;
- masks;
- QA reports;
- manifests.

## Phase 4 — Baselines
**Owner:** Prathamesh.

Deliver:
- single-modality baselines;
- valid classifier;
- concatenation fusion;
- masked concatenation.

## Phase 5 — Proposed model
**Owner:** Prathamesh.

Deliver:
- modality encoders;
- mask-aware cross-attention;
- temporal refiner;
- supported task heads;
- modality dropout;
- uncertainty/calibration;
- explainability.

## Phase 6 — Ablations
**Owner:** Prathamesh; Naman supports data generation.

Run:
- fusion comparisons;
- modality-drop tests;
- multi-task vs single-task where valid;
- dropout variants;
- justified architecture-depth checks.

## Phase 7 — API
**Owner:** Sarthak.

Deliver:
- schema validation;
- checkpoint loading;
- prediction;
- missing-modality comparison;
- health/model metadata;
- reproducibility check.

## Phase 8 — Dashboard
**Owner:** Sarthak.

Deliver:
- run/window selection;
- measured sensor evidence;
- predictions;
- uncertainty;
- missing-sensor experiment;
- explanations;
- research/evaluation view.

## Phase 9 — Integration
**All.**

Run the same stored real-data example through the full stack.

## Phase 10 — Release
**All.**

Release:
- source commit;
- model artifact;
- preprocessor/scaler artifact;
- dataset manifest;
- experiment report;
- calibration metadata;
- deployment configuration;
- limitations;
- evidence screenshots from real data.
