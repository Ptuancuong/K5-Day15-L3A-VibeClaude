# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Câu luyện theo mã kiến thức

| | |
|---|---|
| Dùng để làm gì | Bộ câu luyện khi học viên trả lời sai phần ôn tập cuối ngày. Nguồn cho công cụ `search_lesson()` chọn câu có mã kiến thức khớp. |
| Từ đâu | Log BTC: `answers.csv` (giữ local, không commit). Phân tích: 10 mã kiến thức phổ biến nhất từ 399 câu sai lần đầu ở `pre_post_post`. Nhóm tự soạn tình huống mới cho mỗi mã (không copy câu gốc). |
| Xử lý những bước gì | Lọc: `nguon='pre_post_post' AND lan_thu=1 AND was_correct=False`. Chọn 10 mã `kc_code` phổ biến nhất. Soạn 1 câu hỏi mới + đáp án chuẩn cho mỗi mã (không lặp câu gốc). |
| Số dòng | 10 câu luyện (B01–B10) |
| Phiên bản / ngày lấy | Log BTC ngày 2026-11-27. Câu luyện soạn 2026-11-27. |
| Nhãn | `synthetic` (soạn theo mã kiến thức, không copy nguyên văn) |
| Giới hạn | CP2: 10 câu cơ bản (mỗi mã 1 câu). CP3 mở rộng: thêm câu khó, test case edge case, test case sai (mã sai, thiếu info, v.v.). |

**Cách soạn:** Mỗi câu luyện B01–B10 có:

- **Input**: Tình huống thực tế, câu hỏi rõ (không copy từ log)
- **Expected**: Đáp án chuẩn có giải thích + ví dụ cụ thể
- **Pass Criterion**: Cách nhận biết "đạt" (ghi rõ điều kiện)
- **Source**: tự viết

**10 mã kiến thức:** `chatbot_is_app_around_model`, `agentic_fit_scoring_decision`, `ai_product_canvas`, `cot_task_fit`, `system_prompt_contract`, `react_reasoning_acting_pattern`, `model_tier_selection`, `select_rule_workflow_agent_level`, `complete_ai_problem_statement`, `token_generation_loop_count`
