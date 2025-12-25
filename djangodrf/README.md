# Django / DRF Examples — Python API Practices

This folder contains a **small Django + Django REST Framework codebase** demonstrating the same practices as the FastAPI examples.

The purpose is to show that these habits apply equally well in Django-based APIs.

## What this demonstrates

- Thin DRF views
- Explicit service workflows
- Client boundaries for external APIs
- Retry + backoff + idempotency
- Repository-style persistence boundaries
- Explicit authorization rules
- Centralized configuration
- Tests that avoid full HTTP stacks where possible

## Project structure

```
djangodrf/
  app/
    api/
      views.py
      urls.py
      permissions.py
    clients/
    db/
    services/
    retries/
    manage.py
    app/
      settings.py
      urls.py
      wsgi.py
  tests/
  demo.py
```

## Setup

```bash
cd djangodrf
uv venv
uv sync --extra dev
```

## Run tests

Run pytest from the `djangodrf/` folder.

```bash
cd djangodrf
uv run pytest
```

## Quick demo (offline)

This runs a minimal end-to-end workflow (service → client → repository) without starting an HTTP server.

```bash
cd djangodrf
uv sync --extra dev
uv run python demo.py
```

## Run the development server and the API

To run the actual HTTP endpoint:

```bash
cd djangodrf/app/
uv run python manage.py runserver
```

Then:

```bash
curl -s -X POST http://127.0.0.1:8000/api/payments \
  -H "Content-Type: application/json" \
  -d '{"amount":100,"currency":"EUR"}'
```

## Notes

- This is intentionally minimal.
- Django features not relevant to structure are omitted.
- The focus is on clarity and boundaries.
- The examples default to an offline provider stub (mock://...). Set PAYMENT_BASE_URL to a real URL to use a real provider.
