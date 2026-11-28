# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

> Các dòng còn trống: thành viên phụ trách tự điền phần của mình.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | | | | |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code; Codex (PowerShell, CP1) | Viết script đếm trên data BTC (`answers.csv`, `events.csv`); chỉ đưa số tổng hợp vào repo | Hai cách đếm (PowerShell của Codex, Python của Claude) cho cùng 399/1.968 | Phạm Tuấn Cường, Trần Anh Tú |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | Claude | Chấm đề xuất cột `pass`, `ghi_chu` của `run-3` theo `pass_criterion` | ⏳ Đặng Việt Anh kiểm tay 12 câu hỏi đáp, ghi số khớp | Đặng Việt Anh |
| Slide, văn bản | Claude Code, Claude Slides | Soạn nháp `spec.md`, canvas, data card, slide 5 trang | Phạm Tuấn Cường đọc, sửa, chọn hướng; mọi số trong slide trỏ về file trong repo | Phạm Tuấn Cường |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
