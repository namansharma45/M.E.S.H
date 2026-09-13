# COMMON ENGINEERING RULES — ALL THREE MEMBERS

## One source of truth

Shared contracts live in `docs/team/INTEGRATION_CONTRACT.md`.

## One repository

All work happens in the same MESH repository.

## Ownership

- Naman: data.
- Prathamesh: ML.
- Sarthak: API/dashboard/deployment.
- Shared: contracts, docs, integration tests, release.

## No hidden behavior

Do not hide transformations inside:
- dashboard components;
- API route handlers;
- training scripts;
- notebooks.

Important transformations must live in versioned, testable modules.

## No notebook-only system

Notebooks may be used for research exploration, but final logic must be reproducible from project code/configuration.

## Configuration

Do not hard-code:
- dataset paths;
- model versions;
- thresholds;
- window lengths;
- modality names;
- API URLs.

Use versioned configuration where appropriate.

## Reproducibility

Record:
- seed;
- code commit;
- dataset version;
- preprocessing version;
- model version;
- configuration.

## Review

A PR that changes a shared contract must update:
- documentation;
- schema/example;
- contract tests;
- downstream consumer.

## "Looks finished" is not "works"

A dashboard screenshot is not evidence of correctness.

A training loss curve is not evidence of generalization.

A model loading successfully is not evidence of calibration.

A plausible prediction is not evidence of a valid target.
