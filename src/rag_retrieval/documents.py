import json
import os
from typing import Dict, List

_DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "data",
    "policy_docs.json",
)


def load_documents(path: str = _DATA_PATH) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    return data["documents"]


def document_departments(documents: List[Dict]) -> List[str]:
    seen = []
    for doc in documents:
        dept = doc.get("department")
        if dept and dept not in seen:
            seen.append(dept)
    return seen
