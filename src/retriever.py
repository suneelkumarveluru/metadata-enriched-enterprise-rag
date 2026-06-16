"""
Simple retrieval module.

This module provides a lightweight keyword-based retriever for demonstration.
Later, this can be replaced with vector search using Chroma, FAISS, Qdrant, or Weaviate.
"""

from typing import Dict, Any, List


def keyword_score(query: str, text: str) -> int:
    """
    Calculate a simple keyword overlap score.

    Args:
        query: User question.
        text: Document chunk text.

    Returns:
        Number of query words found in the text.
    """

    query_words = set(query.lower().split())
    text_words = set(text.lower().split())

    return len(query_words.intersection(text_words))


def retrieve_top_k(
    query: str,
    chunks: List[Dict[str, Any]],
    top_k: int = 3,
) -> List[Dict[str, Any]]:
    """
    Retrieve the top-k chunks using simple keyword overlap.

    Args:
        query: User question.
        chunks: List of document chunks.
        top_k: Number of chunks to return.

    Returns:
        Top-k ranked chunks.
    """

    scored_chunks = []

    for chunk in chunks:
        score = keyword_score(query, chunk.get("text", ""))
        scored_chunk = dict(chunk)
        scored_chunk["retrieval_score"] = score
        scored_chunks.append(scored_chunk)

    ranked_chunks = sorted(
        scored_chunks,
        key=lambda item: item["retrieval_score"],
        reverse=True,
    )

    return ranked_chunks[:top_k]


if __name__ == "__main__":
    sample_chunks = [
        {
            "text": "Claims analysts can review internal claims processing policies.",
            "metadata": {
                "document_id": "doc-001",
                "chunk_id": "doc-001-chunk-01",
                "business_domain": "insurance",
            },
        },
        {
            "text": "Only auditors are allowed to access restricted healthcare compliance reports.",
            "metadata": {
                "document_id": "doc-003",
                "chunk_id": "doc-003-chunk-01",
                "business_domain": "healthcare",
            },
        },
    ]

    query = "claims policy"
    results = retrieve_top_k(query, sample_chunks)

    print(f"Query: {query}")
    print("Retrieved chunks:")
    for result in results:
        print(result["retrieval_score"], "-", result["text"])
