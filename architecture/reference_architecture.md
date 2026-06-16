# Reference Architecture

This project proposes a metadata-enriched and policy-aware Retrieval-Augmented Generation (RAG) architecture for enterprise data platforms.

## Architecture Flow

```text
Enterprise Documents
        ↓
Document Ingestion
        ↓
Text Extraction
        ↓
Chunking
        ↓
Metadata Enrichment
        ↓
Sensitivity Classification
        ↓
Embedding Generation
        ↓
Vector Store
        ↓
Policy-Aware Retrieval
        ↓
LLM Answer Generation
        ↓
Citations + Audit Log + Evaluation

```

## Main Components

### 1. Document Ingestion

Collects enterprise documents from sample sources such as SharePoint, S3, Snowflake, Databricks, and internal document repositories.

### 2. Text Extraction

Extracts readable text from enterprise documents such as policies, claims, contracts, reports, and operational documents.

### 3. Chunking

Breaks documents into smaller searchable chunks. Each chunk receives a unique `chunk_id`.

### 4. Metadata Enrichment

Adds business and governance metadata to every chunk, including document type, business domain, sensitivity, owner, access role, source system, effective date, data quality score, and lineage ID.

### 5. Sensitivity Classification

Classifies each document or chunk as public, internal, confidential, or restricted.

### 6. Embedding Generation

Converts text chunks into vector embeddings for semantic search.

### 7. Vector Store

Stores embeddings and metadata for retrieval. Possible vector stores include FAISS, Chroma, Qdrant, and Weaviate.

### 8. Policy-Aware Retrieval

Before returning results, the retriever checks user role, document sensitivity, access permissions, business domain, and metadata filters.

Example:

```text
User role: analyst
Document sensitivity: restricted
Allowed role: auditor

Result: document is not retrieved
```

### 9. LLM Answer Generation

The LLM generates an answer only from allowed retrieved context.

### 10. Citations and Audit Log

Every answer should capture the user query, user role, retrieved document IDs, chunk IDs, source metadata, generated answer, timestamp, and evaluation score.

## Baseline vs Proposed Approach

| Approach | Description | Limitation |
|---|---|---|
| Basic RAG | Vector search over chunks | No strong governance |
| Metadata RAG | Uses metadata filters | Better traceability |
| Governance RAG | Adds role-based policy checks | Enterprise-ready pattern |

## Key Research Hypothesis

Metadata-enriched and policy-aware retrieval can improve enterprise RAG trustworthiness by increasing retrieval accuracy, reducing unauthorized access, and improving auditability.
