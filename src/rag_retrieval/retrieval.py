import re
from typing import Dict, List, Optional


def tokenize(text: str) -> List[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def score_chunk(query_tokens: List[str], chunk_text: str) -> float:
    chunk_tokens = tokenize(chunk_text)
    if not chunk_tokens:
        return 0.0
    chunk_set = set(chunk_tokens)
    overlap = 0
    for token in query_tokens:
        if token in chunk_set:
            overlap += 1
    return float(overlap)


def retrieve(
    query: str,
    chunks: List[Dict],
    top_k: int = 3,
    department: Optional[str] = None,
) -> List[Dict]:
    query_tokens = tokenize(query)
    scored = []
    for chunk in chunks:
        score = score_chunk(query_tokens, chunk["text"])
        scored.append({**chunk, "score": score})
    scored = [item for item in scored if item["score"] > 0]
    scored.sort(key=lambda item: item["score"], reverse=True)
    return scored[:top_k]
