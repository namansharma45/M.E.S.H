# DASHBOARD DATA MAPPING

Every visible element must have a defined source.

| Dashboard element | Source | Function |
|---|---|---|
| Asset/run identifier | Source dataset | Identifies physical experiment/run |
| Sensor trend | Raw/processed measured data | Shows actual evidence |
| Sensor availability | Modality mask/source metadata | Shows whether a channel is available |
| RUL | Model prediction | Maintenance planning support where valid |
| Fault/degradation class | Model output | Supports diagnosis/preparation where valid |
| Uncertainty | Calibrated model output | Indicates reliability of prediction |
| Attention weights | Fusion model | Shows modality-level model reliance |
| Feature attribution | Explainability method | Shows influential inputs |
| Model version | Model artifact metadata | Reproducibility |
| Dataset version | Dataset manifest | Reproducibility |
| Preprocessor/scaler version | Data artifacts | Reproducibility |
| Inference latency | API timing | Operational performance |
| Missing-sensor comparison | Two real inference calls | Measures effect of sensor loss |

## Forbidden dashboard values

Do not add:

- arbitrary health score;
- fake machine temperature;
- fake vibration;
- fake uptime;
- fake maintenance savings;
- fake failure probability;
- fake telemetry;
- decorative "AI confidence";
- charts with no engineering interpretation.
