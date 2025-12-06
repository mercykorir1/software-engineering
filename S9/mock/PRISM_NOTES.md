# PRISM Mock Notes

Run mock server:
npx @stoplight/prism-cli mock ./docs/api/openapi.yaml --port 4010

Mapped examples:

- GET /v1/kiosks → examples/kiosks_list.json
- GET /v1/alerts → examples/alerts_list.json
- POST /v1/alerts → examples/alert_create.json
- Errors forced with example=error_422.json or example=error_409.json
