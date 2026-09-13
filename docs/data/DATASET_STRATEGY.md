# DATASET STRATEGY — REAL DATA ONLY

## Core rule

A dataset may only be used for the sensors, labels, targets, and physical interpretations it actually contains.

The project must never create a fictional synchronized dataset by combining unrelated machines or experiments.

## Dataset priority

| Priority | Dataset | Real measured data | Main use | Important limitation |
|---|---|---|---|---|
| 1 | NASA FEMTO / PRONOSTIA Bearing | Yes | Run-to-failure degradation/RUL; controlled missing-modality experiments | Does not provide the exact DA1 four-channel set |
| 2 | QIT-CEMC Milling Dataset | Yes | Tool wear + force/torque + vibration/sound experiments | Modality set differs from DA1 wording; verify exact metadata after download |
| 3 | NASA IMS Bearings | Yes | Bearing degradation/RUL validation | Primarily vibration; semantics differ from tool wear |
| 4 | NASA Milling Wear | Yes | Measured milling wear/degradation benchmarking | Modality set differs from DA1 |
| 5 | AI4I 2020 | **Synthetic** | Benchmark/sanity check only | Not evidence of real industrial generalization |

## Source links

### NASA PCoE / FEMTO and other prognostics datasets

Official NASA repository:
https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/

FEMTO archive listed by the project documentation:
https://phm-datasets.s3.amazonaws.com/NASA/10.+FEMTO+Bearing.zip

### QIT-CEMC Milling Dataset

Repository:
https://github.com/wwz456/QIT-CEMC-dataset

Figshare record:
https://figshare.com/articles/dataset/Milling_dataset/27323346

### NASA IMS Bearings

NASA catalog:
https://data.nasa.gov/dataset/ims-bearings

Legacy file listed by NASA:
https://data.nasa.gov/docs/legacy/IMS.zip

### NASA Milling Wear

NASA catalog:
https://data.nasa.gov/dataset/milling-wear

NASA catalog file:
https://data.nasa.gov/docs/legacy/mill.zip

NASA PCoE mirror:
https://phm-datasets.s3.amazonaws.com/NASA/3.+Milling.zip

### AI4I 2020 benchmark

UCI:
https://archive.ics.uci.edu/dataset/601/ai4i%2B2020%2Bpredictive%2Bmaintenance

## Dataset selection gate

Before using a dataset in a headline experiment, confirm:

1. The source is public and permitted for the intended use.
2. Raw files can be preserved or referenced reproducibly.
3. Asset/run identity is available.
4. Sensor semantics and units are documented.
5. The target is genuinely supported.
6. The split can be made without temporal/run leakage.
7. Natural missingness is recorded rather than silently repaired.
8. The dataset is large/varied enough for the proposed experiment.
9. The dataset's limitations are stated next to the result.
10. The dataset is not being used to support a stronger claim than it can support.

## Four-channel issue

The DA1 problem statement names temperature, rotational speed, torque, and tool wear. The verified public dataset set does not provide one clean real dataset containing all four synchronized measurements with a legitimate run-to-failure RUL target.

Therefore MESH uses **dataset-native modality sets**. A future exact-four-channel dataset may be added only after passing the dataset selection gate.
