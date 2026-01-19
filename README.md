# Complex Citation Object (CCO) Generator

![WIP](https://img.shields.io)

## Overview

The **Complex Citation Object (CCO) Generator** is a modular software application designed to solve the "data citation scaling problem" in scientific publishing.

Modern research often relies on hundreds or thousands of distinct datasets and software tools. Traditional citation lists in journal articles cannot scale to support this volume, leading to lost credit and broken provenance. This tool enables researchers to collate these references into a single, citable **Complex Citation Object (CCO)** based on the **OAI-ORE (Object Reuse and Exchange)** standard.

This work is informed by the **Research Data Alliance (RDA) Complex Citation Working Group Recommendations**: 
* [**https://doi.org/10.15497/RDA00130**](https://doi.org/10.15497/RDA00130)

## Architecture & Design

This project follows a **"Core Library + Service Wrapper"** architecture to ensure portability and scalability. The system is designed to be deployed by diverse entities including journals, data repositories, and research institutions, without being tightly coupled to a single infrastructure.

### Key Documentation

* **[Product Requirements](docs/requirements.md):** Detailed breakdown of functional, non-functional, and broader business requirements.
* **[Architecture Decision Record (ADR-001)](docs/ADR-001-Architecture.md):** The technical blueprint for the system, including the C4 model, data structures, and core design patterns.

## System Components

The architecture is composed of three primary layers:

1.  **`cco-core` (Python Library):**
    A standalone Python package responsible for the domain logic: parsing BibTeX/Lists, validating inputs, and generating the OAI-ORE graph. It allows for offline, script-based CCO generation.

2.  **`cco-service` (API & Worker):**
    A FastAPI-based web service that wraps the core library. It manages user sessions, handles asynchronous metadata enrichment (fetching titles for raw DOIs), and provides authentication for repository adapters.

3.  **`cco-frontend` (User Interface):**
    A React-based Single Page Application (SPA) providing a human-friendly interface for creating, editing, and publishing CCOs.

## Roadmap

We are currently in the **Architectural Definition** phase. The immediate goals are:

1.  Finalize the OAI-ORE Data Model (Pydantic implementation).
2.  Define the Ingestion Strategy interfaces.
3.  Design the Repository Adapter interface for Zenodo integration.

*See `docs/ADR-001-Architecture.md` for the detailed technical strategy.*
