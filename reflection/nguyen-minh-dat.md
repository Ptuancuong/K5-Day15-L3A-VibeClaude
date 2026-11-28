# Reflection — Nguyễn Minh Đạt

## 1. Vai trò và phần mình làm

Mình phụ trách code và chạy đánh giá cho bản demo ôn tập cuối ngày của VibeClaude.
Ở CP2, mình xây luồng mock và định dạng benchmark để kiểm tra chọn câu luyện, tra lời giải và từ chối đầu vào không hợp lệ.
Ở CP3, mình nối Gemini 3.5 Flash-Lite và chạy lượt 1 trên 26 ca. Ở CP4, mình sửa prompt hỏi đáp, giữ lại lượt lỗi HTTP 429 và chạy lại trên cùng bộ câu.
Các phần mình làm nằm ở [luồng xử lý](../codebase/agent.py), [kết nối Gemini](../codebase/ai.py) và [trace lượt chạy lại](../traces/run-3.jsonl). Bản cải tiến được đưa lên ở commit `bb70ecf`.

## 2. AI hỗ trợ mình thế nào

Mình dùng Codex để rà cấu trúc CSV, hỗ trợ tích hợp Gemini, đọc các ca trượt và soạn bản sửa prompt.
Khi thử thật, mình đối chiếu số lần gọi model và token với output của chương trình, rồi chuyển CSV cho Việt Anh chấm theo tiêu chí đã chốt.
Sau lượt 1, mình chỉnh prompt để lời giải trả lời đủ từng ý, gắn phép tính với lý do và phân biệt token xử lý với chi phí khi dùng cache.
Lượt chạy lại vẫn đạt 22/26, bằng lượt 1. Việc prompt dài và cụ thể hơn chưa giúp nhóm tăng số ca đạt.

## 3. Một câu thử trượt và bài học

Ở ca B10, Gemini tính đúng tổng 2.500 token nhưng vẫn trượt. Lượt 1 bỏ sót phần cache, còn lượt chạy lại vẫn thiếu phần cache và chưa giải thích rõ lịch sử được gửi lại trong đầu vào.
Mình rút ra rằng đáp án đúng chỉ là một phần của câu trả lời. Học viên còn cần hiểu vì sao lịch sử được tính vào từng lần gọi và cache có thể ảnh hưởng đến chi phí thế nào.
Nếu cải tiến tiếp, mình sẽ kiểm tra từng gạch đầu dòng trong tiêu chí của câu nhiều ý và thử trên một tình huống mới cùng dạng.
Nguồn đối chiếu: [lượt 1](../eval/run-1.csv), [lượt chạy lại](../eval/run-3.csv) và [báo cáo đánh giá](../eval/report.md).
