from typing import Dict, Optional

from .chunking import chunk_documents
from .context import build_context
from .documents import load_documents
from .retrieval import retrieve


def answer_query(
    query: str,
    top_k: int = 3,
    department: Optional[str] = None,
) -> Dict:
    documents = load_documents()
    chunks = chunk_documents(documents)
    results = retrieve(query, chunks, top_k=top_k, department=department)
    context = build_context(results)
    return {
        "query": query,
        "results": results,
        "context": context,
    }
