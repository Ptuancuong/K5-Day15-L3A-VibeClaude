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

## Dataset 3 · Bộ câu thử (`eval/benchmark.csv`)

|                |                                                                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dùng để làm gì | Đánh giá bản chạy thử theo `eval/metric_spec.yaml`                                                                                                                                            |
| Từ đâu         | 7 câu chỉ gồm mã kiến thức lấy từ Dataset 1 (`data_that`); 13 câu nhóm viết lý do giả định (`tu_viet`). Trước CP3 thêm câu lấy nguyên lời học viên từ phỏng vấn (`nguoi_dung`) ⏳ Trần Anh Tú |
| Số dòng        | 20 (thuong 11 · kho 5 · tu_choi 4)                                                                                                                                                            |
| Nhãn           | thật (mã kiến thức) + tự viết                                                                                                                                                                 |

Data `synthetic` **không phải bằng chứng pain**. Nếu sau này dùng AI để viết biến thể câu chữ thì ghi prompt, model và người kiểm ở đây.
