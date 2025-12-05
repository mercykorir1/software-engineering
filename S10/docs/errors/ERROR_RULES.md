# ERROR_RULES.md

ERR-01 API: process_sensor returns one of "stale", "online", or "disabled".
ERR-02 Domain: handle invalid timestamps (non-numeric) by returning "error".
ERR-03 Infra: log metrics for stale sensors only; do not print sensitive info.
ERR-04 Retry: N/A for this function.
ERR-05 Feature toggle: ALERTS_ENABLED must be respected; if False, return "disabled".
