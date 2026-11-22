# Prompt record – F1-3

> Theo mục 1.7 Lab Guide. Mỗi lần gọi AI có ý nghĩa = 1 dòng. Raw output để nguyên trong `raw_ai_output/`.

**Prompt dùng:** script starter `notebook/F1_variability.py` v1.0, prompt `PR-F1-001 v1.0`. System prompt yêu cầu trả lời từ tài liệu và từ chối nếu tài liệu không có. Câu hỏi `Q_E1` (gợi ý giá trị kiểm thử số lượng giỏ hàng) và `Q_E2` (giới hạn số lượng tối đa), kèm hoặc không kèm `SRS_EXCERPT` REQ-SF-03 (fixture hư cấu của khóa học).

**Batch được ghi log:** 21:33 ngày 15/11 (+07). Batch 21:32 cùng cấu hình được giữ làm bằng chứng phụ.

| # | Prompt ID + version | Model + tham số (temperature, top_p, max_tokens) | Input (nguồn) | Raw output (đường dẫn) | Nguồn kiểm chứng (SRS/KB/Swagger/UAT) | Quyết định giữ/sửa/loại | Lý do | Thời gian |
|---|---|---|---|---|---|---|---|---|
| 1 | PR-F1-001 v1.0 (E1, run 1–3) | gemini-3.5-flash-lite, temp 0.0, top_p 0.95, max_tokens 400 | Q_E1 + SRS REQ-SF-03 | `raw_ai_output/run01..03_E1_t0.0_ctx.txt` | SRS REQ-SF-03 (1–10) | **Sửa** (chỉ dùng tham khảo) | 3 output khác nhau dù temp 0. Đều thiếu biên SL=1 và SL=10. Run 3 không có kết quả mong đợi. | 2026-11-15 21:33:14–21:33:22 |
| 2 | PR-F1-001 v1.0 (E1, run 4–6) | gemini-3.5-flash-lite, temp 1.0, top_p 0.95, max_tokens 400 | Q_E1 + SRS REQ-SF-03 | `raw_ai_output/run04..06_E1_t1.0_ctx.txt` | SRS REQ-SF-03 | **Sửa** (chỉ dùng tham khảo) | Đúng phân loại 0/5/11 nhưng thiếu biên 1, 10. Run 6 trùng sha1 với run 1 (temp 0). | 2026-11-15 21:33:27–21:33:34 |
| 3 | PR-F1-001 v1.0 (E2, run 7) | gemini-3.5-flash-lite, temp 0.0, có SRS | Q_E2 + SRS REQ-SF-03 | `raw_ai_output/run07_E2_t0.0_ctx.txt` | SRS REQ-SF-03 | **Giữ** | Đúng SRS: tối đa 10, ngoài khoảng thì không chấp nhận và hiển thị thông báo. | 2026-11-15 21:33:38 |
| 4 | PR-F1-001 v1.0 (E2, run 8) | gemini-3.5-flash-lite, temp 0.0, không có SRS | Q_E2 (không có SRS) | `raw_ai_output/run08_E2_t0.0_noctx.txt` | SRS REQ-SF-03 | **Loại** (không có câu trả lời) | Model trả "Không có trong tài liệu." Từ chối đúng theo system prompt, không bịa giới hạn, nhưng không trả lời được. | 2026-11-15 21:33:43 |
| 5 | PR-F1-001 v1.0 (batch 21:32, 8 lần) | như trên | như trên | `evidence/batch_2132_notebook_output.txt`, `raw_ai_output/f1_runs.csv` | SRS REQ-SF-03 | Giữ (bằng chứng phụ) | Một lần temp 0 trả "Không có trong tài liệu" dù có SRS. Output run 5 trùng sha1 với batch 21:33. | 2026-11-15 21:32 |

Log token từng lời gọi: `raw_ai_output/f1_llm_calls.csv`. Log thí nghiệm: `F1_Experiment_Log.csv`.

## Phần AI sinh đã sửa (nếu có)
- Không dùng thẳng output E1 làm bộ condition. Bộ giá trị kiểm thử REQ-SF-03 lấy theo BVA từ SRS: 0, 1, 5, 10, 11. AI chỉ đưa 0/5/11, nên đã bổ sung hai biên 1 và 10 (xem `conclusion.md` câu 3).
