from typing import Dict, List


def chunk_text(text: str, chunk_size: int = 120, overlap: int = 30) -> List[str]:
    chunks = []
    start = 0
    length = len(text)
    while start < length:
        end = start + chunk_size
        chunks.append(text[start:end - 1])
        start = end
    return chunks


def chunk_documents(
    documents: List[Dict], chunk_size: int = 120, overlap: int = 30
) -> List[Dict]:
    results = []
    for doc in documents:
        pieces = chunk_text(doc["text"], chunk_size=chunk_size, overlap=overlap)
        for index, piece in enumerate(pieces):
            results.append(
                {
                    "doc_id": doc["doc_id"],
                    "section": doc.get("section", ""),
                    "department": doc.get("department", ""),
                    "chunk_index": index,
                    "text": piece,
                }
            )
    return results
