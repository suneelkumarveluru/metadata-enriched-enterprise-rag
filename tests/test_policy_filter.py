from src.policy_filter import is_access_allowed, filter_allowed_chunks


def test_public_document_allowed_for_any_role():
    metadata = {
        "sensitivity": "public",
        "access_role": [],
    }

    assert is_access_allowed("analyst", metadata) is True


def test_internal_document_allowed_for_valid_role():
    metadata = {
        "sensitivity": "internal",
        "access_role": ["analyst", "manager"],
    }

    assert is_access_allowed("analyst", metadata) is True


def test_restricted_document_blocked_for_invalid_role():
    metadata = {
        "sensitivity": "restricted",
        "access_role": ["auditor"],
    }

    assert is_access_allowed("analyst", metadata) is False


def test_filter_allowed_chunks():
    chunks = [
        {
            "text": "Internal claims policy.",
            "metadata": {
                "chunk_id": "doc-001-chunk-01",
                "sensitivity": "internal",
                "access_role": ["analyst", "manager"],
            },
        },
        {
            "text": "Restricted healthcare compliance report.",
            "metadata": {
                "chunk_id": "doc-003-chunk-01",
                "sensitivity": "restricted",
                "access_role": ["auditor"],
            },
        },
    ]

    allowed = filter_allowed_chunks("analyst", chunks)

    assert len(allowed) == 1
    assert allowed[0]["metadata"]["chunk_id"] == "doc-001-chunk-01"
