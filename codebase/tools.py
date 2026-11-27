"""Công cụ của bài toán: tra câu luyện do nhóm soạn (spec.md §4)."""
import json
from pathlib import Path

from tracing import tool

BANK = Path(__file__).resolve().parents[1] / "data" / "practice.json"
REVIEW = Path(__file__).resolve().parents[1] / "data" / "review_questions.json"


@tool
def get_review_question(review_id: str) -> dict:
    """Tên: get_review_question.
    Input: review_id — mã câu ôn cuối ngày học viên vừa làm sai, vd "R01" (str).
    Output: {id, kc, question} của câu ôn; {} nếu không có. kc rỗng = chưa có câu luyện cho câu này.
            Không trả đáp án tham khảo (reference_answer).
    Tác động ra ngoài: không (chỉ đọc data/review_questions.json)."""
    with REVIEW.open(encoding="utf-8") as stream:
        for item in json.load(stream):
            if item["id"] == review_id:
                return {key: item[key] for key in ("id", "kc", "question")}
    return {}


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
