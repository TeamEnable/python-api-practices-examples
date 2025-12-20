# FastAPI Examples — Python API Practices

This folder contains a **small, focused FastAPI-style codebase** demonstrating the practices described in **Python API Practices — Vol. 1**.

The goal is not to showcase FastAPI features, but to show how to structure an API so it stays readable, testable, and calm as it grows.

## What this demonstrates

- Thin endpoints that delegate to services
- Explicit service workflows
- Dedicated client modules for external HTTP APIs
- Retry + backoff + idempotency at the client boundary
- Repository-style persistence boundaries
- Centralized configuration
- Cross-cutting concerns kept out of endpoints
- Tests that focus on behavior, not plumbing

## Project structure

```
fastapi/
  app/
    clients/
    db/
    middleware/
    retries/
    utils/
    app.py
  tests/
```

## Setup (UV only)

```bash
uv venv
uv sync --extra dev
```

## Run tests

```bash
uv run pytest -q
```

## Run the demo

```bash
uv run python app/app.py
```

## Notes

- This is not a production-ready application.
- Structure and intent matter more than completeness.
