# DEFINITION OF DONE — MESH RELEASE

A feature/phase is not complete because the UI looks finished.

## Data done

- [ ] source URL recorded
- [ ] license/terms recorded
- [ ] checksum recorded
- [ ] raw data preserved
- [ ] dataset card completed
- [ ] native sensor semantics verified
- [ ] run/asset identity verified
- [ ] split leakage tested
- [ ] preprocessing versioned
- [ ] scaler fitted on training data only
- [ ] masks verified
- [ ] target definitions documented

## Model done

- [ ] baseline exists
- [ ] proposed model trains reproducibly
- [ ] checkpoint metadata exists
- [ ] evaluation uses held-out assets/runs
- [ ] missing-modality experiments run
- [ ] calibration evaluated
- [ ] explainability outputs verified
- [ ] three-seed result available for major comparisons
- [ ] claims match stored metrics

## API done

- [ ] request schema validated
- [ ] response schema versioned
- [ ] model artifact loads
- [ ] preprocessing matches offline inference
- [ ] health endpoint works
- [ ] model metadata endpoint works
- [ ] missing-modality comparison works

## Dashboard done

- [ ] uses actual API responses
- [ ] displays actual source windows
- [ ] units are visible
- [ ] missing sensors are explicit
- [ ] prediction outputs are traceable
- [ ] uncertainty semantics are documented
- [ ] sensor toggle performs real inference
- [ ] no fake values
- [ ] no decorative charts

## Integration done

- [ ] one stored real example passes end-to-end
- [ ] prediction is numerically consistent offline/API
- [ ] versions are preserved
- [ ] contract tests pass
- [ ] integration tests pass
- [ ] E2E test passes

## Release done

- [ ] code commit identified
- [ ] dataset manifest identified
- [ ] model artifact identified
- [ ] preprocessing artifact identified
- [ ] evaluation report identified
- [ ] limitations documented
- [ ] deployment instructions verified
