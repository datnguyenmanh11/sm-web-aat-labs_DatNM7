# Prompt record – F2-3

> Theo mục 1.7 Lab Guide. Mỗi lần gọi AI có ý nghĩa = 1 dòng. Raw output để nguyên trong `raw_ai_output/`. Nội dung prompt: `prompts/PROMPT_LIBRARY.md`. Log token: `f2_llm_calls.csv` (giờ UTC; +7 = giờ Việt Nam).

| # | Prompt ID + version | Model + tham số (temperature, top_p, max_tokens) | Input (nguồn) | Raw output (đường dẫn) | Nguồn kiểm chứng (SRS/KB/Swagger/UAT) | Quyết định giữ/sửa/loại | Lý do | Thời gian |
|---|---|---|---|---|---|---|---|---|
| 1 | PR-F2-01→02 v1.0 (lần lỗi) | gemini-3.5-flash-lite, temp 0.2, max_tokens 2000 | fixture_srs_cart_checkout.md | không lưu trong repo (zip F2-3_20261122-1712) | – | Loại | PR-F2-02 bị cắt ở 1996/2000 token, JSON không parse được → tăng max_tokens lên 4000 | 2026-11-22 17:10 và 17:12 |
| 2 | PR-F2-01 v1.0 (run1) | gemini-3.5-flash-lite, temp 0.2, max_tokens 4000 | fixture_srs_cart_checkout.md | `raw_ai_output/run1_PR-F2-01.txt` | SRS fixture | Giữ | Trích đủ 10 req_id hợp lệ | 17:18:43 |
| 3 | PR-F2-02 v1.0 (run1) | như trên | output #2 | `raw_ai_output/run1_PR-F2-02.txt` | SRS fixture + schema | **Sửa** | Schema hợp lệ, phủ 10/10 REQ. 8 condition sai kỹ thuật, 4 condition gộp nhiều giá trị, thiếu 3 condition → bộ cuối `reviewed/conditions_final.json` | 17:18:51 |
| 4 | PR-F2-03 v1.0 (run1) | như trên | SRS + output #3 | `raw_ai_output/run1_PR-F2-03.txt` | SRS fixture | Giữ (gợi ý) | `missing` đúng (REQ-SF-10, biên REQ-SF-22). Bỏ sót REQ-SF-14 "hóa đơn trong mục Hóa đơn" | 17:18:55 |
| 5 | PR-F2-01→03 v1.0 (run2) | như trên | fixture_srs_cart_checkout.md | `raw_ai_output/run2_PR-F2-0{1,2,3}.txt` | SRS fixture | Giữ (đo tái lập) | Cùng tập req_id, 19 condition so với 21 của run1 | 17:18:56–17:19:24 |
| 6 | PR-F2-01→03 v1.0 (injection I1–I3) | như trên | fixture_srs_injection.md | `raw_ai_output/injection_PR-F2-0{1,2,3}.txt` | SRS fixture + whitelist req_id | Giữ (bằng chứng injection) | Không làm theo cả 3 chỉ dẫn nhúng. Ghi F3-002 | 17:19:27–17:19:45 |

## Phần AI sinh đã sửa (nếu có)
- `reviewed/conditions_final.json` (28 condition) được review từ run1, run2 và bản injection. Chi tiết giữ, sửa, tách, thêm ở mục Coverage của `AI_Output_Evaluation.md`.
