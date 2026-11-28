# Tóm tắt mô phỏng simulate-1@20261128-083947

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 25 | 1 | 254 | 215 | 0.8 | 0.6 |
| dung_vua | 15 | 1 | 239 | 210 | 0.7 | 0.6 |
| dung_nhieu | 10 | 1 | 262 | 217 | 1.0 | 0.6 |

Tỉ lệ đạt dùng để tính: 22/26 (85%) — lượt run-3@20261127-202217

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-3.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (77 người) | Chi phí / tháng — cơ sở (124 người) | Chi phí / tháng — cao (700 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.5-flash-lite (vào 0.3 · ra 2.5 $/1M) | $0.00061 | $0.00072 | $0.00072 | $0.3692 | $0.5945 | $3.36 | $0.0048 |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0020 | $0.0023 | $0.0023 | $1.20 | $1.93 | $10.91 | $0.0156 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.5-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
