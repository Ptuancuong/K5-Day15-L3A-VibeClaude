# Hồ sơ đánh giá — một trang

## 1. Dataset → xử lý

Chi tiết ở `data/DATA_CARD.md`. Nhật ký pre-class của BTC (1.968 lượt trả lời lần đầu ở ôn cuối ngày) chỉ dùng để đào bằng chứng và chọn 7 mã kiến thức, không đưa vào model. Công cụ dùng ngân hàng 14 câu luyện nhóm tự viết (`data/practice.json`, nhãn `synthetic`).

## 2. Bộ câu thử dựng ra sao

- `eval/benchmark.csv`: 26 câu (thuong 9 · kho 12 · tu_choi 5, trong đó 2 câu tấn công: B19, B21)
- Nguồn (`python run.py check`): nguoi_dung 3 · data_that 7 · tu_viet 16 · sinh_seed 0 → từ người dùng / data thật 10/26 (đạt mức ≥1/3)
- Độ phủ: 3 nhánh (hỏi đáp · chọn câu luyện · tra lời giải) cùng các ca từ chối; bảng kịch bản ở `spec.md` §5
- Câu `kho` theo 4 lớp chỗ khó (`spec.md` §5): lớp 1: B07, B10 · lớp 2: B01–B06, B09 · lớp 3: B20 · lớp 4: B08, B24

## 3. Metric và cách chấm

| Metric (`eval/metric_spec.yaml`) | Cách chấm | Ngưỡng |
|---|---|---|
| `chon_dung_cau_luyen` | code | ≥90% ca (9/9) |
| `tra_loi_va_giai_thich` | người | ≥90% ca (tối thiểu 11/12) |
| `tu_choi_dung` | code | 100% ca (5/5) |

- **Người thứ hai chấm thử:** ⏳ chưa làm (cần khớp ≥4/5)
- **Chấm lượt `run-3`:** cột `pass` và `ghi_chu` do Claude (AI) chấm đề xuất theo `pass_criterion`. Metric `tra_loi_va_giai_thich` quy định người chấm, nên ⏳ cần người kiểm lại: đã kiểm tay __/12 câu, khớp __.
- **Chuẩn "đạt"** (chép từ `spec.md` §7, chốt trước 19:30 Thứ Sáu 27/11): "Đạt khi ≥ 90% ca chọn câu luyện qua (bộ CP2: 7/7), và ≥ 90% ca hỏi đáp và tra lời giải qua (bộ CP2: 10/11), và 100% ca từ chối qua (bộ CP2: 3/3); chỉ số học: ≥ 3/5 học viên dùng thử trả lời đúng câu luyện ở lần đầu."
  - Trên bộ 26 câu, giữ nguyên tỉ lệ: chọn câu luyện 9 · hỏi đáp và tra lời giải 12 · từ chối 5.

## 4. Lệnh

`python run.py eval` → `eval/run-N.csv` + `traces/run-N.jsonl` · điền cột `pass` · `python run.py score eval/run-N.csv`

## 5. Đã chạy gì

| Lượt | Run ID | Model | Cấu hình (prompt / công cụ / thay đổi) | Đạt / tổng | % | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-190607` | `gemini-3.5-flash-lite` | Bản đầu CP3 | 22/26 | 85% | chưa |
| `run-2` | — | — | Lượt lỗi kỹ thuật: HTTP 429. Không chấm, không so sánh; file không có trong repo | — | — | — |
| 2 (`run-3`) | `run-3@20261127-202217` | `gemini-3.5-flash-lite` | Chạy lại; ⏳ ghi thay đổi prompt nhánh A (chưa commit) | 22/26 | 85% | chưa |

Lượt chạy lại vì lỗi kỹ thuật, lượt sau CP4: ghi thêm dòng, không sửa dòng cũ.

## 6. Lỗi chính

Nhóm lỗi lớn nhất là nhánh hỏi đáp: 8/12 ở cả hai lượt, dưới ngưỡng 11/12. B03, B09 thiếu lý do có số, B07 chọn trùng model, B10 bỏ sót ý về lịch sử và caching. Chọn câu luyện (9/9) và từ chối (5/5) đạt. Cả 4 lỗi còn nguyên sau lượt 2. Chi tiết: `eval/report.md`.
