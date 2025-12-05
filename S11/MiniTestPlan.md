# Mini Test Plan for S11
Stories Covered: S1 = Offline sensor staleness, S2 = Alerts toggle
Repo: software-engeineering/S10/refactor

## Scope
- Functional: Offline detection, alerts via toggle
- Edge/negative: boundary conditions, feature off, duplicate alerts
- Out of scope: load/performance, full security, property-based tests

## Test Levels & Targets

### S1: Offline sensor staleness
- Unit: `is_sensor_stale`, `process_sensor` logic
- Integration: simulate sensor → backend → dashboard
- System: dashboard shows status for multiple sensors
- UAT: kiosk owner verifies dashboard shows stale correctly

### S2: Alerts toggle
- Unit: check alert functions respect toggle
- Integration: breach → alert system sends SMS/email
- System: end-to-end alert delivery, duplicate prevention
- UAT: PO confirms alert sent according to preferences

## Environments / Repos / CI
- Local: unit tests
- Docker-compose / staging: integration/system tests
- CI: unit tests on PR; integration/system on main

## Entry / Exit Criteria
- Unit: changed-lines coverage ≥ 80%, tests green
- Integration: happy paths + key errors pass; metrics collected
- System: dashboard & alert flow verified
- UAT: ACs verified

## Risks
- Time synchronization across sensors
- Network failures causing false stale
- SMS/email provider delays
- Partially covered now; performance & security deferred

## To Dedicated Testing Course
- Load & endurance for multiple sensors
- Property-based tests for staleness logic
- Security checks (SMS/email auth, data privacy)
