# CCO Generation Examples

This directory contains sample data for the Complex Citation Object (CCO) generation tool. It provides a test case: an input file and the resulting OAI-ORE compliant output object.

## Files in this Directory

| Filename | Description |
| :--- | :--- |
| **`gommapps_input.json`** | The raw, metadata and PID list. This mimics what a user would submit to the tool. |
| **`gommapps_output.json`** | The final, fully resolved OAI-ORE JSON-LD object. This is the expected output after the tool processes the input. |

## The GOMMAPPS Example

These files represent the **Gulf of Mexico Marine Assessment Program for Protected Species (GOMMAPPS)** CCO.

This example verifies the tool's ability to:
* **Ingest Top-Level Metadata:** Mapping project descriptions and creators (BOEM) to the Aggregation level.
* **Resolve PIDs:** Fetching metadata for 38 distinct resources from NCEI, OBIS-SEAMAP, NOAA InPort, and ATN IOOS.
* **Structure Hierarchies:** Detecting that certain PIDs (like the ATN turtle datasets) are parts of a larger collection and structuring the `dcterms:hasPart` / `isPartOf` relationships accordingly.

