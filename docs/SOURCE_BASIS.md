# SOURCE BASIS

This MESH documentation set was assembled from:

1. The supplied DA1 report: `DA1_Report_Final (1)(3).docx`.
2. The supplied latest planning prompt: `Pasted text(3).txt`.
3. The supplied previous MESH/predictive-maintenance documentation archive: `predictive-maintenance-docs-final(1).zip`.
4. The previously established Alfred anti-vibe UI rules, carried forward only where they are relevant to the MESH engineering dashboard.

## Important source-derived decisions retained

- MESH name: Multisensor Engine for System Health.
- Real-data/no-fabrication requirement.
- Dataset-native modality semantics.
- Naman / Prathamesh / Sarthak ownership split.
- CNN-BiLSTM modality encoders.
- Mask-aware cross-attention.
- 2-layer/4-head Transformer temporal refiner.
- Modality dropout starting at p=0.15.
- Supported RUL/fault/anomaly outputs only where targets are legitimate.
- SHAP + modality attention.
- FastAPI + Streamlit + PyTorch stack.
- 20-timestep / stride-5 starting windows.
- Grouped/asset-level splitting and train-only normalization.
- Missing-modality ablations.
- Three-seed reporting for major experiments.
- No-vibe-code UI rules.
- One shared repository with protected ownership boundaries.

## Evidence discipline

The report's metrics and success criteria remain targets unless MESH's own experiments produce the corresponding results. Dataset descriptions that require verification after download are explicitly marked as such.
