# MESH — Multisensor Engine for System Health

> **M**ultisensor **E**ngine for **S**ystem **H**ealth

MESH is a research-grade predictive-maintenance system for measured industrial/prognostics data. It is designed to turn real sensor observations into traceable maintenance decision support through data engineering, multimodal machine learning, missing-sensor robustness experiments, explainability, an inference API, and an engineer-facing dashboard.

This is **not an MVP specification**. The repository is intended to grow into a complete, reproducible system with real-data validation, baselines, ablations, calibration, integration tests, deployment, and release traceability.

## 1. Non-negotiable principles

1. **Real data only for real claims.** No random telemetry, fake live mode, fabricated sensor readings, or invented industrial measurements.
2. **No fabricated modalities.** Never combine measurements from unrelated machines/datasets to manufacture a four-sensor sample.
3. **No invented targets.** RUL, fault class, degradation, anomaly, and uncertainty must have a documented definition.
4. **No silent imputation.** Missing modalities remain missing and are represented explicitly by a modality mask.
5. **No leakage.** Splits are by asset/run wherever possible; preprocessing and threshold tuning use training data only.
6. **No decorative dashboard metrics.** Every displayed number must be a source value, deterministic calculation, model output, or saved experiment result.
7. **No fake confidence.** Confidence/uncertainty must come from a documented statistical/modeling method.
8. **Research claims require evidence.** A target metric is not an achieved result until the experiment has actually been run.
9. **One repository, three owners.** Naman, Prathamesh, and Sarthak work in separate responsibility boundaries inside one shared architecture.
10. **No vibe coding.** MESH is an engineering console, not a generic AI/SaaS landing page.

## 2. Team ownership

| Member | Primary ownership | Does not own |
|---|---|---|
| **Naman** | Real-data acquisition, adapters, cleaning, QA, canonical schema, grouped splits, windowing, normalization, masks, data manifests | Model architecture/training, API transport, dashboard, deployment |
| **Prathamesh** | Baselines, model architecture, training, evaluation, ablations, calibration, checkpoints, explainability | Raw-data preprocessing internals, API transport, dashboard, deployment |
| **Sarthak** | FastAPI service, Streamlit dashboard, integration, deployment, operational UX, integration/E2E tests | Data-processing internals, model/training internals |

See `docs/team/GITHUB_OWNERSHIP.md` for protected paths and branch rules.

## 3. End-to-end flow

```text
REAL SOURCE DATA
      ↓
Naman: acquisition + provenance + QA
      ↓
Naman: canonical representation + splits + normalization + windows + masks
      ↓
Prathamesh: baselines
      ↓
Prathamesh: mask-aware multimodal model
      ↓
Prathamesh: evaluation + missing-modality ablations + calibration + explainability
      ↓
Sarthak: FastAPI inference service
      ↓
Sarthak: Streamlit engineer dashboard
      ↓
All: contract + integration + end-to-end tests
      ↓
Sarthak: Docker-ready deployment
      ↓
All: reproducible release bundle
```

## 4. Current research design from DA1

The DA1 report defines the starting architecture as:

- per-modality **1D-CNN + BiLSTM** encoders;
- **mask-aware cross-attention fusion** as the central novelty;
- a lightweight **2-layer, 4-head Transformer temporal refiner**;
- joint task heads for RUL, fault type, and anomaly score where the selected dataset legitimately supports them;
- modality dropout starting at **p = 0.15**;
- SHAP plus per-modality attention;
- PyTorch for ML, Python backend, and Streamlit dashboard. The report describes the software pipeline as raw sensors → preprocessing → mask-aware fusion → prediction → dashboard and the served architecture as a Streamlit front end, Python backend, and PyTorch inference engine. 

The report's formal success target is to keep RUL degradation within 10% of the stated single-sensor LSTM baseline under a single dropped modality and keep classification macro-F1 within 5% of the full-modality model. These are **targets, not results**.

## 5. Important dataset correction

The DA1 report uses AI4I 2020 as its primary dataset, but the project documentation treats the public AI4I 2020 dataset as synthetic. Therefore:

- AI4I 2020 may be used for loader/API sanity checks and classical benchmark experiments.
- AI4I 2020 must **not** be presented as proof of real industrial generalization.
- Real-data claims must use measured datasets such as NASA FEMTO/PRONOSTIA, NASA IMS Bearings, NASA Milling Wear, and QIT-CEMC, subject to dataset-specific modality and target support.

No public real dataset currently verified by this project provides one clean synchronized sample containing all four DA1-named channels — temperature, rotational speed, torque, and tool wear — together with a clean run-to-failure RUL target. The implementation must therefore preserve native dataset semantics instead of fabricating a common four-channel dataset.

## 6. Documentation map

### Read first
- `docs/01_READ_FIRST.md`
- `docs/PROJECT_IDENTITY.md`
- `docs/PROJECT_SCOPE.md`

### Data
- `docs/data/DATASET_STRATEGY.md`
- `docs/data/DATA_ACQUISITION.md`
- `docs/data/DATA_PIPELINE.md`
- `docs/data/DATA_PROVENANCE.md`
- `docs/data/DATASET_CARD_TEMPLATE.md`

### Model
- `docs/model/MODEL_SPEC.md`
- `docs/model/TRAINING_EVALUATION.md`
- `docs/model/MISSING_MODALITY_EXPERIMENTS.md`
- `docs/model/UNCERTAINTY_CALIBRATION.md`
- `docs/model/EXPLAINABILITY.md`

### Product / UI
- `docs/product/DASHBOARD_SPEC.md`
- `docs/product/DASHBOARD_DATA_MAPPING.md`
- `docs/product/UI_NO_VIBE_CODE_RULES.md`

### Architecture / operations
- `docs/architecture/SYSTEM_ARCHITECTURE.md`
- `docs/DEPLOYMENT_OPERATIONS.md`
- `docs/EXECUTION_ROADMAP.md`
- `docs/DEFINITION_OF_DONE.md`

### Team / integration
- `docs/team/NAMAN_DATA.md`
- `docs/team/PRATHAMESH_MODEL.md`
- `docs/team/SARTHAK_DASHBOARD.md`
- `docs/team/INTEGRATION_CONTRACT.md`
- `docs/team/GITHUB_OWNERSHIP.md`

### Research integrity
- `docs/NO_HALLUCINATION_POLICY.md`
- `docs/LITERATURE_TO_IMPLEMENTATION.md`

## 7. Stack

| Layer | Technology |
|---|---|
| Data | Python, Pandas, NumPy |
| ML | PyTorch, scikit-learn |
| Explainability | SHAP + model attention outputs |
| API | FastAPI + Pydantic + Uvicorn |
| Dashboard | Streamlit |
| Charts | Plotly / Matplotlib where each chart has a real engineering purpose |
| Packaging | Docker-ready |
| Version control | GitHub |
| Testing | Python unit/contract/integration/E2E tests |

Do not add libraries merely because they are fashionable or convenient.

## 8. Build philosophy

MESH should answer a real maintenance question:

> **Given the measured condition of an asset, what does the model predict, how reliable is that prediction, which sensor evidence mattered, and what changes when a sensor is unavailable?**

Anything that cannot contribute to that question should not become a dashboard element or model output.
