# Product Requirements: Complex Citation Object (CCO) Generator

## 1. Functional Requirements
**What the system must do.**

* **OAI-ORE Compliance:** Create CCOs following the Open Archives Initiative Object Reuse and Exchange schema.
* **Collation:** Collate Linked Digital Objects (LDOs) into a single aggregation.
* **Graph Generation:** Produce valid Resource Maps in JSON-LD format.
* **Input Support:**
    * Accept persistent resource identifiers (DOIs, IGSNs).
    * Convert BibTeX lists of resources.
    * Convert simple IGSN/DOI lists.
* **Relationship Management:** Allow users to specify relationships (predicates) between LDOs and the CCO.
* **Editability:** Allow users to upload an existing CCO object to edit/rehydrate.
* **Interfaces:**
    * **UI:** Webform for manual human construction.
    * **API:** Autonomous workflow for machine users.
* **Validation:** Ensure CCOs are compliant with OAI-ORE and downstream constraints.

## 2. Non-Functional Requirements
**System attributes and technical constraints.**

* **Machine-Readability:** Relationships must be semantically expressive (RDF/JSON-LD).
* **Dual-User Support:** System must be optimized for both human interaction and API automation.
* **Core Stack:**
    * Logic: Python (distributed as a PyPI package).
    * API: FastAPI.
    * Frontend: Modern Language (React).
* **Scalability:** Designed to handle high user load and large batches of citations (1000+).

## 3. Broader Requirements
**Business goals and ecosystem constraints.**

* **Downstream Compliance:** CCOs must meet requirements of Crossref, DataCite, ORCID, and JATS4R.
* **Portability:** The system must be deployable by diverse hosts (Journals, Repositories), meaning it cannot be tightly coupled to a single entity's infrastructure.
* **Repository Connection:** The system must support adapters to publish CCOs to repositories (e.g., Zenodo) to mint a DOI.
