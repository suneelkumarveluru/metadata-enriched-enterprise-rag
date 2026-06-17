# Results Template

## Experiment Summary

This document captures the results of comparing Baseline RAG, Metadata-Enriched RAG, and Governance-First RAG.

## Experiment Setup

| Field | Value |
|---|---|
| Dataset | Synthetic enterprise documents |
| Number of documents | 5 |
| Number of chunks | TBD |
| Retrieval method | Keyword baseline / future vector search |
| User roles tested | analyst, manager, auditor |
| Access policy | Role-based access filtering |
| Evaluation date | TBD |

## Compared Approaches

| Approach | Description |
|---|---|
| Baseline RAG | Retrieves chunks using text similarity only |
| Metadata-Enriched RAG | Uses document metadata to improve retrieval and traceability |
| Governance-First RAG | Adds policy-aware filtering and audit logging |

## Test Results

| Query ID | User Role | Query | Expected Chunk | Retrieved Chunk | Allowed? | Hit Rate | Unauthorized Retrieval Rate | Citation Coverage |
|---|---|---|---|---|---|---:|---:|---:|
| q-001 | analyst | claims processing policy | doc-001-chunk-01 | TBD | Yes | TBD | TBD | TBD |
| q-002 | analyst | healthcare compliance report | doc-003-chunk-01 | TBD | No | TBD | TBD | TBD |
| q-003 | manager | finance contract review guide | doc-002-chunk-01 | TBD | Yes | TBD | TBD | TBD |
| q-004 | auditor | healthcare compliance report | doc-003-chunk-01 | TBD | Yes | TBD | TBD | TBD |
| q-005 | analyst | hr policy | doc-005-chunk-01 | TBD | No | TBD | TBD | TBD |

## Observations

- Baseline RAG may retrieve restricted content without policy checks.
- Metadata-Enriched RAG improves traceability by attaching source and governance metadata.
- Governance-First RAG blocks unauthorized retrieval based on access roles.
- Audit logging provides evidence of retrieved, allowed, and blocked chunks.

## Expected Finding

Governance-First RAG is expected to reduce unauthorized retrieval while improving auditability and enterprise readiness.

## Limitations

- Initial results are based on synthetic documents.
- Retrieval is currently keyword-based.
- Future experiments should include vector search and larger datasets.
- Future experiments should evaluate latency, cost, and answer faithfulness with LLM-generated responses.
