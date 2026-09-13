# PROJECT SCOPE — MESH

## In scope

### Data
- Real public industrial/prognostics datasets.
- Dataset-specific adapters.
- Immutable raw data and provenance.
- Data-quality checks.
- Asset/run-level splits.
- Training-only normalization.
- Sliding windows.
- Explicit modality masks.

### Machine learning
- RUL regression where legitimate run-to-failure data supports it.
- Fault/degradation classification where labels support it.
- Mask-aware multimodal fusion.
- Missing-modality training and evaluation.
- Calibration/uncertainty.
- Explainability.
- Baselines and ablations.
- Multi-seed reporting for major experiments.

### Application
- FastAPI inference service.
- Streamlit dashboard.
- Sensor evidence.
- Prediction outputs supported by the selected dataset.
- Missing-sensor comparison.
- Explanation view.
- Research/evaluation view.
- Health/model metadata.
- Docker-ready local deployment.

### Quality
- Unit tests.
- Contract tests.
- Integration tests.
- End-to-end tests.
- Versioned model/data/preprocessor identifiers.
- Reproducible release artifacts.

## Out of scope unless separately justified

- Random fake telemetry.
- Fabricated four-sensor datasets.
- Arbitrary 0–100 health scores.
- Production reliability claims without production evidence.
- Automatic work-order creation.
- LLM-generated numerical predictions.
- Decorative AI features.
- Dashboard controls that do not affect a real function.
