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

|                  |                                                                                                                                                                             |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dùng để làm gì   | Nguồn duy nhất của công cụ `practice_candidates(kc)` (nhánh B, C); đề câu luyện và lời giải mẫu lấy nguyên văn từ file này                                                  |
| Từ đâu           | Nhóm tự viết theo 7 mã kiến thức có nhiều lượt sai nhất trong Dataset 1 (6/7 mã thuộc top 6; tổng 77/399 lượt sai). Không chép câu hỏi của khoá                             |
| Trường           | `id, kc, topic, level (co_ban · van_dung), question, rubric` — `rubric` là lời giải mẫu: không gửi cho model; chỉ hiện ở nhánh C khi học viên đã trả lời đúng và tự yêu cầu |
| Số dòng          | 14 câu (7 mã kiến thức × 2 mức)                                                                                                                                             |
| Phiên bản / ngày | 27/11/2026 — Nguyễn Minh Đạt                                                                                                                                                |
| Nhãn             | `synthetic` (người viết tay, không sinh bằng script hay prompt)                                                                                                             |
| Người kiểm       | ⏳ Đặng Việt Anh kiểm `question` và `rubric`; ghi số câu đã kiểm tay                                                                                                        |

## Dataset 3 · Bộ câu thử (`eval/benchmark.csv`)

|                |                                                                                                                                                                                                                                                                                                                            |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dùng để làm gì | Đánh giá bản chạy thử theo `eval/metric_spec.yaml`                                                                                                                                                                                                                                                                         |
| Từ đâu         | B01–B10: 10 câu hỏi ôn Đặng Việt Anh viết, kèm đáp án tham khảo (`tu_viet`); B11–B17: 7 câu chỉ gồm mã kiến thức lấy từ Dataset 1 (`data_that`); B18–B21: câu từ chối, tấn công, tra lời giải (`tu_viet`); B22–B26: B22, B24, B25 dựng theo lời học viên trong phiếu khảo sát (`nguoi_dung`), B23, B26 tự viết (`tu_viet`) |
| Số dòng        | 26 (thuong 9 · kho 12 · tu_choi 5) — B22–B26 thêm 27/11 18:59; 3 câu `nguoi_dung` lấy từ phiếu khảo sát KS10, KS17, KS18/KS20 (Dataset 4)                                                                                                                                                                                  |
| Nhãn           | thật (mã kiến thức) + tự viết                                                                                                                                                                                                                                                                                              |

## Dataset 4 · Khảo sát học viên (Google Form) — chỉ để đào bằng chứng

|                      |                                                                                                                                                                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dùng để làm gì       | Bằng chứng pain: học viên làm gì sau khi trả lời sai, có chắc đã hiểu không (`evidence/summary.md`). Không dùng làm nguồn cho công cụ                                                                                                                |
| Từ đâu               | Nhóm tự khảo sát bằng Google Form, đăng ở kênh Discord `#chung` của cohort lúc 17:15 ngày 27/11/2026; thu phiếu đến 17:54                                                                                                                            |
| Xử lý những bước gì  | Loại 1 phiếu của thành viên nhóm; bỏ cột dấu thời gian và cột liên hệ; đánh số lại 1–20 (`evidence/survey/results.csv`)                                                                                                                              |
| Số dòng              | 20 phiếu hợp lệ (21 phiếu thu được)                                                                                                                                                                                                                  |
| Phiên bản / ngày lấy | Xuất CSV ngày 27/11/2026. Bộ câu hỏi đã dùng: `evidence/survey/questions.md`                                                                                                                                                                         |
| Nhãn                 | thật (ẩn danh)                                                                                                                                                                                                                                       |
| Giới hạn             | Mẫu nhỏ (n = 20), thu ở kênh chung của cohort nên có thể lệch về người chủ động điền; form không có câu hỏi vai nên chưa kiểm được "đúng người dùng"; câu 8 đổi nội dung giữa lúc thu (9 phiếu bản cũ, 11 phiếu bản mới) nên không dùng làm số chính |

Data `synthetic` **không phải bằng chứng pain**. Nếu sau này dùng AI để viết biến thể câu chữ thì ghi prompt, model và người kiểm ở đây.
