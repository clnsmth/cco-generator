#cco-core

## Getting Started

Run these commands in your terminal to set up the environment using uv.

```bash
# 1. Navigate to the core directory
cd cco-monorepo/cco-core

# 2. Initialize the virtual environment
uv venv

# 3. Activate the environment (Mac/Linux)
source .venv/bin/activate
# OR (Windows)
# .venv\Scripts\activate

# 4. Install dependencies (including dev tools)
uv pip install -e ".[dev]"
```

## Developer Workflow

Run tests and formatting before committing:

```bash
# Run tests
pytest

# Run linter
ruff check --fix
```
