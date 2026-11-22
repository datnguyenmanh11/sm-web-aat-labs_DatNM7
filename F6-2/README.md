# F6-2 – Đo token/chi phí, so sánh 2 model theo chất lượng–chi phí, guardrail ngân sách/rate limit/backoff

> File này được sinh từ `lab_chain.json` bằng `scripts/generate_lab_docs.py` – không sửa tay. Đề đầy đủ: `05_Lab_Guides.md` mục F6-2.

| Tuần | Day | Thời lượng | Hình thức | Người chấm | Review & fix comment |
|---|---|---|---|---|---|
| 2 | Day 8 | 60' | demo 10' + thực hành & nộp 50' | Mentor | Review lab nền tảng (Day 8) |

**Mục tiêu:** Tính cost per task từ token thật, chọn model bằng rubric chất lượng + chi phí, đặt guardrail.

**Bài học tiên quyết:** F6-1

## ⬅️ Đầu vào từ lab trước
| Từ | File | Mức | Dùng để làm gì |
|---|---|---|---|
| F2-3 | `F2-3/notebook/F2_prompt_chain.py` | Khuyến nghị | LevelUp mô tả task = chuỗi F2-3 của học viên; starter F6_cost_guardrail.py v1.0 (đang dùng) đo bằng prompt gộp TASK trên cùng fixture – ghi rõ trong prompt_record.md. |
| F2-3 | `prompts/PROMPT_LIBRARY.md` | **Bắt buộc** | Ghi prompt/version dùng để đo trên 2 model. |
| F2-3 | `F2-3/AI_Output_Evaluation.md` | Khuyến nghị | Cách đo schema/REQ phủ/hallucination/tái lập của F2-3 dùng lại cho điểm chất lượng. |

Kiểm tra trước khi bắt đầu: `python scripts/check_lab_chain.py F6-2 --mode start`

**Đầu vào khác (bộ tài liệu khóa):**
- 10_Starter_Kit/common/llm_client.py (usage thật, Budget 80%/100%, min_interval_s, retry 429/5xx tối đa 5 lần)
- Rubric chất lượng (bài F6-1 / 05b mục F6-1): schema 25 · coverage 40 · hallucination 25 · tái lập 10; ngưỡng 75
- Bảng giá trả phí công khai https://ai.google.dev/gemini-api/docs/pricing (ghi URL + ngày tra; tách giá vào/ra)
- Fixture 10_Starter_Kit/f2_fixtures/fixture_srs_cart_checkout.md (cùng input F2-3)

## ▶️ Chạy notebook (Colab) – output ghi thẳng vào thư mục lab
- Script: `F6_cost_guardrail.py starter v1.0 (ô %%writefile trong notebook Colab, chỉ sửa 2 dòng MODELS)` · `LAB_OUT=<repo>/F6-2` · biến: `LLM_MODEL_A`, `LLM_MODEL_B`, `LLM_MODEL (model chạy thử guardrail)`, `đơn giá trả phí trong MODELS`
- Ghi ra: `F6-2/f6_calls_<model>.csv`; `F6-2/raw_<model>_<i>.json (chuyển vào raw_ai_output/ khi commit)`; `F6-2/f6_guardrail_test.csv`; `F6-2/evidence/f6_run_log.txt ([CẢNH BÁO] + Guardrail dừng đúng)`; `F6-2/evidence/backoff_log.txt (ô (4), 429 giả lập – SIMULATED)`
- Cách đặt Secrets, clone repo, commit: [colab/COLAB_SETUP.md](../colab/COLAB_SETUP.md)

## Các bước (tóm tắt)
1. Chọn 2 model khác mức (vd bản Flash-Lite đã dùng + một bản lớn hơn); đặt LLM_MODEL_A, LLM_MODEL_B trong Colab Secrets – không in key.
2. Tra bảng giá trả phí (ai.google.dev/gemini-api/docs/pricing): đơn giá input và output riêng cho từng model + URL + ngày tra; thay đơn giá ví dụ.
3. Đo bằng F6_cost_guardrail.py (starter v1.0): mỗi model 3 task (prompt gộp TASK trên fixture, max_tokens 1500); token từ usage (f6_calls_<model>.csv); cost per task = trung bình cost_usd_equiv. Raw raw_<model>_<i>.json → raw_ai_output/.
4. Chấm chất lượng mỗi lần chạy: schema (% hợp lệ × 25), coverage (theo benchmark/mentor), hallucination (25 − 5×số condition bịa), tái lập (chênh req_id ≤1 = 10; 2 = 5; >2 = 0).
5. Chọn model: loại < 75 → rẻ nhất trong nhóm đạt → model chất lượng cao hơn đắt hơn < 20% thì chọn; ghi reason có số liệu.
6. Guardrail ngân sách: Budget(max_tokens=500), gọi lặp → log [CẢNH BÁO] (80%) + 'Guardrail dừng đúng' (100%) → evidence/guardrail_80_100.
7. Backoff 429: chứng minh retry tối đa 5 lần, chờ tăng dần, chỉ retry 429/5xx/timeout (gọi dồn dập hoặc giả lập 429 có ghi rõ) → evidence/backoff_log.txt.
8. Lưu prompt_record, F3 log, evidence index (E-F6-01/02/03); xóa output có thể chứa key; commit và nộp link commit.

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `F6-2/F6_Model_Quality_Cost.csv` | Template chính thức: 2 model × 3 lần – token thật, đơn giá vào/ra + URL + ngày, cost_usd_per_task, điểm 4 tiêu chí, quality_total, ngưỡng 75, selected, reason | **Bắt buộc** | ≥ 6 dòng |
| `F6-2/notebook/*` | Notebook .ipynb (đã xóa mọi output có thể chứa key) hoặc file .md chứa link Colab chỉ xem | **Bắt buộc** | – |
| `F6-2/f6_calls_*.csv` | Log usage từng lời gọi của mỗi model (f6_calls_<modelA>.csv, f6_calls_<modelB>.csv) | **Bắt buộc** | – |
| `F6-2/f6_guardrail_test.csv` | Log lần chạy thử guardrail ngân sách nhỏ | **Bắt buộc** | ≥ 1 dòng |
| `F6-2/evidence/guardrail_80_100*` | Ảnh/log '[CẢNH BÁO] …' và 'Guardrail dừng đúng: Vượt ngân sách…' | **Bắt buộc** | – |
| `F6-2/evidence/backoff_log.txt` | Log backoff khi gặp 429 (thật hoặc giả lập có ghi rõ): chờ tăng dần, dừng sau số lần giới hạn | **Bắt buộc** | – |
| `F6-2/raw_ai_output/*` | Output nguyên bản của 2 model | **Bắt buộc** | – |
| `F6-2/prompt_record.md` | Prompt version dùng cho task, 2 model + tham số | **Bắt buộc** | – |
| `F3_AI_Usage_Escalation_Log.csv` | Dòng F6-2 | **Bắt buộc** | ≥ 3 dòng |

Kiểm tra trước khi nộp: `python scripts/check_lab_chain.py F6-2 --mode submit` → nộp **link commit** qua form + cập nhật `evidence/EVIDENCE_INDEX.md`.

## ➡️ Đầu ra được dùng ở lab sau
| Lab sau | File của lab này | Mức | Dùng để làm gì |
|---|---|---|---|
| A1-4 | `F6-2/F6_Model_Quality_Cost.csv` | Khuyến nghị | Gợi ý (không bắt buộc theo lab guide): dùng model đã chọn ở F6-2 và giữ guardrail cho các lab A. |

Dùng lại ngoài lab: G1 (ước tính chi phí từ token thật).

> ⚠️ Lab sau dùng **bản đã fix comment** – sửa xong theo nhận xét review rồi mới chuyển sang lab tiếp theo.

## ✅ Tự kiểm theo rubric (100 điểm, đạt ≥ 70)
- [ ] Token/chi phí tính đúng từ usage thật, ghi nguồn giá + ngày — **30**
- [ ] So sánh 2 model có điểm chất lượng theo rubric — **25**
- [ ] Guardrail ngân sách/số lần gọi hoạt động (có log) — **25**
- [ ] Backoff khi gặp lỗi 429 — **20**

**Critical fail (dừng chấm):** Lộ API key (notebook chia sẻ, log, commit)

Quy tắc chung: insufficient evidence → 0 điểm tiêu chí; mọi dùng AI có dữ liệu cần cân nhắc → ghi `F3_AI_Usage_Escalation_Log.csv`.
