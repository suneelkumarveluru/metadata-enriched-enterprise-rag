"""
Document ingestion module.

This module simulates ingestion of enterprise documents from source systems
such as SharePoint, S3, Snowflake, and Databricks.
"""

from typing import Dict, Any, List


def load_sample_documents() -> List[Dict[str, Any]]:
    """
    Load sample enterprise documents.

    Returns:
        List of sample documents with basic source information.
    """

    return [
        {
            "document_id": "doc-001",
            "title": "Claims Processing Policy",
            "document_type": "policy",
            "business_domain": "insurance",
            "source_system": "sharepoint",
            "text": (
                "Claims analysts can review internal claims processing policies. "
                "Managers and auditors can also access this document for operational review."
            ),
        },
        {
            "document_id": "doc-002",
            "title": "Finance Contract Review Guide",
            "document_type": "contract",
            "business_domain": "finance",
            "source_system": "snowflake",
            "text": (
                "Finance contracts include pricing terms, approval workflows, "
                "and vendor obligations. Access is limited to managers and auditors."
            ),
        },
        {
            "document_id": "doc-003",
            "title": "Healthcare Compliance Report",
            "document_type": "report",
            "business_domain": "healthcare",
            "source_system": "s3",
            "text": (
                "This restricted healthcare compliance report includes sensitive audit findings. "
                "Only auditors are allowed to access this document."
            ),
        },
    ]


def chunk_document(document: Dict[str, Any], chunk_size: int = 180) -> List[Dict[str, Any]]:
    """
    Split a document into simple text chunks.

    Args:
        document: Source document dictionary.
        chunk_size: Maximum number of characters per chunk.

    Returns:
        List of chunk dictionaries.
    """

    text = document["text"]
    chunks = []

    for index, start in enumerate(range(0, len(text), chunk_size), start=1):
        chunk_text = text[start : start + chunk_size]

        chunks.append(
            {
                "document_id": document["document_id"],
                "chunk_id": f"{document['document_id']}-chunk-{index:02d}",
                "text": chunk_text,
                "document_type": document["document_type"],
                "business_domain": document["business_domain"],
                "source_system": document["source_system"],
            }
        )

    return chunks


def ingest_documents() -> List[Dict[str, Any]]:
    """
    Load and chunk all sample documents.

    Returns:
        List of document chunks.
    """

    documents = load_sample_documents()
    all_chunks = []

    for document in documents:
        all_chunks.extend(chunk_document(document))

    return all_chunks


if __name__ == "__main__":
    chunks = ingest_documents()

    print("Ingested chunks:")
    for chunk in chunks:
        print(chunk["chunk_id"], "-", chunk["text"])
