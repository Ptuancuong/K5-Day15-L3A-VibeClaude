# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Cùng bộ 26 câu, cùng cách chấm (`eval/metric_spec.yaml`, chuẩn "đạt" ở `spec.md` §7). **Lượt 2 của báo cáo là file `run-3.csv`.**

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-190607` | 22/26 | 85% | 9/9 | 8/12 | 5/5 | **chưa đạt** |
| `run-2` | — | không tính | — | — | — | — | lỗi kỹ thuật HTTP 429 |
| 2 | `run-3@20261127-202217` | 22/26 | 85% | 9/9 | 8/12 | 5/5 | **chưa đạt** |

`run-2` là lượt lỗi kỹ thuật (Gemini API trả HTTP 429), không dùng để so sánh. File vẫn giữ trong repo: `eval/run-2.csv` (run ID `run-2@20261127-201627`, 7/26 câu lỗi) và `traces/run-2.jsonl`.

Theo metric:

| Metric | Ngưỡng | Lượt 1 | Lượt 2 (`run-3`) |
|---|---|---|---|
| `chon_dung_cau_luyen` | ≥90% | 9/9 (100%) đạt | 9/9 (100%) đạt |
| `tra_loi_va_giai_thich` | ≥90% (≥11/12) | 8/12 (67%) **chưa đạt** | 8/12 (67%) **chưa đạt** |
| `tu_choi_dung` | 100% | 5/5 đạt | 5/5 đạt |
| Chỉ số học | ≥3/5 học viên | chưa đo | chưa đo |

So với 22/26 ở lượt 1: **không tăng, không giảm**. Bốn câu trượt vẫn là B03, B07, B09, B10; không câu nào chuyển từ đạt sang trượt hay ngược lại.

Ca sát ngưỡng (B02, B03, B05) được chấm cùng mức với lượt 1. Nếu chấm B03 đúng theo mặt chữ của `pass_criterion` (có ≥4 mục, "không", có con số) thì lượt 2 là 23/26, nhóm hỏi đáp 9/12 (75%), vẫn chưa đạt chuẩn.

Kết quả từng câu: `eval/run-1.csv`, `eval/run-3.csv`. Trace: `traces/run-1.jsonl`, `traces/run-3.jsonl`.

## 2. Lỗi — gom thành nhóm có tên

Cả 4 lỗi nằm ở nhánh A (hỏi đáp, model tự trả lời).

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Lý do thiếu số liệu theo yêu cầu | 2 | B03, B09 |
| Bỏ sót ý bắt buộc | 1 | B10 |
| Không giữ ràng buộc của đề | 1 | B07 |

**Lỗi cụ thể (lượt 2):**

| Câu | Input (tóm tắt) | Output (tóm tắt) | Vì sao sai |
|---|---|---|---|
| B07 | Chọn model cho 3 bài toán: chấm rubric, dịch 1.000 email, viết bài báo sâu | Haiku, Haiku, Claude 3.5 Sonnet | Cần 3 model khác nhau cho 3 bài. Lượt 1 trượt cùng lỗi chọn trùng |
| B09 | Có User, Pain, thiếu Impact và Decision: có nên làm prototype? | "Không đồng ý"; chỉ lý do Impact có số giả định (10 manager × 5 giờ/tuần, 20$/giờ) | Cần ≥3 lý do có số; lý do về chi phí và hướng giải pháp không có số nào |
| B10 | Tính tổng token 3 vòng và giải thích | 2.500 token, liệt kê input 500 / 700 / 850 | Đúng tổng nhưng không nói input vòng sau gồm lịch sử gửi lại, và không nhắc caching. Lượt 1 cũng thiếu caching |
| B03 | Canvas đã có User, Pain, Solution: còn mục nào, thiếu Impact có nên code? | Liệt kê Value Proposition, Data, Model, Evaluation, UX, Cost; "không nên" | Thiếu Decision (so sánh hướng); số $0.05/lần và 100 user × 10 lần chỉ là giả định, không tính ra lợi ích hay chi phí |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: nhánh A (B03, B07, B09, B10). Đây là nhóm **đau nhất với người dùng** vì câu trả lời do model tự viết, học viên có thể học theo một câu trả lời thiếu hoặc sai.
- Đã sửa gì: viết lại `TUTOR_SYSTEM` của nhánh A trong `codebase/agent.py` (commit `bb70ecf`, đẩy lên 28/11 07:48): yêu cầu tách mọi câu hỏi con, gắn mỗi lý do quan trọng với một phép tính hoặc đối chiếu định lượng, chọn phương án khác nhau khi các tình huống có ưu tiên khác nhau, và phân biệt tổng token với chi phí giảm nhờ cache. Token vào của 10 câu B01–B10 tăng từ 2.008 lên 5.568 vì prompt dài hơn.
- Kết quả: nhóm lỗi đó 0/4 → 0/4 · tổng 85% → 85%. Cải tiến chưa có tác dụng trên các câu đang trượt.
- Câu **tệ đi** (đổi đạt → trượt): không có. Điểm cần lưu ý dù vẫn đạt hoặc đã trượt sẵn:
  - B04, B07, B09 mở đầu bằng phần "những gì người học cần nhận", giống chỉ dẫn nội bộ bị lộ ra câu trả lời.
  - B10 thêm câu trong ngoặc khó hiểu về cách cộng.
- Chi phí đo được (cả lượt, 19 lần gọi model): token vào 2.611 → 6.171, token ra 7.031 → 5.216.

## 4. Còn lại

- Lỗi chưa sửa: cả 4 câu trên. Nguy cơ: học viên nhận câu trả lời trông đầy đủ nhưng thiếu ý (B03, B10) hoặc không theo đúng đề (B07) và mang vào lớp.
- Nếu có thêm 1 tuần (đề xuất, chưa thử):
  - Yêu cầu model tách từng ý đề hỏi và tự kiểm đủ trước khi trả lời, không in phần kiểm ra output.
  - Cho nhánh A dựa trên tài liệu bài học thay vì trí nhớ model.
  - Đo trên câu hỏi mới ngoài bộ 26 câu để tránh chỉnh prompt chỉ khớp bộ thử.
