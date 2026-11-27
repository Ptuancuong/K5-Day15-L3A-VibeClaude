# Data card · CP2

| Dataset | Nguồn và xử lý | Quy mô | Giới hạn |
|---|---|---|---|
| Log ôn cuối ngày | BTC cấp, xử lý local từ answers.csv. Lọc pre_post_post, lần đầu và có nhãn đúng/sai. Chỉ xuất số tổng hợp. | 1.968 lượt, 399 sai | Không có nguyên văn câu hỏi hay câu trả lời. Chưa xác nhận nhu cầu luyện thêm. |
| practice.json | 14 câu luyện tự soạn, dùng 7 mã kiến thức từ số liệu tổng hợp. Mỗi mã có hai mức, co_ban và van_dung. Dữ liệu synthetic, soạn theo chủ đề, không dùng seed. | 14 câu | Phạm vi 7 chủ đề. Nhóm chưa duyệt đáp án với học viên hay giáo viên. |
| benchmark.csv | 8 ca dùng mã kiến thức từ log BTC, 16 ca tự viết. Các tình huống và câu luyện đều do nhóm tự dựng. | 24 ca: 10 thường, 8 khó, 6 từ chối | Kiểm tra chọn câu sau kết quả đúng hoặc sai, trả lời giải mẫu theo mã và từ chối yêu cầu không hợp lệ. Chưa đo kết quả học thật. |

Data gốc giữ local, không chuyển vào model. Mock CP2 lấy câu luyện từ ngân hàng tự soạn và tra lời giải chuẩn theo mã câu khi được yêu cầu. Xem evidence/data-mining.md để tái lập số liệu.
