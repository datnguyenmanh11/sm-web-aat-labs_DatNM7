# Evidence Index – sm-web-aat-<mã HV>
<!-- TEMPLATE: xóa dòng này khi đã điền xong -->

> Mỗi lab nộp **link commit** qua form nộp bài + cập nhật bảng này. Tiêu chí không có bằng chứng truy được → 0 điểm (mục 1.2).

## A1-1 – Checklist truy cập môi trường
- [ ] UI Toolshop bản chuẩn  - [ ] API `/status`, `/products`  - [ ] Swagger  - [ ] Bản with-bugs  - [ ] Repo cá nhân đã tạo

## Bảng bằng chứng
| Lab | Sản phẩm | Đường dẫn trong repo | Link commit nộp | Ngày nộp | Kết quả review | Commit fix comment |
|---|---|---|---|---|---|---|
| F1-3 | F1_Experiment_Log (8 lần chạy, batch 21:33, có token) + raw output + log gọi API; bổ sung: output batch 21:32. + kết luận + phiếu F1-1 (đủ 4 mục bắt buộc) | `F1-3/F1_Experiment_Log.csv`, `F1-3/conclusion.md`, `F1-3/F1-1_notes.md`, `F1-3/raw_ai_output/`, `F1-3/evidence/batch_2132_notebook_output.txt`, `F3_AI_Usage_Escalation_Log.csv` (F3-001) | [f461826](https://github.com/datnguyenmanh11/DatNM7_sm-web-aat-labs/commit/f4618263d2b760fab1a6cc58552ecb6fd538b90f) | Chưa nộp form | | |
| F2-3 | Chuỗi prompt PR-F2-01/02/03 v1.0: run1, run2, 3 ca injection + log gọi API + AI_Output_Evaluation + bộ condition cuối 28 condition (10/10 REQ) + bảng đo thời gian + prompt library v1 | `F2-3/AI_Output_Evaluation.md`, `F2-3/reviewed/`, `F2-3/time_log.md`, `F2-3/prompt_record.md`, `prompts/PROMPT_LIBRARY.md`, `F2-3/f2_llm_calls.csv`, `F2-3/raw_ai_output/`, `F2-3/notebook/`, `F3_AI_Usage_Escalation_Log.csv` (F3-002) | Commit `[submit F2-3]` (xem git log) | 2026-11-22 | | | |
| F6-2 | Bảng cost/chất lượng 2 model × 3 lần (coverage, total và selected chờ benchmark) + prompt record + log gọi API + guardrail 80/100% + backoff 429/400 – xem E-F6-01..03 | `F6-2/F6_Model_Quality_Cost.csv`, `F6-2/prompt_record.md`, `F6-2/f6_calls_*.csv`, `F6-2/raw_ai_output/`, `F6-2/evidence/`, `F3_AI_Usage_Escalation_Log.csv` (F3-003) | Commit `[submit F6-2]` (xem git log) | 2026-11-22 (coverage chờ benchmark mentor) | | | |
| A1-4 | | | | | | |
| A2-3 | | | | | | |
| A3-2 | | | | | | |
| A4-3 | | | | | | |
| A7-3 | | | | | | |
| A5-3 | | | | | | |
| A6-3 | | | | | | |

## Bằng chứng theo tiêu chí rubric
| ID | Lab | Loại | Mô tả | Link | Tiêu chí rubric chứng minh |
|---|---|---|---|---|---|
| E-F6-01 | F6-2 | File | Bảng cost per task và chất lượng của 2 model (gemini-3.5-flash-lite: 0.003947 USD/task; gemini-3.1-flash-lite: 0.001698 USD/task), giá in/out có nguồn và ngày tra; log token từng lời gọi | [F6_Model_Quality_Cost.csv](../F6-2/F6_Model_Quality_Cost.csv), [f6_calls_gemini-3.5-flash-lite.csv](../F6-2/f6_calls_gemini-3.5-flash-lite.csv), [f6_calls_gemini-3.1-flash-lite.csv](../F6-2/f6_calls_gemini-3.1-flash-lite.csv) | Token/chi phí; so sánh 2 model |
| E-F6-02 | F6-2 | Log | Guardrail ngân sách 500 token: cảnh báo ở 425/500 (≥80%), dừng khi 1042 > 500 | [guardrail_80_100_log.txt](../F6-2/evidence/guardrail_80_100_log.txt), [f6_run_log.txt](../F6-2/evidence/f6_run_log.txt), [f6_guardrail_test.csv](../F6-2/f6_guardrail_test.csv) | Guardrail cảnh báo 80% / dừng 100% |
| E-F6-03 | F6-2 | Log | Backoff giả lập: 429 retry 5 lần, chờ tăng dần 1.51/2.69/4.06/8.34 giây; 400 không retry | [backoff_log.txt](../F6-2/evidence/backoff_log.txt) | Xử lý rate limit / lỗi API |
