# Prompt record – F6-2

> Theo mục 1.7 Lab Guide. Mỗi lần gọi AI có ý nghĩa = 1 dòng. Raw output để nguyên trong `raw_ai_output/`.

**Prompt dùng:** script starter `notebook/F6_cost_guardrail.py` v1.0 gửi **một prompt gộp duy nhất là biến `TASK`**. Prompt này gồm vai trò, yêu cầu sinh test condition dạng JSON theo schema, và đoạn SRS SM-WEB (fixture hư cấu của khóa học). Script **không** dùng chuỗi prompt PR-F2-01/02 của F2-3. Hai model nhận cùng `TASK` và cùng tham số, nên phép so sánh là công bằng.

**Tham số:** `max_tokens=1500`, không đặt temperature hay top_p (mặc định của API). Budget guardrail là `Budget(max_tokens=500)`, `min_interval_s=4`, backoff `2**i + random` tối đa 5 lần.

| # | Prompt ID + version | Model + tham số | Input (nguồn) | Raw output (đường dẫn) | Nguồn kiểm chứng | Quyết định giữ/sửa/loại | Lý do | Thời gian |
|---|---|---|---|---|---|---|---|---|
| 1 | TASK v1.0 (lần 1–3) | gemini-3.5-flash-lite, max_tokens 1500 | `TASK` gộp: SRS SM-WEB fixture khóa học (hư cấu) | `raw_ai_output/raw_gemini-3.5-flash-lite_{1,2,3}.json`, log `f6_calls_gemini-3.5-flash-lite.csv` | SRS SM-WEB (fixture), schema JSON trong `TASK` | **Loại** (không dùng trực tiếp) | Cả 3 lần dừng ở 1496/1500 token, JSON bị cắt và không parse được. Id, technique và priority sai schema/enum. Thiếu REQ-SF-14 và REQ-SF-22. | 2026-11-22 21:49 (+07) |
| 2 | TASK v1.0 (lần 1–3) | gemini-3.1-flash-lite, max_tokens 1500 | như trên | `raw_ai_output/raw_gemini-3.1-flash-lite_{1,2,3}.json`, log `f6_calls_gemini-3.1-flash-lite.csv` | như trên | **Sửa** trước khi dùng | JSON đầy đủ, 3 lần giống hệt, phủ 10/10 REQ. Nhưng schema 0%: id `TC-xx`, technique và priority ngoài enum, có văn xuôi bọc ngoài. TC-02 gắn sai BVA, TC-03 gộp hai biên. | 2026-11-22 21:50 (+07) |
| 3 | Guardrail test (TASK rút gọn) | gemini-3.5-flash-lite, Budget 500 token | prompt ngắn của script | `f6_guardrail_test.csv`, `evidence/f6_run_log.txt`, `evidence/guardrail_80_100_log.txt` | Log script | Giữ (bằng chứng) | Cảnh báo ở 425/500 (≥80%). Dừng đúng khi vượt ngân sách: 1042 > 500 token. | 2026-11-22 21:50 (+07) |
| 4 | Backoff test (giả lập, không gọi API) | `llm_client` với lỗi giả lập 429/400 | — | `evidence/backoff_log.txt` | Log script | Giữ (bằng chứng) | 429: retry 5 lần, chờ 1.51, 2.69, 4.06, 8.34 giây rồi dừng. 400: không retry. | 2026-11-22 21:51 (+07) |

## Phần AI sinh đã sửa (nếu có)
- Chưa sửa output. Cả hai model đều trượt schema (0/25). Hướng sửa dự kiến cho lần chạy sau:
  - Thêm ví dụ JSON đúng `C-01`, nêu enum technique và priority, và yêu cầu "chỉ trả JSON, không văn xuôi" vào `TASK`.
  - Tăng `max_tokens` cho model A (giống cách đã xử lý ở F2-3).
  - Mọi thay đổi trên phải ghi version mới `TASK v1.1`.
- Cột hallucination ghi 0 là kết quả tự đối chiếu `req_id` và `source_quote` với SRS fixture. Cần mentor xác nhận.
- Coverage, `quality_total` và `selected` đang **chờ benchmark của mentor**. Khi chưa có coverage, tổng tối đa của mỗi model là 35 + 40 = 75. Model chỉ đạt ngưỡng nếu coverage ≥ 90%.
