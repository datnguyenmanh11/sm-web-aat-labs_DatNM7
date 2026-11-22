# F6-2 – Notebook

- Colab (chỉ xem – xóa output có thể chứa key trước khi chia sẻ): https://colab.research.google.com/drive/1AQ1AcQS36L2_hpLpZaGeZwsbKzG4Xgku – phần "F6-2", ô (1)–(5)
- `F6_cost_guardrail.py`, `llm_client.py`: starter v1.0 nguyên văn. Trên Colab chỉ sửa 2 dòng `MODELS` (đơn giá trả phí input/output USD/1M token) – ghi đơn giá đã dùng + URL + ngày tra vào `prompt_record.md` và `F6_Model_Quality_Cost.csv`.
- Task đo: prompt gộp `TASK` của script (1 lời gọi/task, max_tokens 1500) trên `fixture_srs_cart_checkout.md`; mỗi model 3 task; cost per task = trung bình `cost_usd_equiv` trong `f6_calls_<model>.csv`.
- Script ghi raw output `raw_<model>_<i>.json` ở thư mục F6-2 – khi commit chuyển vào `F6-2/raw_ai_output/`.
- Backoff 429: ô (4) giả lập lỗi 429/400 (ghi rõ SIMULATED) → `evidence/backoff_log.txt`.
