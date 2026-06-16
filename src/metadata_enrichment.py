"""
Metadata enrichment module.

This module adds enterprise metadata to document chunks before they are indexed
into a vector store for Retrieval-Augmented Generation (RAG).
"""

from typing import Dict, Any, List


def enrich_chunk(
    text: str,
    document_id: str,
    chunk_id: str,
    document_type: str,
    business_domain: str,
    sensitivity: str,
    owner: str,
    access_role: List[str],
    source_system: str,
    effective_date: str,
    data_quality_score: int,
    lineage_id: str,
) -> Dict[str, Any]:
    """
    Create a metadata-enriched document chunk.

    Args:
        text: Text content of the chunk.
        document_id: Unique document identifier.
        chunk_id: Unique chunk identifier.
        document_type: Type of document.
        business_domain: Business domain such as healthcare, finance, or insurance.
        sensitivity: Data classification such as public, internal, confidential, or restricted.
        owner: Business owner of the document.
        access_role: Roles allowed to retrieve this chunk.
        source_system: Original source system.
        effective_date: Date when the content became valid.
        data_quality_score: Quality score for the document or chunk.
        lineage_id: Upstream lineage reference.

    Returns:
        A dictionary containing chunk text and metadata.
    """

    return {
        "text": text,
        "metadata": {
            "document_id": document_id,
            "chunk_id": chunk_id,
            "document_type": document_type,
            "business_domain": business_domain,
            "sensitivity": sensitivity,
            "owner": owner,
            "access_role": access_role,
            "source_system": source_system,
            "effective_date": effective_date,
            "data_quality_score": data_quality_score,
            "lineage_id": lineage_id,
        },
    }


def enrich_sample_chunks() -> List[Dict[str, Any]]:
    """
    Create sample metadata-enriched chunks for demonstration.
    """

    return [
        enrich_chunk(
            text="Internal claims policy for insurance analysts.",
            document_id="doc-001",
            chunk_id="doc-001-chunk-01",
            document_type="policy",
            business_domain="insurance",
            sensitivity="internal",
            owner="claims-team",
            access_role=["analyst", "manager", "auditor"],
            source_system="sharepoint",
            effective_date="2026-01-01",
            data_quality_score=95,
            lineage_id="pipeline-claims-001",
        ),
        enrich_chunk(
            text="Restricted healthcare compliance report for auditors.",
            document_id="doc-003",
            chunk_id="doc-003-chunk-01",
            document_type="report",
            business_domain="healthcare",
            sensitivity="restricted",
            owner="compliance-team",
            access_role=["auditor"],
            source_system="s3",
            effective_date="2026-03-10",
            data_quality_score=88,
            lineage_id="pipeline-compliance-003",
        ),
    ]


if __name__ == "__main__":
    chunks = enrich_sample_chunks()

    for chunk in chunks:
        print(chunk)
