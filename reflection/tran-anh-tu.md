# Reflection — Trần Anh Tú

1. Vai trò + phần mình làm (trỏ tới file / commit):
   Mình phụ trách phần bằng chứng và phần chi phí.
   - Bằng chứng: kiểm lại số trên log preclass của BTC ở `evidence/data-mining.md` (399/1.968 lượt trả lời lần đầu sai, 69/77 học viên có ≥1 câu sai); làm khảo sát 20 học viên ngoài nhóm ở `evidence/survey/`, `evidence/summary.md`, `evidence/hypothesis.md` và Dataset 4 trong `data/DATA_CARD.md` (commit `b1b7d16`, `5c374e1`).
   - Chi phí: `cost/personas.yaml`, `cost/cost-estimate.md` và lượt chạy `cost/simulate-1.csv` (50 phiên, model `gemini-3.5-flash-lite`, commit `ba76293`).

2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):
   Mình dùng Claude Code để dựng form bằng Google Apps Script, viết đoạn PowerShell đếm log, nháp các file trong `evidence/`, viết persona và chạy `simulate`.
   Chỗ phải sửa lại output của AI: AI từng tự thêm 4 câu thử B22–B25 và sửa `spec.md` mà chưa kiểm `main`, nên trùng id và trùng việc của Việt Anh; mình bỏ phần đó. AI cũng từng nói PR đang chờ duyệt trong khi PR đã merge; mình nhắc và AI kiểm lại trên GitHub.
   Số trong `summary.md` được đối chiếu lại với `results.csv` và `answers.csv`; các trích dẫn chép nguyên văn từ phiếu khảo sát, không viết lại.

3. Một câu thử trượt của nhóm và mình học được gì từ nó:
   B07 (chọn model cho 3 bài toán: chấm rubric, dịch 1.000 email, viết bài sâu). Đề cần 3 model khác nhau nhưng bản chạy thử chọn Haiku, Haiku rồi Claude 3.5 Sonnet, trượt cả lượt 1 và lượt 2 (`eval/report.md`).
   Mình học được hai điều. Một, đổi prompt giữa hai lượt không làm 4 câu trượt đổi kết quả (22/26 vẫn là 22/26), nên phải sửa theo nhóm lỗi chứ không chỉ chạy lại. Hai, một cải tiến phải được ghi lại để tái lập: báo cáo ghi chưa tái lập được lượt 2 từ repo, mà tỉ lệ đạt đó cũng là số mình dùng để tính chi phí.
