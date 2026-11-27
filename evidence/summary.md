# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn                                               | Đạt ngưỡng?                  | File                         |
| --------------------------------------------------- | ---------------------------- | ---------------------------- |
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☐ đã chạy lại, có x/N, %, cách đếm; ví dụ mới là 6 mã kiến thức, chưa có ví dụ từng dòng | `evidence/data-mining.md`    |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng)    | Không thực hiện              | —                            |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng)    | ☑ n = 20 (xem lưu ý ở mục 4) | `evidence/survey/`           |

## 2. Số chính

- Đào data: log preclass 399/1.968 lượt trả lời lần đầu bị sai (20,3%), đã chạy lại trên `answers.csv` gốc ngày 27/11/2026, khớp số (69/77 học viên có ≥1 câu sai; cách đếm và phân bố ở `evidence/data-mining.md`).
- Phỏng vấn: không thực hiện.
- Khảo sát: n = 20 người ngoài nhóm (21 phiếu, đã loại 1 phiếu của thành viên nhóm) ·
  - 17/20 (85%) từng trả lời sai khi dùng preclass-online hoặc phần mềm ôn tập khác (rất hay 5, thỉnh thoảng 9, hiếm khi 3; chưa bao giờ 3).
  - 18/20 (90%) sau khi xem lời giải **không hoàn toàn chắc** mình đã hiểu (hơi chắc 12, không chắc 4, biết là chưa hiểu 2; chỉ 2/20 chắc đã hiểu).
  - 5/20 (25%) tự tìm thêm câu tương tự để làm; 14/20 (70%) hỏi ChatGPT hoặc AI riêng (câu hỏi chọn nhiều).
  - 10/20 mất từ 15 phút trở lên để xử lý câu sai (15–30 phút: 7, trên 30 phút: 3).
  - Nguồn: `evidence/survey/results.csv` (đã ẩn danh).

Nhóm không thực hiện phỏng vấn (chỉ làm khảo sát), nên không có bảng P1–P3.

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "Hoàn thành nhưng lại không hoàn toàn hiểu những gì đã làm" — phiếu khảo sát 7
2. "Nhiều khi AI hay tự biên tự diễn, bánh vẽ khiến bài bị đi lệch với yêu cầu đề bài" — phiếu khảo sát 1
3. "Không hiểu phần giải thích của snoop" — phiếu khảo sát 16
4. "Snoop không hiểu ngữ cảnh hỏi" — phiếu khảo sát 17
5. "Phần giải thích hơi khó hiểu" — phiếu khảo sát 18
6. "Snoop giải thích khó hiểu" — phiếu khảo sát 20

## 4. Các nguồn có khớp nhau không

Data nói: 399/1.968 lượt trả lời lần đầu ở ôn tập cuối ngày bị sai (20,3%), tức sai là chuyện thường gặp. Người dùng nói: 17/20 từng trả lời sai, 18/20 không hoàn toàn chắc mình đã hiểu sau khi xem lời giải, chỉ 5/20 tự tìm thêm câu tương tự. Hai nguồn **khớp** ở chỗ trả lời sai là phổ biến, và học viên chưa có cách chắc chắn để tự kiểm tra lại.

**Lệch / lưu ý:**

- 14/20 đã tự hỏi ChatGPT hoặc AI riêng, nên nhu cầu có thể đang được đáp ứng bằng công cụ khác chứ không phải "không có cách nào".
- Bốn phiếu (16, 17, 18, 20) nhận xét phần giải thích khó hiểu hoặc "snoop" không hiểu ngữ cảnh. Đây là pain về chất lượng lời giải, hơi khác với pain "thiếu câu luyện".
- Form không có câu hỏi vai ("Bạn là"), nên chưa chứng minh được người trả lời là đúng người dùng; chỉ biết phiếu thu qua form của nhóm.
- Câu thứ 8 đã đổi nội dung giữa lúc thu phiếu (xem `evidence/survey/questions.md`), nên không dùng cột này làm số chính.
- Mẫu nhỏ (n = 20), chưa kiểm chứng việc câu luyện có giúp học viên hiểu hơn.

## 5. Kết luận

Giả thuyết ở evidence/hypothesis.md: đúng một phần. Khảo sát (n = 20, học viên cohort 5, thu qua Discord #chung) cho thấy 17/20 từng trả lời sai, 18/20 không hoàn toàn chắc mình đã hiểu sau khi xem lời giải, và chỉ 5/20 tự tìm thêm câu tương tự để làm. Nhu cầu tự kiểm tra lại là có thật. Tuy nhiên 14/20 đã tự hỏi ChatGPT hoặc AI riêng, và 4 phiếu nêu lời giải khó hiểu, nên pain không chỉ là "thiếu câu luyện" mà còn gồm chất lượng lời giải.
Điều vẫn chưa biết: (1) câu luyện tương đương có giúp học viên hiểu hơn không, chưa thử; (2) không thực hiện phỏng vấn nên chưa kiểm lại khảo sát bằng nguồn khác; (3) mẫu nhỏ (n = 20), chưa xác nhận người trả lời là đúng người dùng vì form không có câu hỏi vai.
