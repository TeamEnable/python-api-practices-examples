# Changelog

This repository follows semantic versioning.

## [v0.1.0] – 2025-12-25

### Added

#### FastAPI track
- Initial FastAPI example codebase
- Offline demo runnable via `python -m app`
- Minimal HTTP API endpoint: `POST /api/payments`
- Explicit client boundary for external HTTP calls
- Retry, backoff, and idempotency handling at the client level
- Repository-style persistence example
- Deterministic test suite
- Offline-by-default provider stub (`mock://`)

#### Django / DRF track
- Initial Django / DRF example codebase
- Offline demo runnable via `python demo.py`
- Minimal DRF endpoint: `POST /api/payments`
- Separation between views, services, clients, and repositories
- Deterministic test suite
- Offline-by-default provider stub (`mock://`)

#### Repository-wide
- UV-based dependency management
- Consistent API paths across frameworks (`/api/*`)
- Public READMEs for each track
- CONTRIBUTING guidelines
- Initial CHANGELOG

### Notes
- This release focuses on structure, boundaries, and ergonomics.
- Authentication, validation, and production hardening are intentionally minimal.
- Examples are designed to run offline by default.
