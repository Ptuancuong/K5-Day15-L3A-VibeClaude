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

## Kiểm lại ngày 27/11/2026 (Trần Anh Tú, trên `answers.csv` gốc)

Chạy lại đoạn lệnh trên và đoạn dưới trên bản BTC cấp (3.776 dòng, 05–24/11/2026). Kết quả khớp số ở trên:

- 1.968 lượt trả lời lần đầu có kết quả đúng/sai, **399 sai (20,3%)**; 77 học viên làm phần ôn, **69 có ≥1 câu sai**; ôn cuối ngày có 1.970 lượt, trong đó **2 lượt** là lần làm thứ hai (`lan_thu = 2`). Trung vị 4 câu sai / học viên trong số học viên có câu sai (3 nếu tính cả 8 học viên không sai câu nào).
- **Mã kiến thức sai nhiều nhất** (số câu sai / số lượt lần đầu):

  | Mã kiến thức (`kc_code`)         | Sai / lượt lần đầu |
  | -------------------------------- | ------------------ |
  | chatbot_is_app_around_model      | 16 / 41 (39%)      |
  | agentic_fit_scoring_decision     | 12 / 20 (60%)      |
  | ai_product_canvas                | 12 / 15 (80%)      |
  | cot_task_fit                     | 11 / 27 (41%)      |
  | system_prompt_contract           | 9 / 27 (33%)       |
  | react_reasoning_acting_pattern   | 9 / 18 (50%)       |

- **Phân bố số câu sai lần đầu / học viên** (cho persona, `spec.md` §2): ≤2 câu: 31/77 (40,3%) · 3–6 câu: 26/77 (33,8%) · ≥7 câu: 20/77 (26,0%).

```powershell
$perHv = $first | Group-Object hv | ForEach-Object {
    [pscustomobject]@{ hv = $_.Name; sai = @($_.Group | Where-Object was_correct -eq 'False').Count }
}
@($perHv | Where-Object { $_.sai -le 2 }).Count                       # ít
@($perHv | Where-Object { $_.sai -ge 3 -and $_.sai -le 6 }).Count     # vừa
@($perHv | Where-Object { $_.sai -ge 7 }).Count                       # nhiều
$wrong | Group-Object kc_code | Sort-Object Count -Descending | Select-Object -First 6 Count,Name
```

Chỉ giữ số đã tổng hợp, không ghi mã học viên. Giới hạn như trên: log không có nguyên văn câu hỏi và không cho biết học viên có muốn ôn thêm không.

## Giả thuyết cần kiểm

Học viên muốn thử một câu khác cùng chủ đề sau khi xem lời giải. Hỏi học viên: “Lần gần nhất trả lời sai câu ôn cuối ngày, bạn đã làm gì để kiểm tra mình hiểu lại?” Ghi bằng mã P1, P2… kèm vai. Khi thử bản demo, dùng một câu kiểm tra riêng thuộc cùng chủ đề để đo kết quả học.
