"""
Policy-aware retrieval filter.

This module checks whether a user role is allowed to retrieve a document chunk
based on metadata such as sensitivity and access_role.
"""

from typing import Dict, Any


def is_access_allowed(user_role: str, metadata: Dict[str, Any]) -> bool:
    """
    Check whether the user role is allowed to access a document chunk.

    Args:
        user_role: Role of the user asking the question.
        metadata: Metadata attached to the document chunk.

    Returns:
        True if access is allowed, otherwise False.
    """

    allowed_roles = metadata.get("access_role", [])
    sensitivity = metadata.get("sensitivity", "public")

    if isinstance(allowed_roles, str):
        allowed_roles = allowed_roles.split("|")

    if sensitivity == "public":
        return True

    return user_role in allowed_roles


def filter_allowed_chunks(user_role: str, chunks: list[Dict[str, Any]]) -> list[Dict[str, Any]]:
    """
    Filter document chunks based on user role.

    Args:
        user_role: Role of the user asking the question.
        chunks: List of document chunks with metadata.

    Returns:
        List of chunks the user is allowed to retrieve.
    """

    allowed_chunks = []

    for chunk in chunks:
        metadata = chunk.get("metadata", {})
        if is_access_allowed(user_role, metadata):
            allowed_chunks.append(chunk)

    return allowed_chunks


if __name__ == "__main__":
    sample_chunks = [
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
    results = filter_allowed_chunks(user_role, sample_chunks)

    print(f"User role: {user_role}")
    print("Allowed chunks:")
    for item in results:
        print(item["metadata"]["chunk_id"], "-", item["text"])
