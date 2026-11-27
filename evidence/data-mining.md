# Bằng chứng dữ liệu ban đầu — CP1

Trong phần ôn tập cuối ngày trên preclass, có **399 / 1.968 lượt trả lời lần đầu bị sai (20,3%)** trong các lượt có kết quả đúng/sai. Đây là tỷ lệ theo lượt trả lời. Day01 ghi nhận 16 lượt sai lần đầu ở mã kiến thức chatbot_is_app_around_model, một chủ đề ứng viên cho demo.

Nguồn: answers.csv và column_dictionary.csv do BTC cấp, giữ local. Lọc nguon = pre_post_post (ôn tập cuối ngày), lan_thu = 1 và was_correct có giá trị True hoặc False. Mã kc_code cho biết chủ đề của câu hỏi. Các số này chưa xác nhận học viên thiếu bài luyện hoặc bài luyện giúp họ hiểu hơn. Nhóm tự soạn nội dung câu demo vì log không chứa nguyên văn câu hỏi và câu trả lời.

## Tái lập bằng PowerShell

```powershell
$first = @(Import-Csv ./data/preclass/answers.csv | Where-Object {
    $_.nguon -eq 'pre_post_post' -and $_.lan_thu -eq '1' -and $_.was_correct -in @('True','False')
})
$wrong = @($first | Where-Object was_correct -eq 'False')
$first.Count
$wrong.Count
$wrong | Where-Object kc_code -eq 'chatbot_is_app_around_model' | Group-Object lesson_id | Select-Object Count,Name
```

## Giả thuyết cần kiểm

Học viên muốn thử một câu khác cùng chủ đề sau khi xem lời giải. Hỏi học viên: “Lần gần nhất trả lời sai câu ôn cuối ngày, bạn đã làm gì để kiểm tra mình hiểu lại?” Ghi bằng mã P1, P2… kèm vai. Khi thử bản demo, dùng một câu kiểm tra riêng thuộc cùng chủ đề để đo kết quả học.

## Trích dẫn dữ liệu CP2

Một bản ghi đã bỏ trường định danh có các giá trị: nguon = pre_post_post, lan_thu = 1, was_correct = False, kc_code = chatbot_is_app_around_model. Nguồn: answers.csv (BTC). Bản ghi minh họa cách lọc lượt sai, không chứa lời học viên.
