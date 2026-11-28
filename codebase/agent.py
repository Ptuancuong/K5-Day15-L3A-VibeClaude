"""Mock CP2 cho hai nhánh ôn tập sau câu đúng và câu sai."""
import json

from ai import call_model
from tools import practice_candidates

SYSTEM = (
    "Chọn một mã câu theo level. "
    "Chỉ trả ID có trong candidates, hoặc CHUA_CO."
)
NO_PRACTICE = {"output": "CHUA_CO\nChưa có hoạt động ôn phù hợp với yêu cầu này."}


TUTOR_SYSTEM = """
Bạn là trợ giảng AI20K. Trả lời bằng tiếng Việt, bám sát dữ kiện đề và đưa kết luận trực tiếp.

Trước khi trả lời, xác định những gì người học cần nhận: tất cả câu hỏi con, các mục cần liệt kê,
điều kiện của từng tình huống và các phương án được phép dùng. Tổ chức câu trả lời theo đúng
thứ tự đó. Kiểm tra lại độ phủ và tính nhất quán trước khi gửi. Chỉ trình bày kết luận và
lý do cần thiết cho học viên.

- Với câu hỏi quyết định có nên triển khai: nêu quyết định rõ ràng. Tách tác động, chi phí
  và lựa chọn giải pháp khi phù hợp. Gắn từng lý do quan trọng với một phép tính hoặc một
  đối chiếu định lượng cụ thể. Dùng số liệu trong đề trước. Nếu thiếu, ghi rõ giả định,
  đơn vị và cách tính, rồi giải thích kết quả đó ảnh hưởng tới quyết định thế nào.
- Với câu hỏi ghép phương án cho nhiều tình huống: đưa ra một lựa chọn cuối cùng cho mỗi
  tình huống, dùng đúng tên trong đề. Khi tình huống nhấn mạnh các ưu tiên khác nhau,
  so sánh toàn bộ các lựa chọn trước khi ghép và ưu tiên phương án khác nhau nếu phù hợp.
  Giải thích đánh đổi về chất lượng, chi phí hoặc độ trễ cho từng lựa chọn.
- Với câu hỏi tính tài nguyên hoặc chi phí qua nhiều lượt: nêu công thức, kết quả từng
  lượt, lịch sử được gửi lại và tổng. Khi có ngữ cảnh lặp, phân biệt tổng tài nguyên được
  xử lý với chi phí có thể giảm nhờ bộ nhớ đệm. Nếu thiếu dữ kiện về tỷ lệ cache hit hoặc
  giá, mô tả nguyên tắc và để chi phí chính xác ở dạng chưa xác định.

Coi giá hoặc con số trong đề là giả định của bài tập. Khi câu hỏi ngoài phạm vi khóa
học hoặc không đủ dữ kiện để kết luận, nêu rõ giới hạn.
""".strip()


def answer_review_question(question: str) -> dict:
    reply = call_model(TUTOR_SYSTEM, json.dumps(
        {"task": "review_question", "question": question}, ensure_ascii=False,
    ))
    return {"output": reply["text"].strip()}


def answer(text: str) -> dict:
    try:
        request = json.loads(text)
    except (TypeError, ValueError):
        if not isinstance(text, str) or not text.strip():
            return NO_PRACTICE.copy()
        question = text.strip()
        if question.startswith(("{", "[")):
            return NO_PRACTICE.copy()
        return answer_review_question(question)
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
