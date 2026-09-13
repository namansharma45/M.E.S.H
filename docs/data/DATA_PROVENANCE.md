# DATA PROVENANCE — TRACEABILITY

## Objective

Every training sample, prediction, experiment result, and dashboard value must be traceable.

## Minimum prediction lineage

```text
dataset_id
→ dataset_version
→ run_id
→ window_start/window_end
→ preprocessing_version
→ scaler_version
→ model_version
→ experiment_id
→ API request/response
→ dashboard display
```

## Dashboard rule

If a number cannot be traced to one of:

1. source data;
2. deterministic calculation;
3. model output;
4. stored experiment report;

it must not be displayed.

## Experiment provenance

Every major experiment records:

- Git commit;
- dataset version;
- split version;
- preprocessing/scaler version;
- configuration;
- random seed;
- training date;
- evaluation metrics;
- checkpoint identifier.

## Evidence hierarchy

**Strongest:** measured source record and reproducible calculation.

**Model-derived:** prediction, uncertainty, attention, attribution.

**Experiment-derived:** benchmark/ablation result stored in a report.

**Documentation-only:** methodology statement.

Do not present documentation-only information as live machine evidence.
