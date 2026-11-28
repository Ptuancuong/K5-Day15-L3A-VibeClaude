# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu, 1 lượt hỏi / phiên. Nguồn: data BTC `answers.csv`, 77 học viên làm ôn cuối ngày (05–24/11/2026), cách đếm ở `evidence/data-mining.md`.

  | Persona | Tỉ lệ | Số phiên / người / tháng | Căn cứ |
  |---|---|---|---|
  | `dung_it` | 0,40 (31/77) | 1,5 | sai ≤2 câu / 20 ngày, trung bình 0,97 câu |
  | `dung_vua` | 0,34 (26/77) | 6,2 | sai 3–6 câu, trung bình 4,12 câu |
  | `dung_nhieu` | 0,26 (20/77) | 19,6 | sai ≥7 câu, trung bình 13,1 câu |

  Mỗi câu sai = 1 phiên, nhân 30/20 để ra tháng. Số lượt hỏi / phiên = 1 là *(tự ước tính)*: bản chạy thử chỉ làm lát cắt một câu (`spec.md` §4).
- **Số người dùng thật** 3 kịch bản: thấp **77** · cơ sở **124** · cao **700**. Nguồn: data BTC chỉ 77/436 học viên có làm phần ôn; lớp L3 hơn 700 học viên (README hackathon). Thấp = đúng số người đang làm ôn. Cơ sở = 77/436 × 700 ≈ 124 *(tự ước tính: giữ tỉ lệ người làm ôn, áp lên lớp L3)*. Cao = 700, mọi học viên L3 dùng *(tự ước tính)*.
- **Giá** (bảng giá K5, `further-reading/model-prices.md` của repo đề; https://ai.google.dev/gemini-api/docs/pricing, xem 25/11/2026): `gemini-3.5-flash-lite` vào 0,30 · ra 2,50 USD / 1M token · `gemini-4-hydrogen` vào 1,50 · ra 7,50 USD / 1M token.
- **Tỉ lệ đạt** dùng để tính: **22/26 (85%)** — lượt `run-3` (lượt 2), run ID `run-3@20261127-202217`, đã chấm. Chưa đạt chuẩn "đạt" ở `spec.md` §7 (nhánh hỏi đáp 8/12, cần ≥11/12). **Chỉ số học (≥3/5 học viên trả lời đúng câu luyện ở lần đầu): chưa đo.**
- Đo token trên model `gemini-3.5-flash-lite`, tính giá model `gemini-3.5-flash-lite` và `gemini-4-hydrogen`.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-083947` · 50 phiên (0 phiên lỗi) · seed 42 · bản tóm tắt: `cost/simulate-1-summary.md`

Trong 50 phiên có 9 phiên không gọi model (câu từ chối và tra lời giải chạy bằng code, token bằng 0). Trung bình mỗi phiên: 251 token vào, 214 token ra.

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (77 người) | / tháng — cơ sở (124 người) | / tháng — cao (700 người) | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| gemini-3.5-flash-lite (vào 0,3 · ra 2,5 $/1M) | $0,00061 | **$0,00072** | $0,37 | $0,59 | $3,36 | $0,0048 |
| gemini-4-hydrogen (vào 1,5 · ra 7,5 $/1M) | $0,0020 | **$0,0023** | $1,20 | $1,93 | $10,91 | $0,0156 |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

Dòng `gemini-4-hydrogen` dùng số token đo trên `gemini-3.5-flash-lite`, chỉ đổi giá. Model khác có bộ tách token khác, số token thật có thể lệch.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): ≈ **127 phút** học viên / tháng (~9.800 phút trên 77 học viên làm ôn). Đây là thời gian học viên đang bỏ ra, không phải thời gian chắc chắn tiết kiệm được.
- Chi phí / người / tháng (cơ sở, model `gemini-3.5-flash-lite`): **$0,0048** (model `gemini-4-hydrogen`: $0,0156).
- **Kết luận một dòng — đáng làm không:** về chi phí model thì đáng: cả lớp L3 dùng (700 người) tốn $3,36 / tháng ở model nhỏ, $10,91 ở model lớn; chi phí không phải rào cản. Điều chưa đạt là chất lượng (85%, chưa đủ chuẩn "đạt") và chỉ số học chưa đo.

## 4. Giới hạn của số này

- Chi phí ngoài model chưa tính: hosting, lưu trữ, giờ công người chấm cho metric `tra_loi_va_giai_thich` (metric này quy định người chấm).
- Persona lấy từ 77 học viên đang làm ôn. Học viên chưa làm ôn lần nào có dùng công cụ hay không thì data không cho biết, nên kịch bản cơ sở và cao là *(tự ước tính)*.
- Mô hình mạnh hơn (`gemini-4-hydrogen`) đắt khoảng 3,2 lần mỗi task thành công. Chưa đo xem nó có nâng được tỉ lệ đạt hay không.
- Token đo bằng `codebase/agent.py` bản đẩy lúc 07:48 ngày 28/11; `run-3` chạy lúc 20:22 ngày 27/11. Chưa xác nhận prompt của hai lần trùng nhau (`eval/report.md` mục 3).
