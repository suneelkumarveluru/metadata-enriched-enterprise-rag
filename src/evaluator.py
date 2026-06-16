"""
RAG evaluation module.

This module provides simple evaluation functions for metadata-enriched and
policy-aware Retrieval-Augmented Generation (RAG).
"""

from typing import Dict, Any, List


def calculate_hit_rate(
    retrieved_chunks: List[Dict[str, Any]],
    expected_chunk_id: str,
) -> float:
    """
    Check whether the expected chunk appears in the retrieved results.

    Args:
        retrieved_chunks: Chunks returned by the retriever.
        expected_chunk_id: The chunk expected to be retrieved.

    Returns:
        1.0 if expected chunk is found, otherwise 0.0.
    """

    for chunk in retrieved_chunks:
        metadata = chunk.get("metadata", {})
        if metadata.get("chunk_id") == expected_chunk_id:
            return 1.0

    return 0.0


def calculate_citation_coverage(
    answer_sources: List[str],
    retrieved_chunks: List[Dict[str, Any]],
) -> float:
    """
    Measure whether generated answer citations match retrieved chunks.

    Args:
        answer_sources: Source chunk IDs cited in the answer.
        retrieved_chunks: Chunks returned by the retriever.

    Returns:
        Fraction of answer sources found in retrieved chunks.
    """

    if not answer_sources:
        return 0.0

    retrieved_chunk_ids = {
        chunk.get("metadata", {}).get("chunk_id")
        for chunk in retrieved_chunks
    }

    matched_sources = [
        source for source in answer_sources if source in retrieved_chunk_ids
    ]

    return len(matched_sources) / len(answer_sources)


def calculate_unauthorized_retrieval_rate(
    retrieved_chunks: List[Dict[str, Any]],
    user_role: str,
) -> float:
    """
    Measure whether retrieved chunks include content the user is not allowed to access.

    Args:
        retrieved_chunks: Chunks returned by the retriever.
        user_role: Role of the user asking the question.

    Returns:
        Fraction of retrieved chunks that are unauthorized.
    """

    if not retrieved_chunks:
        return 0.0

    unauthorized_count = 0

    for chunk in retrieved_chunks:
        metadata = chunk.get("metadata", {})
        sensitivity = metadata.get("sensitivity", "public")
        access_role = metadata.get("access_role", [])

        if isinstance(access_role, str):
            access_role = access_role.split("|")

        if sensitivity != "public" and user_role not in access_role:
            unauthorized_count += 1

    return unauthorized_count / len(retrieved_chunks)


if __name__ == "__main__":
    sample_retrieved_chunks = [
        {
            "text": "Internal claims policy for insurance analysts.",
            "metadata": {
                "document_id": "doc-001",
                "chunk_id": "doc-001-chunk-01",
                "sensitivity": "internal",
                "access_role": ["analyst", "manager", "auditor"],
            },
        },
        {
            "text": "Restricted healthcare compliance report.",
            "metadata": {
                "document_id": "doc-003",
                "chunk_id": "doc-003-chunk-01",
                "sensitivity": "restricted",
                "access_role": ["auditor"],
            },
        },
    ]

    user_role = "analyst"
    expected_chunk_id = "doc-001-chunk-01"
    answer_sources = ["doc-001-chunk-01"]

    print("Hit Rate:", calculate_hit_rate(sample_retrieved_chunks, expected_chunk_id))
    print(
        "Citation Coverage:",
        calculate_citation_coverage(answer_sources, sample_retrieved_chunks),
    )
    print(
        "Unauthorized Retrieval Rate:",
        calculate_unauthorized_retrieval_rate(sample_retrieved_chunks, user_role),
    )
