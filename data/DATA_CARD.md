# Data card — dữ liệu bản chạy thử dùng

> Bản đầu CP2, đủ ở CP3. Ô **⏳** chờ người phụ trách điền.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Nhật ký pre-class (data BTC cấp) — chỉ để đào bằng chứng

|                      |                                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Dùng để làm gì       | Đào bằng chứng pain (`evidence/data-mining.md`), chọn 7 mã kiến thức cho ngân hàng câu luyện, số lần / tháng cho persona. **Không** dùng làm nguồn cho công cụ, không đưa vào model                          |
| Từ đâu               | `data/preclass/` trong repo đề BTC phát: `answers.csv` (3.776 dòng), `events.csv` (107.709 dòng), `column_dictionary.csv`                                                                                    |
| Xử lý những bước gì  | Lọc `answers.csv`: `nguon = pre_post_post`, `lan_thu = 1`, `was_correct ∈ {True, False}` → 1.968 dòng; đếm lượt sai theo `kc_code`. Chỉ giữ số đếm tổng hợp. Không ghép mã học viên với bất kỳ thông tin nào |
| Số dòng              | 1.968 lượt trả lời lần đầu ở ôn cuối ngày, 77 học viên, 05–24/11/2026                                                                                                                                        |
| Phiên bản / ngày lấy | Bản trong repo đề, lấy 27/11/2026. Kiểm đúng bản: `answers.csv` có 3.776 dòng dữ liệu                                                                                                                        |
| Nhãn                 | thật (đã ẩn danh bởi BTC)                                                                                                                                                                                    |
| Giới hạn             | Không có nguyên văn câu hỏi, câu trả lời hay lý do học viên chọn, chỉ có mã. Chỉ 77/436 học viên có hoạt động làm phần ôn → không suy ra cho cả khoá. Không cho biết _vì sao_ học viên không làm lại         |
| Cách giữ             | Mỗi người tự giữ bản local ngoài repo; `.gitignore` chặn `data/preclass/`, `data/training-ops/`, `data-btc/`                                                                                                 |

## Dataset 2 · Ngân hàng câu luyện (`data/practice.json`) — nhóm tự viết

|                  |                                                                                                                                                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dùng để làm gì   | Nguồn duy nhất của công cụ `practice_candidates(kc)`; đề câu luyện hiện cho học viên lấy nguyên văn từ file này                                                                                            |
| Từ đâu           | Nhóm tự viết theo 7 mã kiến thức có nhiều lượt sai nhất trong Dataset 1 (6/7 mã thuộc top 6; tổng 77/399 lượt sai). Không chép câu hỏi của khoá                                                            |
| Trường           | `id, kc, topic, level (co_ban · van_dung), question, rubric, targets` — `targets` là hiểu nhầm câu đó nhắm tới; `rubric` là lời giải, **không bao giờ** được gửi cho model hay hiện trước khi học viên làm |
| Số dòng          | 14 câu (7 mã kiến thức × 2 câu)                                                                                                                                                                            |
| Phiên bản / ngày | 27/11/2026 — `question`, `rubric`: Nguyễn Minh Đạt; `targets`: bản nháp do đội trưởng thêm ⏳ Đặng Việt Anh kiểm                                                                                           |
| Nhãn             | `synthetic` (người viết tay, không sinh bằng script hay prompt)                                                                                                                                            |
| Người kiểm       | ⏳ người thứ hai kiểm `rubric` và `targets`; ghi số câu đã kiểm tay                                                                                                                                        |

## Dataset 2b · Câu ôn cuối ngày (`data/review_questions.json`) — nhóm tự viết

|                  |                                                                                                                                                                                                                                                                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dùng để làm gì   | Nguồn cho công cụ `get_review_question(review_id)`: đề câu ôn học viên vừa sai, làm ngữ cảnh cho AI khi chọn câu luyện                                                                                                                                                                                                                    |
| Từ đâu           | Đặng Việt Anh viết 10 câu hỏi ôn (ban đầu soạn làm câu thử hỏi đáp), mỗi câu gắn một `kc_code` có thật trong Dataset 1 (R01–R06: 6 mã có câu luyện; R07–R10: `model_tier_selection`, `select_rule_workflow_agent_level`, `complete_ai_problem_statement`, `token_generation_loop_count` — xếp hạng 7–10 theo lượt sai, chưa có câu luyện) |
| Trường           | `id, kc, question, reference_answer, author` — `reference_answer` không gửi cho model                                                                                                                                                                                                                                                     |
| Số dòng          | 10                                                                                                                                                                                                                                                                                                                                        |
| Phiên bản / ngày | 27/11/2026                                                                                                                                                                                                                                                                                                                                |
| Nhãn             | `synthetic` (người viết tay, không chép câu hỏi của khoá)                                                                                                                                                                                                                                                                                 |

## Dataset 3 · Bộ câu thử (`eval/benchmark.csv`)

|                |                                                                                                                                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dùng để làm gì | Đánh giá bản chạy thử theo `eval/metric_spec.yaml`                                                                                                                                                                        |
| Từ đâu         | 8 câu chỉ gồm mã kiến thức lấy từ Dataset 1 (`data_that`); 16 câu nhóm viết lý do giả định hoặc dùng câu ôn Dataset 2b (`tu_viet`). Trước CP3 thêm câu lấy nguyên lời học viên từ phỏng vấn (`nguoi_dung`) ⏳ Trần Anh Tú |
| Số dòng        | 24 (thuong 12 · kho 8 · tu_choi 4)                                                                                                                                                                                        |
| Nhãn           | thật (mã kiến thức) + tự viết                                                                                                                                                                                             |

## Dataset 4 · Khảo sát học viên (Google Form) — chỉ để đào bằng chứng

|                      |                                                                                                                                                                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dùng để làm gì       | Bằng chứng pain: học viên làm gì sau khi trả lời sai, có chắc đã hiểu không (`evidence/summary.md`). Không dùng làm nguồn cho công cụ                                                                                                                              |
| Từ đâu               | Nhóm tự khảo sát bằng Google Form, đăng ở kênh Discord `#chung` của cohort lúc 17:15 ngày 27/11/2026; thu phiếu đến 17:54                                                                                                                                       |
| Xử lý những bước gì  | Loại 1 phiếu của thành viên nhóm; bỏ cột dấu thời gian và cột liên hệ; đánh số lại 1–20 (`evidence/survey/results.csv`)                                                                                                                                            |
| Số dòng              | 20 phiếu hợp lệ (21 phiếu thu được)                                                                                                                                                                                                                              |
| Phiên bản / ngày lấy | Xuất CSV ngày 27/11/2026. Bộ câu hỏi đã dùng: `evidence/survey/questions.md`                                                                                                                                                                                     |
| Nhãn                 | thật (ẩn danh)                                                                                                                                                                                                                                                   |
| Giới hạn             | Mẫu nhỏ (n = 20), thu ở kênh chung của cohort nên có thể lệch về người chủ động điền; form không có câu hỏi vai nên chưa kiểm được "đúng người dùng"; câu 8 đổi nội dung giữa lúc thu (9 phiếu bản cũ, 11 phiếu bản mới) nên không dùng làm số chính                  |

Data `synthetic` **không phải bằng chứng pain**. Nếu sau này dùng AI để viết biến thể câu chữ thì ghi prompt, model và người kiểm ở đây.
