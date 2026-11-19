from rag_retrieval.chunking import chunk_documents, chunk_text
from rag_retrieval.context import build_context
from rag_retrieval.documents import load_documents
from rag_retrieval.retrieval import retrieve
from rag_retrieval.answer import answer_query


def test_chunking_preserves_all_text():
    text = "abcdefghijklmnopqrstuvwxyz0123456789"
    chunks = chunk_text(text, chunk_size=10, overlap=4)
    joined = "".join(chunks)
    assert "z" in "".join(chunks)
    for piece in chunks:
        assert len(piece) > 0
    reconstructed = chunks[0]
    for piece in chunks[1:]:
        reconstructed += piece
    assert set(text).issubset(set(reconstructed))


def test_chunking_applies_overlap():
    text = "0123456789abcdefghij"
    chunks = chunk_text(text, chunk_size=10, overlap=4)
    assert len(chunks) >= 2
    first_tail = chunks[0][-4:]
    second_head = chunks[1][:4]
    assert first_tail == second_head


def test_department_filter_excludes_other_departments():
    documents = load_documents()
    chunks = chunk_documents(documents)
    results = retrieve("patients request days", chunks, top_k=5, department="records")
    assert len(results) > 0
    for item in results:
        assert item["department"] == "records"


def test_ranking_is_deterministic_and_relevant():
    documents = load_documents()
    chunks = chunk_documents(documents)
    first = retrieve("cancel appointment late cancellation", chunks, top_k=3)
    second = retrieve("cancel appointment late cancellation", chunks, top_k=3)
    assert [c["chunk_index"] for c in first] == [c["chunk_index"] for c in second]
    assert [c["doc_id"] for c in first] == [c["doc_id"] for c in second]
    assert first[0]["department"] == "scheduling"


def test_context_contains_citation_markers():
    documents = load_documents()
    chunks = chunk_documents(documents)
    results = retrieve("refund overpayment billing", chunks, top_k=2)
    context = build_context(results)
    for item in results:
        marker = "[{doc_id}:{section}]".format(
            doc_id=item["doc_id"], section=item["section"]
        )
        assert marker in context


def test_empty_query_returns_safe_result():
    result = answer_query("", top_k=3)
    assert result["results"] == []
    assert result["context"] == ""
