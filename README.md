# Python API Practices — Examples

Runnable code examples that accompany **Python API Practices — Vol. 1**.

This repository contains **two independent example codebases** that demonstrate the same habits applied to different Python API stacks:

- `fastapi/` — examples using FastAPI-style structure and tooling
- `djangodrf/` — equivalents using Django + Django REST Framework

The goal is to show that the practices are **framework-agnostic**: thin endpoints/views, explicit service workflows, client boundaries for external APIs, repository boundaries for persistence, centralized configuration, and tests that stay fast.

## Dependency management (UV only)

Each codebase is self-contained and uses **UV** for dependency management and virtual environments.
Each folder has its own `pyproject.toml` and `uv.lock`.

You work inside one folder at a time.

## Sync policy

This repository is **synced periodically** from the book’s source repository.
Updates may land in batches (typically per chapter or per release).

- Code in this repository is MIT-licensed (see `LICENSE`).
- The book manuscript and educational text are not included here and are not open source.

