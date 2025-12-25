# Changelog

This repository follows semantic versioning.

## [v0.1.0] – 2025-12-25

### Added
- Initial public release of the examples repository
- FastAPI example codebase
  - Offline demo runnable via `python -m app`
  - Minimal HTTP API (`POST /api/payments`)
  - Client boundary with retry and idempotency handling
  - Repository-style persistence example
- Django / DRF example codebase
  - Offline demo runnable via `python demo.py`
  - Minimal DRF endpoint (`POST /api/payments`)
  - Client, service, and repository separation
- Fully offline-by-default behavior using a mock provider (`mock://`)
- Deterministic test suites for both tracks
- UV-based dependency management
- Project READMEs and contributor-facing documentation

### Notes
- This release focuses on structure, boundaries, and ergonomics rather than feature completeness.
- Authentication, validation, and production hardening are intentionally minimal and covered in the book.
