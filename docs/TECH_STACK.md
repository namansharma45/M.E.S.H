# MESH TECH STACK

## Data layer

- Python
- Pandas
- NumPy
- scikit-learn for selected preprocessing/baseline utilities

## ML layer

- PyTorch
- scikit-learn where appropriate for baselines/evaluation
- SHAP for feature attribution where compatible with the final model/output

## Service layer

- FastAPI
- Pydantic
- Uvicorn

## Dashboard

- Streamlit
- Plotly and/or Matplotlib for purposeful engineering charts

## Deployment

- Docker-ready packaging
- local deployment for DA1/DA2 demonstration

## Testing

- Python unit tests
- data/contract tests
- API contract tests
- integration tests
- end-to-end tests

## Version control

- Git
- GitHub

## Dependency rule

Only add a dependency when a documented project function requires it. Do not install a package because it is popular, visually convenient, or "might be useful later."
