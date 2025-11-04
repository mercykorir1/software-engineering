## Context

NFR-PERF-01 requires p95 < 300ms at 200 RPS for dashboard reads.

## Choice

We choose a read-through cache + cursor pagination to keep read latency low under burst.

## Alternatives Rejected

1. Sharding microservices — rejected due to premature complexity and operational burden.
2. Stateless CDN-only caching — rejected since alerts require up-to-date state.

## Risks & Mitigations

Risk: Stale cache serving. -> Mitigation: Short TTL + cache invalidation on write; verification T-PERF-01.

## Verification Hook

T-PERF-01: k6 test validating p95 < 300ms at 200 RPS. Evidence: /evidence/EV-perf-alerts.pdf
