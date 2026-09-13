# DATA ACQUISITION — Naman

## Owner

Naman owns dataset acquisition and provenance.

## Directory convention

```text
data/
├── raw/
├── interim/
├── processed/
├── external/
└── benchmarks/
```

## Required acquisition record

For each dataset, record:

```text
dataset_id
dataset_version
source_url
download_url
download_timestamp
original_filename
sha256
license_or_terms
machine_or_equipment_type
sensor_list
units
sampling_information
run_identifier_definition
targets_available
natural_missingness
notes_and_limitations
```

## Procedure

1. Download from the approved/public source.
2. Compute SHA-256 before extraction.
3. Record the source and download date.
4. Store the original archive under the dataset-specific raw directory.
5. Extract without editing source files.
6. Build the dataset card.
7. Build the adapter.
8. Produce processed artifacts from immutable raw input.
9. Record the exact processing configuration and version.

## Never do

- Do not alter raw files in place.
- Do not fabricate unavailable sensors.
- Do not rename a physical quantity into a different physical quantity.
- Do not merge unrelated assets to create a larger artificial sequence.
- Do not commit large raw data unless licensing and repository policy explicitly permit it.

## Dataset card requirement

No dataset enters a final experiment until its dataset card states which tasks are valid: RUL, fault classification, degradation prediction, or benchmark-only use.
