# cco-service

This component is the "Service Wrapper". Its job is to expose the logic from `cco-core` over HTTP and manage the asynchronous state with Redis.

## Getting Started

Install `uv`: https://docs.astral.sh/uv/getting-started/installation/

Install `redis`: https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/
Or with Mac Homebrew: `brew install redis`

How to Run It (Local Dev)

```bash
# 1. Navigate to the service directory
cd cco-generator/cco-service

# 2. Create venv and install
# Note: uv will see the "../cco-core" path in pyproject.toml and set it up automatically
uv venv
source .venv/bin/activate
uv pip install -e .

# 3. Run redis
brew services start redis

# 4. Run the server locally
uv run uvicorn cco_service.main:app --reload
```

## Developer Workflow

Run tests and formatting before committing:

```bash
# Run tests
uv run pytest

# Run linter
uv run ruff check --fix
```

