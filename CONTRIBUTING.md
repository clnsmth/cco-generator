# Contributing to the CCO Generator

Welcome to the team!

This document contains the "Rules of Engagement" to keep us moving fast without breaking the build.

## 🏗️ Architectural Guardrails (READ THIS)

We are working in a **Monorepo** with strict separation of concerns.

1.  **`cco-core` (The Brain):**
    * **Strict Rule:** Pure Python only. **NEVER** import `fastapi`, `flask`, or web-related libs here.
    * **Goal:** This code must run in an offline script.
    * **Deps:** Only data/logic libraries (`pydantic`, `rdflib`).

2.  **`cco-service` (The Mouth):**
    * **Role:** Wraps the core in an API.
    * **Rule:** This is the *only* place where `fastapi` lives.

3.  **`cco-frontend` (The Face):**
    * **Role:** React/Vite UI. talks to `cco-service` via `/api`.

---

## 🚀 Development Workflows

You have two ways to work. Choose based on your task.

### Option A: The "Full Stack" Flow (Docker)
*Best for: Integration testing, UI dev, checking the full system.*

1.  **Start everything:**
    ```bash
    docker-compose up --build
    ```
2.  **Live Reloading:**
    * Edits to `cco-core` or `cco-service` auto-reload the backend.
    * Edits to `cco-frontend` auto-reload the browser.
3.  **Access:**
    * Frontend: `http://localhost:3000`
    * API Docs: `http://localhost:8000/docs`
    * Redis: `localhost:6379`

### Option B: The "Focused" Flow (Local/Fast)
*Best for: Core logic dev, unit tests, fast iteration.*

**For Python (Core or Service):**
We use `uv` for lightning-fast installs.

```bash
# 1. Go to the component (e.g., core)
cd cco-core

# 2. Sync environment
uv venv
source .venv/bin/activate
uv pip install -e .[dev]

# 3. Test & Lint
pytest
ruff check --fix
```

**For Frontend:**
```bash
cd cco-frontend
npm install
npm run dev
# Test
npm test
```

---

## 📦 Managing Dependencies

**STOP.** Do not just `pip install`. Since we are packaging `cco-core` for PyPI, dependencies must be recorded in `pyproject.toml`.

**To add a Python dependency:**

1. Open `pyproject.toml` in the relevant folder (`cco-core` or `cco-service`).
2. Add the package to the `dependencies = [...]` list.
3. Run `uv pip install -e .` to update your environment.

**To add a Frontend dependency:**

1. `cd cco-frontend`
2. `npm install <package_name>`

---

## ✅ Definitions of Done

Before you commit or open a PR, run the **Sanity Check**:

1. **Core Logic:**
   * Does `pytest` pass in `cco-core`?
   * Did you run `ruff check .`?


2. **API:**
   * Does `pytest` pass in `cco-service`?
   * Did you run `ruff check .`?


3. **Frontend:**
   * Does `npm test` pass?
   * No TypeScript errors in the editor?


## 🤝 Git Workflow

We follow a structured branching model to keep our main branch stable and our history clean.

1. **Branches:**
   * `main`: **Production Ready.** Contains only released versions. Do not push here directly.
   * `development`: **The Working Head.** This branch must always be in a releasable (passing tests) state.
   * `feature/<name>`: Your workspace (e.g., `feature/bibtex-parser`).


2. **The Process:**
   * **Start:** Create your branch off `development`.
   * **Work:** Commit often, but squash tidy before merging.
   * **Merge:** Open a Pull Request (PR) targeting `development`.
   * **Release:** The Lead will merge `development` into `main` on a regular cadence.


3. **Commit Messages (Angular Style):**
We use [Conventional Commits](https://www.conventionalcommits.org/) to automate our changelogs.
**Format:** `<type>(<scope>): <subject> (ref #<issue>)`
* **Types:**
  * `feat`: A new feature
  * `fix`: A bug fix
  * `docs`: Documentation only changes
  * `style`: Formatting, missing semi-colons, etc (no code change)
  * `refactor`: A code change that neither fixes a bug nor adds a feature
  * `test`: Adding missing tests or correcting existing tests
  * `build`: Changes to the build process or auxiliary tools (e.g., Docker, uv)


* **Examples:**
  * `feat(core): add Pydantic model for Aggregation (ref #12)`
  * `fix(frontend): resolve CORS issue in vite proxy (fixes #45)`
  * `docs: update contributing guide with git rules`

