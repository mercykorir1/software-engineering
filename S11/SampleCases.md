# Sample Cases for S11
Stories: S1 = Offline sensor staleness, S2 = Alerts toggle

---

## S1: Offline Sensor Staleness

### Inputs
- `last_update_time` (float timestamp)
- `ALERTS_ENABLED` (bool toggle)
- Sensor ID (string)

### Outputs
- Status string: `"online"`, `"stale"`, `"disabled"`
- Optional log: `offline_alerts_sent` metric

### Business Rules
- Sensor offline if last update > 60s
- Only one alert per incident
- Feature toggle can disable alerts

### Errors
- None expected; function returns `"disabled"` if feature off

### Equivalence Classes
- `last_update_time`:
  - V1: <60s → online
  - I1: =60s → stale boundary
  - I2: >60s → stale
- `ALERTS_ENABLED`:
  - V2: True → alerts enabled
  - I2: False → disabled

### Boundaries
- `last_update_time`: 59s, 60s, 61s
- `ALERTS_ENABLED`: True / False

### Test Ideas
- TI1 [V1]: last_update = now-30s → online
- TI2 [I1/B]: last_update = now-60s → stale
- TI3 [I2]: last_update = now-61s → stale
- TI4 [ALERTS_OFF]: ALERTS_ENABLED=False → disabled
- TI5 [edge]: last_update = exactly 60s → stale

### Test Cases
- TC1 [S1][V1]: last_update = 30s, ALERTS_ENABLED=True → "online"
- TC2 [S1][I1][B]: last_update = 60s, ALERTS_ENABLED=True → "stale"
- TC3 [S1][I2]: last_update = 61s, ALERTS_ENABLED=True → "stale"
- TC4 [S1][ALERTS_OFF]: last_update = 30s, ALERTS_ENABLED=False → "disabled"
- TC5 [S1][edge]: last_update = 60s exactly → "stale"

---

## S2: Alerts Toggle

### Inputs
- `ALERTS_ENABLED` (bool)
- Sensor breach: temp > threshold

### Outputs
- Alert sent via SMS/email
- Metric: `alert_sent_count`

### Business Rules
- Alerts only sent if toggle is True
- Avoid duplicate alerts for same breach

### Errors
- None, toggle disables alert

### Equivalence Classes
- `ALERTS_ENABLED`: True / False
- Breach duration:
  - V1: >2 mins → alert sent
  - I1: <2 mins → ignored

### Boundaries
- Breach duration: 1 min, 2 min, 3 min

### Test Ideas
- TI1 [V1]: ALERTS_ENABLED=True, breach >2min → alert sent
- TI2 [I1]: ALERTS_ENABLED=True, breach 1min → no alert
- TI3 [ALERTS_OFF]: ALERTS_ENABLED=False → no alert
- TI4 [duplicate prevention]: ALERTS_ENABLED=True, repeated breach → only 1 alert

### Test Cases
- TC6 [S2][V1]: ALERTS_ENABLED=True, breach 3min → SMS/email sent, `alert_sent_count`=1
- TC7 [S2][I1]: ALERTS_ENABLED=True, breach 1min → no alert
- TC8 [S2][ALERTS_OFF]: ALERTS_ENABLED=False, breach 3min → no alert
- TC9 [S2][duplicate]: ALERTS_ENABLED=True, same breach repeated → only 1 alert
