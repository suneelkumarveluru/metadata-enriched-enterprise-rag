# Future Work

This project is currently an initial research prototype. The following areas are planned for future improvement.

## 1. Vector Search Integration

The current retriever uses a simple keyword-based baseline. Future versions should integrate vector search using:

- Chroma
- FAISS
- Qdrant
- Weaviate

This will allow comparison between keyword retrieval, vector retrieval, metadata-filtered retrieval, and governance-first retrieval.

## 2. Metadata-Filtered Retrieval

Future work should extend retrieval logic to support metadata filters such as:

- business_domain
- document_type
- sensitivity
- owner
- source_system
- effective_date
- data_quality_score

This will help evaluate whether metadata improves retrieval relevance and governance compliance.

## 3. Policy Engine

The current policy logic uses simple role-based access control. Future versions should support:

- Role-Based Access Control
- Attribute-Based Access Control
- document-level policies
- sensitivity-based filtering
- business-domain restrictions
- approval-based access

## 4. Enterprise Identity Integration

Future versions should explore integration with identity providers such as:

- Azure Active Directory
- Okta
- AWS IAM Identity Center

This would make the architecture closer to enterprise production patterns.

## 5. RAG Evaluation Enhancements

Future work should include stronger evaluation metrics:

- answer faithfulness
- hallucination detection
- context precision
- context recall
- citation quality
- source attribution accuracy
- unauthorized retrieval rate
- policy compliance score

## 6. Audit and Observability

Future versions should improve audit and observability by capturing:

- user query
- user role
- retrieved chunks
- blocked chunks
- answer sources
- policy decisions
- evaluation scores
- timestamps
- latency
- cost estimates

## 7. Streamlit Demo Application

A Streamlit app can make the project easier to demonstrate.

Planned UI features:

- user role selector
- query input
- retrieved chunk display
- allowed vs blocked chunk display
- generated answer placeholder
- evaluation metrics
- audit log output

## 8. Larger Dataset

The current project uses synthetic documents. Future work should test the architecture using:

- public financial filings
- public healthcare policy documents
- public insurance documents
- synthetic enterprise policy documents
- public government datasets

## 9. Research Paper Completion

Future work includes preparing a full research paper with:

- literature review
- methodology
- experiment results
- architecture diagram
- limitations
- conclusion
- conference submission version

## 10. Conference and Community Submission

Potential submission targets include:

- IEEE BigData workshops
- KDD Applied Data Science track
- Applied Machine Learning Conference
- local Dallas/DFW AI and data meetups
- Databricks, Snowflake, and Microsoft community events
