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
      permissions.py
    clients/
    db/
    services/
    utils/
    manage.py
    app/
      settings.py
      urls.py
      wsgi.py
  tests/
```

## Setup (UV only)

```bash
uv venv
uv sync --extra dev
```

## Run tests

Run pytest from the `djangodrf/` folder.

```bash
cd djangodrf
uv run pytest -q
```

## Run the development server

Run `manage.py` commands from `djangodrf/app/`.

```bash
cd djangodrf/app/
uv run python manage.py runserver
```

## Notes

- This is intentionally minimal.
- Django features not relevant to structure are omitted.
- The focus is on clarity and boundaries.
