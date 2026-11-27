"""Mock CP2 cho hai nhánh ôn tập sau câu đúng và câu sai."""
import json

from ai import call_model
from tools import practice_candidates

SYSTEM = (
    "Chọn một mã câu theo level. "
    "Chỉ trả ID có trong candidates, hoặc CHUA_CO."
)
NO_PRACTICE = {"output": "CHUA_CO\nChưa có hoạt động ôn phù hợp với yêu cầu này."}


def answer(text: str) -> dict:
    try:
        request = json.loads(text)
    except (TypeError, ValueError):
        return NO_PRACTICE.copy()
    if not isinstance(request, dict) or request.keys() - {"kc", "level", "result", "action", "practice_id"}:
        return NO_PRACTICE.copy()
    kc = request.get("kc")
    result = request.get("result", "sai")
    action = request.get("action", "luyen")
    if not isinstance(kc, str) or not kc.strip() or result not in ("dung", "sai"):
        return NO_PRACTICE.copy()
    if action not in ("luyen", "giai_thich"):
        return NO_PRACTICE.copy()

    if action == "giai_thich":
        practice_id = request.get("practice_id")
        if result != "dung" or "level" in request or not isinstance(practice_id, str) or not practice_id.strip():
            return NO_PRACTICE.copy()
        for item in practice_candidates(kc):
            if item["id"] == practice_id:
                return {"output": f"GIAI_THICH {practice_id}\nGiải thích mẫu: {item['rubric']}"}
        return NO_PRACTICE.copy()

    level = request.get("level", "van_dung" if result == "dung" else "co_ban")
    if "practice_id" in request or level not in ("co_ban", "van_dung"):
        return NO_PRACTICE.copy()
    candidates = [item for item in practice_candidates(kc) if item["level"] == level]
    if not candidates:
        return NO_PRACTICE.copy()
    shortlist = [{key: item[key] for key in ("id", "question", "level")} for item in candidates]
    reply = call_model(SYSTEM, json.dumps({"level": level, "candidates": shortlist}, ensure_ascii=False))
    chosen = reply["text"].strip()
    for item in candidates:
        if item["id"] == chosen:
            prompt = "Giải thích lý do bằng một câu."
            if result == "dung":
                prompt += f" Bạn có thể yêu cầu giải thích mẫu với mã {chosen}."
            return {"output": f"{chosen}\n{item['question']}\n{prompt}"}
    return NO_PRACTICE.copy()
