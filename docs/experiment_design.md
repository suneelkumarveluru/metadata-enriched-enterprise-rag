# Experiment Design

## Objective

This experiment evaluates whether metadata-enriched and policy-aware retrieval improves enterprise RAG trustworthiness compared with basic vector-search RAG.

## Research Question

Can metadata-enriched and policy-aware retrieval improve retrieval accuracy, governance compliance, citation coverage, and auditability in enterprise RAG systems?

## Compared Approaches

| Approach | Description |
|---|---|
| Baseline RAG | Uses only text chunks and keyword/vector similarity for retrieval |
| Metadata-Enriched RAG | Uses text chunks plus enterprise metadata such as domain, document type, source system, sensitivity, and owner |
| Governance-First RAG | Uses metadata-enriched retrieval plus role-based access filtering and audit logging |

## Sample Dataset

The initial prototype uses synthetic enterprise documents.

| Document ID | Document Type | Domain | Sensitivity | Allowed Roles |
|---|---|---|---|---|
| doc-001 | policy | insurance | internal | analyst, manager, auditor |
| doc-002 | contract | finance | confidential | manager, auditor |
| doc-003 | report | healthcare | restricted | auditor |
| doc-004 | claim | insurance | internal | analyst, manager |
| doc-005 | policy | hr | confidential | manager, auditor |

## Test Queries

| Query ID | User Role | Query | Expected Behavior |
|---|---|---|---|
| q-001 | analyst | claims processing policy | Retrieve internal claims policy |
| q-002 | analyst | healthcare compliance report | Block restricted healthcare report |
| q-003 | manager | finance contract review guide | Retrieve confidential finance contract |
| q-004 | auditor | healthcare compliance report | Retrieve restricted healthcare report |
| q-005 | analyst | hr policy | Block confidential HR policy |

## Evaluation Metrics

| Metric | Definition |
|---|---|
| Hit Rate@5 | Whether the expected chunk appears in the top 5 retrieved results |
| Citation Coverage | Whether generated answer sources match retrieved chunks |
| Unauthorized Retrieval Rate | Percentage of retrieved chunks the user should not access |
| Policy Compliance | Whether retrieval respects metadata access rules |
| Latency | Time taken for query retrieval and filtering |
| Audit Completeness | Whether query, role, document ID, chunk ID, and timestamp are captured |

## Expected Results

The expected result is that Governance-First RAG should reduce unauthorized retrieval compared with Baseline RAG.

Metadata-Enriched RAG is expected to improve traceability and retrieval relevance.

Governance-First RAG is expected to provide the strongest enterprise readiness because it combines metadata, access control, and auditability.

## Limitations

- Initial prototype uses synthetic documents
- Retrieval is currently keyword-based
- Future work should include vector search using Chroma, FAISS, Qdrant, or Weaviate
- Future work should integrate real identity providers such as Azure AD or Okta
- Future work should evaluate larger enterprise document sets
