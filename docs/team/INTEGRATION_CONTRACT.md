# INTEGRATION CONTRACT — NAMAN ↔ PRATHAMESH ↔ SARTHAK

## 1. Canonical data object

Naman provides:

- ordered run identity;
- source metadata;
- fixed-length native modality arrays;
- modality mask;
- supported targets;
- preprocessor/scaler version identifiers.

The interface must preserve dataset-specific modality names and semantics.

## 2. Model interface

Prathamesh exposes conceptually:

```python
predict(canonical_batch) -> PredictionBundle
```

Only supported targets and evidence are returned.

## 3. API interface

Sarthak wraps the model package behind HTTP. JSON responses are versioned and serializable.

## 4. Dashboard interface

The dashboard consumes the API contract. It must not manipulate model tensors or import training internals.

## 5. Traceability fields

Every prediction must be traceable to:

```text
dataset_id
dataset_version
split_version
preprocessor_version
scaler_version
model_version
experiment_id
```

## 6. Protected semantic fields

No one silently changes:

- modality names;
- units;
- tensor shape;
- target names;
- mask semantics;
- response schema;
- checkpoint metadata.

## 7. Contract-change process

1. Document reason.
2. Update this contract.
3. Update schemas/examples.
4. Update contract tests.
5. Merge owner change.
6. Update downstream consumer.

## 8. No UI preprocessing

Frontend code must not create model-ready features.
