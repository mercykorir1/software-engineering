# DIFF.md
Before:
- process_sensor mixed logic + logging
- single function handled everything

After:
- Extracted determine_sensor_status() for pure logic
- Extracted log_sensor_status() for printing/logging
- process_sensor() calls both for cleaner structure
- Added comments to explain each function

Tests:
- All previous tests pass
- Added new tests for alerts disabled

Risks/Edge Cases:
- Time drift may affect staleness calculation
- ALERTS_ENABLED toggle must be reset in tests

Peer Review:
- Strong choice: clearer separation of logic vs side effects
- Risk: none
- Question: threshold_seconds hardcoded; consider config per sensor
