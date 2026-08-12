# python-ai-service-template

An opinionated FastAPI starter for AI services — typed, linted, tested, and
containerized from commit zero. Clone it to start each new project with a green
CI badge instead of scaffolding you'll "clean up later."

![CI](https://github.com/<you>/<repo>/actions/workflows/ci.yml/badge.svg)

## What's inside

- **FastAPI** app built via an app factory (`app/main.py`) with a `/health`
  endpoint and an example `/v1/generate` endpoint.
- **Pluggable LLM client** (`app/llm.py`) behind a `Protocol`, so routes depend
  on an interface — swap the stub for a real provider without touching handlers.
- **Typed settings** via `pydantic-settings` (`app/config.py`).
- **Ruff** (lint + format), **mypy** (strict), **pytest** (async, ASGI-level).
- **pre-commit** hooks, **GitHub Actions** CI, multi-stage **Dockerfile**
  (non-root, healthcheck), **docker-compose**, and a **Makefile**.

## Quick start

```bash
# 1. Install uv (https://docs.astral.sh/uv/) if you don't have it, then:
make install          # create the venv and install deps
cp .env.example .env  # optional local config

# 2. Run it
make dev              # http://localhost:8000/docs

# 3. The full local gate (identical to CI)
make check            # ruff + mypy + pytest
```

Try the endpoints:

```bash
curl localhost:8000/health
curl -X POST localhost:8000/v1/generate \
  -H 'content-type: application/json' \
  -d '{"prompt": "hello world"}'
```

Or with Docker:

```bash
make docker-up        # build + serve on :8000
```

## Layout

```
app/
  main.py            # app factory + lifespan
  config.py          # typed settings
  observability.py   # logging (add tracing here)
  llm.py             # LLMClient Protocol + StubLLMClient
  dependencies.py    # DI providers
  schemas/           # pydantic request/response models
  api/routes/        # health + generate routers
tests/               # ASGI-level tests via httpx
```

## Using it for a new project

1. Create a repo from this template (GitHub: "Use this template"), or clone and
   re-init git.
2. Rename the project in `pyproject.toml` and the package dir if you like.
3. Replace `StubLLMClient` with a real provider client; keep the `LLMClient`
   interface so nothing else changes.
4. Add endpoints under `app/api/routes/` and schemas under `app/schemas/`.
5. Point the CI badge at your repo and push — the gate runs on every PR.

## Design decisions

- **App factory over a module-level app** so tests build a fresh instance and DI
  overrides are trivial.
- **LLM behind a Protocol** so provider swaps and test doubles need no route
  changes.
- **Ruff + mypy strict in CI** — the quality bar is enforced by the pipeline,
  not by discipline.
- **Multi-stage, non-root Docker image with a healthcheck** so the container is
  deploy-ready, not just runnable.
