# Metadata-Enriched Enterprise RAG

A reference implementation for improving enterprise Retrieval-Augmented Generation (RAG) accuracy, governance, and auditability using metadata-enriched data pipelines.

## Research Problem

Most enterprise RAG systems focus on vector search and answer generation, but they often lack strong support for metadata, access control, lineage, sensitivity classification, data quality, and auditability.

This project explores whether metadata-enriched retrieval can improve:

- Retrieval accuracy
- Answer faithfulness
- Governance compliance
- Policy-aware access control
- Source traceability
- Enterprise audit readiness

## Proposed Architecture

Enterprise documents are processed through a metadata-enriched pipeline before retrieval.

```text
Documents
   ↓
Ingestion
   ↓
Chunking
   ↓
Metadata Enrichment
   ↓
Sensitivity Classification
   ↓
Vector Index
   ↓
Policy-Aware Retrieval
   ↓
LLM Answer Generation
   ↓
Citations + Audit Log + Evaluation
## Metadata Fields

The RAG system enriches every document chunk with enterprise metadata before indexing into the vector store.

| Field | Description | Example |
|---|---|---|
| document_id | Unique document identifier | doc-001 |
| chunk_id | Unique chunk identifier | doc-001-chunk-01 |
| document_type | Type of document | policy, claim, contract, report |
| business_domain | Business area | healthcare, finance, insurance |
| sensitivity | Data classification | public, internal, confidential, restricted |
| owner | Business/data owner | claims-team |
| access_role | Roles allowed to retrieve this content | analyst, manager, auditor |
| source_system | Original source | sharepoint, snowflake, s3, databricks |
| effective_date | Date when document became valid | 2026-01-01 |
| data_quality_score | Quality score for document or chunk | 92 |
| lineage_id | Reference to upstream system/pipeline | pipeline-claims-001 |

## How to Run

Clone the repository:

```bash
git clone https://github.com/suneelkumarveluru/metadata-enriched-enterprise-rag.git
cd metadata-enriched-enterprise-rag
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the demo:

```bash
python demo.py
```

Run tests:

```bash
pytest
```


