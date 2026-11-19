from typing import Dict, List


def format_citation(chunk: Dict) -> str:
    return "{doc_id}:{section}".format(
        doc_id=chunk.get("doc_id", ""),
        section=chunk.get("section", ""),
    )


def build_context(chunks: List[Dict]) -> str:
    lines = []
    for chunk in chunks:
        lines.append(chunk["text"])
    return "\n\n".join(lines)
