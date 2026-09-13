# MESH DATASET DECISION MATRIX

Use this matrix before assigning a task to a dataset.

| Dataset | Real | RUL | Fault class | Wear/degradation | Multimodal | Missing-modality study | Role |
|---|---|---|---|---|---|---|---|
| NASA FEMTO/PRONOSTIA | Yes | Yes | Dataset-dependent | Yes | Limited/native | Yes | Primary prognostics |
| QIT-CEMC Milling | Yes | Dataset/protocol-dependent | Dataset-dependent | Yes | Yes | Yes | Multisensor/tool-wear research |
| NASA IMS Bearings | Yes | Yes | Limited/dataset-specific | Yes | Mostly vibration | Yes | External RUL validation |
| NASA Milling Wear | Yes | Dataset/protocol-dependent | Limited | Yes | Dataset-specific | Yes where modality permits | Wear validation |
| AI4I 2020 | No — synthetic | Benchmark definition only | Yes | Yes | Tabular multi-sensor | Benchmark only | Sanity/classical benchmark |

## Important

The cells above are planning guidance, not permission to invent labels. Naman must verify exact dataset metadata and target definitions before the dataset is approved for a specific experiment.

## Selection rule

For each experiment, write:

```text
dataset
native modalities
target
split
why this target is legitimate
why this dataset is appropriate
what the result cannot prove
```
