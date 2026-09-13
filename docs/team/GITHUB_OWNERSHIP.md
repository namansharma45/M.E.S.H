# GITHUB OWNERSHIP — ONE REPOSITORY, NO OVERLAP

## Core rule

MESH is **one shared repository**.

Do not create:

```text
/prathamesh
/naman
/sarthak
```

Do not create three independent applications.

## Ownership map

| Path | Owner | Others modify directly? |
|---|---|---|
| `data/**` | Naman | No, except approved contract metadata |
| `pipelines/data/**` | Naman | No |
| `configs/data/**` | Naman | PR/contract approval |
| `ml/**` | Prathamesh | No |
| `pipelines/training/**` | Prathamesh | No |
| `pipelines/evaluation/**` | Prathamesh | No |
| `configs/model/**` | Prathamesh | PR/contract approval |
| `configs/training/**` | Prathamesh | PR/contract approval |
| `backend/**` | Sarthak | No |
| `app/**` / dashboard code | Sarthak | No |
| `deployment/**` | Sarthak | No |
| `tests/integration/**` | Sarthak lead | Shared review |
| `tests/end_to_end/**` | Sarthak lead | Shared review |
| `docs/**` | Shared | PR required |
| `tests/contract/**` | Shared | PR required |
| root configs | Shared | PR required |

## Branch naming

```text
main
naman/data-*
prathamesh/model-*
sarthak/app-*
integration/*
```

No direct pushes to `main`.

## File conflict rule

If two owners need the same file:

1. stop;
2. define the interface change;
3. split the file if possible;
4. use an `integration/*` branch if necessary;
5. merge through review.

Do not copy another owner's implementation to bypass ownership.

## PR requirements

Every PR states:

- owner;
- changed paths;
- why the change belongs there;
- tests run;
- contract impact;
- artifact/version impact.

## Commit examples

```text
data: add FEMTO adapter
model: add masked attention
train: add RUL baseline
api: add prediction contract
app: add sensor evidence panel
infra: add health check
test: add missing-modality contract
```

Avoid commits such as `final changes`, `stuff`, `misc`, or `update`.
