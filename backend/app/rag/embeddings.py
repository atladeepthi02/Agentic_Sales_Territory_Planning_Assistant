from __future__ import annotations

import hashlib
from typing import List


def deterministic_embedding(text: str, dims: int = 768) -> List[float]:
    vector = []
    for i in range(dims):
        value = hashlib.sha256(f"{text}:{i}".encode("utf-8")).hexdigest()
        numeric = int(value, 16) / 16 ** len(value)
        vector.append(float(numeric))
    return vector
