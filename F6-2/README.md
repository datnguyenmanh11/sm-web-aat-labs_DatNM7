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
| F2-3 | `F2-3/notebook/*` | **Bắt buộc** | 1 task = 1 lần chạy chuỗi F2-3 của chính học viên (cùng prompt version, cùng input). F6_cost_guardrail v1.1 nạp file .py qua biến F2_CHAIN. |
| F2-3 | `prompts/PROMPT_LIBRARY.md` | **Bắt buộc** | Ghi đúng prompt ID + version dùng để đo trên 2 model. |
| F2-3 | `F2-3/AI_Output_Evaluation.md` | Khuyến nghị | Cách chấm schema/coverage/hallucination của F2-3 dùng lại cho điểm chất lượng. |

Kiểm tra trước khi bắt đầu: `python scripts/check_lab_chain.py F6-2 --mode start`

**Đầu vào khác (bộ tài liệu khóa):**
- 10_Starter_Kit/common/llm_client.py, F6_cost_guardrail.py
- Rubric chất lượng 05b mục F6-1
- Bảng giá trả phí công khai của từng model (ghi URL + ngày tra)

## ▶️ Chạy notebook (Colab) – output ghi thẳng vào thư mục lab
- Script: `10_Starter_Kit/common/F6_cost_guardrail.py` · `LAB_OUT=<repo>/F6-2` · biến: `LLM_MODEL_A`, `LLM_MODEL_B`, `F2_CHAIN=<repo>/F2-3/notebook/F2_prompt_chain.py`, `F2_FIXTURES`
- Ghi ra: `F6-2/F6_Model_Quality_Cost.csv (6 task)`; `F6-2/evidence/f6_guardrail_test.csv (80% / dừng 100% / rate limit / backoff)`; `F6-2/f6_calls_<model>.csv`
- Cách đặt Secrets, clone repo, commit: [colab/COLAB_SETUP.md](../colab/COLAB_SETUP.md)

## Các bước (tóm tắt)
1. Chạy task F2-3 trên 2 model, mỗi model 3 lần; lấy token vào/ra thật từ usage.
2. Quy đổi chi phí theo bảng giá trả phí công khai (ghi URL + ngày tra), kể cả khi dùng free tier.
3. Chấm chất lượng mỗi model theo rubric F6-1 (schema, coverage so benchmark fixture, số hallucination).
4. Chọn model rẻ nhất đạt ngưỡng chất lượng; giải thích.
5. Guardrail: giới hạn lần gọi/phút, ngân sách token (cảnh báo 80%, dừng 100%), backoff khi 429; chạy thử vượt ngân sách và lưu log.

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `F6-2/F6_Model_Quality_Cost.csv` | 2 model × 3 lần: token thật, cost, điểm chất lượng, model được chọn | **Bắt buộc** | ≥ 6 dòng |
| `F6-2/notebook/*` | Notebook có guardrail ngân sách, rate limit, backoff 429 | **Bắt buộc** | – |
| `F6-2/evidence/*` | Ảnh/log khi guardrail kích hoạt (80% cảnh báo, 100% dừng, 429) | **Bắt buộc** | – |

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
