# FastAPI Examples — Python API Practices

This folder contains a **small, focused FastAPI-style codebase** demonstrating the practices described in **Python API Practices — Vol. 1**.

The goal is not to showcase FastAPI features, but to show how to structure an API so it stays readable, testable, and calm as it grows.

## What this demonstrates

- Thin endpoints that delegate to services
- Explicit service workflows
- Dedicated client modules for external HTTP APIs
- Repository-style persistence boundaries
- Centralized configuration
- Cross-cutting concerns kept out of endpoints

## Project structure

```
fastapi/
  app/
    api.py
    config.py
    clients/
    db/
    services/
    middleware/
  tests/
  demo.py
```

## Setup

```bash
cd fastapi
uv venv
uv sync --extra dev
```

## Quick demo (offline)

This runs a minimal end-to-end workflow (service → client → repository), fully offline by mocking the external payment provider call.

```bash
cd fastapi
uv sync --extra dev
uv run python demo.py
```

## Run the development server and the API

To run the actual HTTP endpoint:

```bash
cd fastapi
uv run uvicorn app.api:app --reload
```

Then:

```bash
curl -s -X POST http://127.0.0.1:8000/api/payments \
  -H "Content-Type: application/json" \
  -d '{"amount":100,"currency":"EUR"}'
```

## Notes

- This is not a production-ready application.
- The examples default to an offline provider stub (mock://...). Set PAYMENT_BASE_URL to a real URL to use a real provider.