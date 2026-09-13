# DEPLOYMENT AND OPERATIONS

## Goal

Make the complete MESH stack reproducible locally and Docker-ready without inventing infrastructure behavior.

## Services

The documented architecture requires:

1. inference backend;
2. Streamlit dashboard;
3. model/preprocessor artifacts.

Exact ports and service names must be defined in the implementation configuration rather than guessed in documentation.

## Environment

Never commit:

- API keys;
- passwords;
- access tokens;
- private URLs;
- credentials.

Use `.env.example` for documented variable names.

## Health checks

The service should be able to report:

- process/service health;
- loaded model version;
- loaded preprocessing version;
- readiness of required artifacts.

A healthy API process is not proof that the model is accurate.

## Startup validation

On startup, validate:

- required model artifact exists;
- preprocessing/scaler artifact exists;
- metadata matches expected versions;
- configuration is valid.

## Deployment principle

A deployment is only release-ready when the exact model artifact, data/preprocessor versions, code commit, and evaluation report can be identified.

## Local demonstration

The preferred DA1/DA2 demonstration path is local/Docker-ready using stored real dataset windows, clearly labelled as replayed/stored data rather than live plant telemetry.
