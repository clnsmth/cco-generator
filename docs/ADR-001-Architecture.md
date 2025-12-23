# ADR-001: Architecture for Complex Citation Object (CCO) Generator

* **Status:** Draft
* **Date:** 2025-12-23
* **Context:** The scientific community lacks a standardized, scalable way to cite thousands of datasets/software in a single journal article. We need a tool to generate OAI-ORE compliant "Complex Citation Objects" (CCOs) that is portable, modular, and user-friendly.

## 1. High-Level Decision

We will implement a **"Core Library + Service Wrapper"** architecture.

* **`cco-core`:** A pure Python library containing the domain logic (parsing, validation, OAI-ORE graph generation). It has no web dependencies and can be used in offline scripts.
* **`cco-service`:** A FastAPI web application that wraps the core library to provide a user interface, session management, and asynchronous metadata enrichment.

This separation ensures the tool is **portable** (can be hosted by Zenodo, a Journal, or a University) and **composable** (the core logic can be reused in other pipelines).

## 2. System Architecture (C4 Model)

### Context

The system acts as a middleware between raw user inputs (BibTeX, Lists) and permanent repositories (Zenodo, etc.).

### Container Design

The application is containerized using Docker to ensure easy deployment by third parties.

1. **Frontend (React):** A Single Page Application (SPA) for manual editing and visualization.
2. **Backend (FastAPI):** Handles API requests, orchestration, and auth flows.
3. **Worker (Background Tasks):** Handles high-latency tasks (fetching metadata for 1000+ IDs) without blocking the UI.
4. **Session Store (Redis):** Stores "Work-in-Progress" CCOs. **Decision:** We do *not* use a permanent database; state is transient.

## 3. Data Model

We use **Pydantic** to enforce the OAI-ORE specification.

* **`Aggregation`:** The central collection object.
* **`AggregatedResource`:** The individual Linked Digital Object (LDO).
* **`ResourceMap`:** The top-level document wrapper (serialized to JSON-LD).

## 4. Key Design Patterns

### A. Ingestion (Strategy Pattern)

To handle diverse inputs without tight coupling, we define a common `BaseIngestor` interface.

* **`BibTexIngestor`:** Parses rich metadata from `.bib` files.
* **`IdentifierListIngestor`:** Parses raw lists of DOIs. Creates "hollow" objects that require enrichment.
* **`OaiOreIngestor`:** Parses existing JSON-LD for the "Edit" workflow.

### B. Publication (Adapter Pattern)

To allow publishing to different repositories, we define a `RepositoryAdapter` interface.

* **`ZenodoAdapter`:** Implements the "Reserve DOI -> Update CCO -> Publish" cycle specific to Zenodo.
* *Future:* Can add `DryadAdapter`, `FigshareAdapter` without changing core logic.

## 5. Deployment & Configuration

* **Containerization:** The system is defined via `docker-compose.yml` orchestrating Backend, Frontend, and Redis.
* **Rebrandable:** The Frontend reads configuration (branding, active adapters) from environment variables to allow hosting institutions to customize the look and feel.

## 6. Consequences

* **Pros:**
  * **High Portability:** Can be deployed anywhere via Docker.
  * **Scalability:** Async workers handle large citation lists preventing timeouts.
  * **Reusability:** `cco-core` can be published to PyPI separately.


* **Cons:**
  * **State Complexity:** Managing state in Redis (vs a standard DB) requires careful expiration handling.
  * **Async UX:** The Frontend must handle "loading" states gracefully while metadata populates in the background.
