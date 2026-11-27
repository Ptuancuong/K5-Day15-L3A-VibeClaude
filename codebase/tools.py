"""Tra câu luyện do nhóm soạn."""
import json
from pathlib import Path

from tracing import tool

BANK = Path(__file__).resolve().parents[1] / "data" / "practice.json"


@tool
def practice_candidates(kc: str) -> list:
    """Tra theo mã kiến thức. Trả danh sách câu ứng viên. Chỉ đọc file local."""
    with BANK.open(encoding="utf-8") as stream:
        return [
            {key: item[key] for key in ("id", "question", "level", "rubric")}
            for item in json.load(stream) if item["kc"] == kc
        ]
