"""
Demo pipeline for Metadata-Enriched Enterprise RAG.

This script connects:
1. Document ingestion
2. Metadata enrichment
3. Retrieval
4. Policy-aware filtering
5. Evaluation
"""
from src.audit_logger import create_audit_event, print_audit_event
from src.ingestion import ingest_documents
from src.metadata_enrichment import enrich_chunk
from src.retriever import retrieve_top_k
from src.policy_filter import filter_allowed_chunks
from src.evaluator import (
    calculate_hit_rate,
    calculate_citation_coverage,
    calculate_unauthorized_retrieval_rate,
)


def build_metadata_enriched_chunks():
    """
    Build sample chunks with enterprise metadata.
    """

    raw_chunks = ingest_documents()
    enriched_chunks = []

    for chunk in raw_chunks:
        document_id = chunk["document_id"]
        chunk_id = chunk["chunk_id"]

        if document_id == "doc-001":
            sensitivity = "internal"
            owner = "claims-team"
            access_role = ["analyst", "manager", "auditor"]
            effective_date = "2026-01-01"
            data_quality_score = 95
            lineage_id = "pipeline-claims-001"

        elif document_id == "doc-002":
            sensitivity = "confidential"
            owner = "finance-team"
            access_role = ["manager", "auditor"]
            effective_date = "2026-02-15"
            data_quality_score = 91
            lineage_id = "pipeline-finance-002"

        elif document_id == "doc-003":
            sensitivity = "restricted"
            owner = "compliance-team"
            access_role = ["auditor"]
            effective_date = "2026-03-10"
            data_quality_score = 88
            lineage_id = "pipeline-compliance-003"

        else:
            sensitivity = "public"
            owner = "unknown"
            access_role = []
            effective_date = "2026-01-01"
            data_quality_score = 80
            lineage_id = "unknown"

        enriched_chunk = enrich_chunk(
            text=chunk["text"],
            document_id=document_id,
            chunk_id=chunk_id,
            document_type=chunk["document_type"],
            business_domain=chunk["business_domain"],
            sensitivity=sensitivity,
            owner=owner,
            access_role=access_role,
            source_system=chunk["source_system"],
            effective_date=effective_date,
            data_quality_score=data_quality_score,
            lineage_id=lineage_id,
        )

        enriched_chunks.append(enriched_chunk)

    return enriched_chunks


def run_demo():
    """
    Run the end-to-end metadata-enriched and policy-aware RAG demo.
    """

    query = "healthcare compliance report"
    user_role = "analyst"
    expected_chunk_id = "doc-003-chunk-01"

    print("=" * 80)
    print("Metadata-Enriched Enterprise RAG Demo")
    print("=" * 80)

    print(f"\nUser role: {user_role}")
    print(f"Query: {query}")

    enriched_chunks = build_metadata_enriched_chunks()

    print("\nStep 1: Metadata-enriched chunks created")
    for chunk in enriched_chunks:
        metadata = chunk["metadata"]
        print(
            f"- {metadata['chunk_id']} | "
            f"domain={metadata['business_domain']} | "
            f"sensitivity={metadata['sensitivity']} | "
            f"access_role={metadata['access_role']}"
        )

    retrieved_chunks = retrieve_top_k(query, enriched_chunks, top_k=3)

    print("\nStep 2: Retrieved chunks before policy filtering")
    for chunk in retrieved_chunks:
        metadata = chunk["metadata"]
        print(
            f"- {metadata['chunk_id']} | "
            f"score={chunk['retrieval_score']} | "
            f"sensitivity={metadata['sensitivity']}"
        )

    allowed_chunks = filter_allowed_chunks(user_role, retrieved_chunks)

    print("\nStep 3: Retrieved chunks after policy filtering")
    if not allowed_chunks:
        print("- No chunks allowed for this user role.")
    else:
        for chunk in allowed_chunks:
            metadata = chunk["metadata"]
            print(
                f"- {metadata['chunk_id']} | "
                f"sensitivity={metadata['sensitivity']} | "
                f"text={chunk['text']}"
            )

    answer_sources = [
        chunk["metadata"]["chunk_id"]
        for chunk in allowed_chunks
    ]

    hit_rate = calculate_hit_rate(retrieved_chunks, expected_chunk_id)
    citation_coverage = calculate_citation_coverage(answer_sources, allowed_chunks)
    unauthorized_rate = calculate_unauthorized_retrieval_rate(
        allowed_chunks,
        user_role,
    )

    print("\nStep 4: Evaluation Metrics")
    print(f"- Hit Rate: {hit_rate}")
    print(f"- Citation Coverage: {citation_coverage}")
    print(f"- Unauthorized Retrieval Rate: {unauthorized_rate}")
    hit_rate = calculate_hit_rate(retrieved_chunks, expected_chunk_id)
    citation_coverage = calculate_citation_coverage(answer_sources, allowed_chunks)
    unauthorized_rate = calculate_unauthorized_retrieval_rate(
        allowed_chunks,
        user_role,
    )

    print("\nStep 4: Evaluation Metrics")
    print(f"- Hit Rate: {hit_rate}")
    print(f"- Citation Coverage: {citation_coverage}")
    print(f"- Unauthorized Retrieval Rate: {unauthorized_rate}")

    evaluation_metrics = {
        "hit_rate": hit_rate,
        "citation_coverage": citation_coverage,
        "unauthorized_retrieval_rate": unauthorized_rate,
    }

    audit_event = create_audit_event(
        user_role=user_role,
        query=query,
        retrieved_chunks=retrieved_chunks,
        allowed_chunks=allowed_chunks,
        evaluation_metrics=evaluation_metrics,
    )

    print_audit_event(audit_event)

    print("\nInterpretation:")
    print(
        "The query retrieves healthcare compliance content, but because the user role "
        "is analyst and the healthcare report is restricted to auditors, policy-aware "
        "retrieval blocks the restricted chunk."
    )

if __name__ == "__main__":
    run_demo()
