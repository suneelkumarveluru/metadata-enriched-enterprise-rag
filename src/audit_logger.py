"""
Audit logging module.

This module captures retrieval activity for enterprise RAG systems, including
user role, query, retrieved chunks, allowed chunks, and evaluation metadata.
"""

from datetime import datetime, timezone
from typing import Dict, Any, List


def create_audit_event(
    user_role: str,
    query: str,
    retrieved_chunks: List[Dict[str, Any]],
    allowed_chunks: List[Dict[str, Any]],
    evaluation_metrics: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Create an audit event for a RAG query.

    Args:
        user_role: Role of the user asking the question.
        query: User question.
        retrieved_chunks: Chunks retrieved before policy filtering.
        allowed_chunks: Chunks allowed after policy filtering.
        evaluation_metrics: RAG evaluation metrics.

    Returns:
        Audit event dictionary.
    """

    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "user_role": user_role,
        "query": query,
        "retrieved_chunk_ids": [
            chunk.get("metadata", {}).get("chunk_id")
            for chunk in retrieved_chunks
        ],
        "allowed_chunk_ids": [
            chunk.get("metadata", {}).get("chunk_id")
            for chunk in allowed_chunks
        ],
        "blocked_chunk_ids": [
            chunk.get("metadata", {}).get("chunk_id")
            for chunk in retrieved_chunks
            if chunk.get("metadata", {}).get("chunk_id")
            not in {
                allowed_chunk.get("metadata", {}).get("chunk_id")
                for allowed_chunk in allowed_chunks
            }
        ],
        "evaluation_metrics": evaluation_metrics,
    }


def print_audit_event(audit_event: Dict[str, Any]) -> None:
    """
    Print audit event in readable format.
    """

    print("\nAudit Event")
    print("-" * 80)
    print(f"Timestamp UTC: {audit_event['timestamp_utc']}")
    print(f"User Role: {audit_event['user_role']}")
    print(f"Query: {audit_event['query']}")
    print(f"Retrieved Chunks: {audit_event['retrieved_chunk_ids']}")
    print(f"Allowed Chunks: {audit_event['allowed_chunk_ids']}")
    print(f"Blocked Chunks: {audit_event['blocked_chunk_ids']}")
    print(f"Evaluation Metrics: {audit_event['evaluation_metrics']}")


if __name__ == "__main__":
    sample_retrieved_chunks = [
        {
            "metadata": {
                "chunk_id": "doc-001-chunk-01",
                "sensitivity": "internal",
                "access_role": ["analyst", "manager", "auditor"],
            }
        },
        {
            "metadata": {
                "chunk_id": "doc-003-chunk-01",
                "sensitivity": "restricted",
                "access_role": ["auditor"],
            }
        },
    ]

    sample_allowed_chunks = [
        {
            "metadata": {
                "chunk_id": "doc-001-chunk-01",
                "sensitivity": "internal",
                "access_role": ["analyst", "manager", "auditor"],
            }
        }
    ]

    sample_metrics = {
        "hit_rate": 1.0,
        "citation_coverage": 1.0,
        "unauthorized_retrieval_rate": 0.0,
    }

    event = create_audit_event(
        user_role="analyst",
        query="healthcare compliance report",
        retrieved_chunks=sample_retrieved_chunks,
        allowed_chunks=sample_allowed_chunks,
        evaluation_metrics=sample_metrics,
    )

    print_audit_event(event)
