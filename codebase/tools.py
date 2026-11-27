"""Công cụ của bài toán: tra câu luyện do nhóm soạn (spec.md §4)."""
import json
from pathlib import Path

from tracing import tool

BANK = Path(__file__).resolve().parents[1] / "data" / "practice.json"


@tool
def practice_candidates(kc: str) -> list:
    """Tên: practice_candidates.
    Input: kc — mã kiến thức của câu ôn học viên vừa làm sai (str).
    Output: danh sách câu luyện cùng mã kiến thức, mỗi câu {id, question, level, targets}.
            KHÔNG trả lời giải (rubric) — để model không thể lộ lời giải.
    Tác động ra ngoài: không (chỉ đọc data/practice.json)."""
    with BANK.open(encoding="utf-8") as stream:
        return [
            {key: item[key] for key in ("id", "question", "level", "targets")}
            for item in json.load(stream) if item["kc"] == kc
        ]
