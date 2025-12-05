# AI Use Log

## 2025-12-05 — Smart Freezer Refactor
- **Prompt summary:** Asked AI to suggest a way to separate logic from logging in process_sensor().
- **Kept:** The suggestion to create `determine_sensor_status()` for core logic and `log_sensor_status()` for printing.
- **Rejected:** Any suggestion to change return values or add correlationId (too advanced for current assignment).
- **Verification:** Unit tests for stale, online, and alerts-disabled paths pass; CI green; prints work as expected.
