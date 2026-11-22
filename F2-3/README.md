# F2-3 – Chuỗi prompt yêu cầu → test condition (JSON schema), self-check, kiểm thử injection + đo thời gian

> File này được sinh từ `lab_chain.json` bằng `scripts/generate_lab_docs.py` – không sửa tay. Đề đầy đủ: `05_Lab_Guides.md` mục F2-3.

| Tuần | Day | Thời lượng | Hình thức | Người chấm | Review & fix comment |
|---|---|---|---|---|---|
| 1 | Day 5 | 135' | demo 15' + thực hành & nộp 120' | Trainer (chữa trong CK1-1) | CK1-1 (Day 6) + Review lab nền tảng (Day 8) |

**Mục tiêu:** Xây chuỗi prompt có version sinh test condition đúng schema, truy vết req ID, phát hiện hallucination, kiểm thử injection, tái lập được.

**Bài học tiên quyết:** F2-1, F2-2

## ⬅️ Đầu vào từ lab trước
| Từ | File | Mức | Dùng để làm gì |
|---|---|---|---|
| F1-3 | `F1-3/conclusion.md` | Khuyến nghị | Bài học F1-3 (biến thiên, hallucination khi thiếu ngữ cảnh) → luôn đưa đoạn SRS vào prompt, cố định config để tái lập. |
| F2-1 | `prompts/PROMPT_LIBRARY.md` | Khuyến nghị | 2 prompt có version + change log từ bài F2-1 (PR-F2-001 v1.0 → v1.1) là điểm xuất phát. |

Kiểm tra trước khi bắt đầu: `python scripts/check_lab_chain.py F2-3 --mode start`

**Đầu vào khác (bộ tài liệu khóa):**
- 10_Starter_Kit/f2_fixtures/ (tc_condition.schema.json, fixture_srs_cart_checkout.md, fixture_srs_injection.md)
- 10_Starter_Kit/common/F2_prompt_chain.py
- KHÔNG dùng Toolshop bản có lỗi

## ▶️ Chạy notebook (Colab) – output ghi thẳng vào thư mục lab
- Script: `F2_prompt_chain.py (starter v1.0, ghi bằng %%writefile trong notebook Colab)` · `LAB_OUT=<repo>/F2-3` · biến: `LLM_MODEL`, `fixtures ở /content/f2_fixtures (đọc qua ../f2_fixtures)`
- Ghi ra: `F2-3/raw_ai_output/run1_*, run2_*, injection_* (v1.0 GHI ĐÈ khi chạy lại – tải zip ngay sau mỗi lần chạy)`; `F2-3/f2_llm_calls.csv`
- Cách đặt Secrets, clone repo, commit: [colab/COLAB_SETUP.md](../colab/COLAB_SETUP.md)

## Các bước (tóm tắt)
1. Bấm giờ start; Colab Secrets; chạy cell cài đặt – không key nào hiện trong cell/output.
2. P1 PR-F2-01 v1.0: trích {req_id, mô tả, giá trị/quy tắc} – phải đủ 10 req_id hợp lệ, thiếu thì sửa prompt (tăng version) trước bước 2. Gốc: 2 prompt có version từ F2-1.
3. P2 PR-F2-02 v1.0: JSON theo tc_condition.schema.json; req_id thuộc danh sách P1; có source_quote nguyên văn.
4. P3 PR-F2-03 v1.0: self-check (req_id lạ, giá trị không có trong SRS, biên thiếu) – xác minh TỪNG mục với fixture trước khi sửa.
5. Validate bằng code: jsonschema + whitelist 10 req_id + source_quote; condition bịa → đánh dấu, loại, ghi lý do → reviewed/conditions_final.json.
6. Injection ≥ 3 ca trên fixture_srs_injection.md (I1 ở REQ-SF-03, I2 ở REQ-SF-04, I3 ở REQ-SF-22): ghi làm theo hay không + kiểm soát phát hiện + hành động. In ra nội dung giống system prompt/key → DỪNG, escalation F3.
7. Tái lập: chạy lại toàn chuỗi 2 lần cùng config (temp 0.2, max_tokens 2000); ghi 'chênh tập req_id run1/run2 → kết luận'.
8. Đo thời gian: thủ công 5 condition vs chuỗi prompt 5 condition tương đương (gồm review) → time_log.md.
9. Sửa prompt → tăng version + change log, chạy lại cùng fixture; không sửa raw output cũ. Không kết luận 'v1.1 chống được injection'.
10. Lưu PROMPT_LIBRARY v1, prompt_record, evidence index (E-F2-01…), F3 log; commit và nộp link commit.

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `prompts/PROMPT_LIBRARY.md` | Prompt library v1: PR-F2-01/02/03 có ID, mục đích, version, định dạng output, change log | **Bắt buộc** | – |
| `F2-3/notebook/*` | Notebook đã chạy (.ipynb, hoặc file .md chứa link Colab chỉ xem) – không chứa key, không bỏ bước validate | **Bắt buộc** | – |
| `F2-3/AI_Output_Evaluation.md` | Theo template chính thức: run1/run2, tái lập, bảng injection I1–I3, coverage, đo thời gian | **Bắt buộc** | – |
| `F2-3/time_log.md` | Bảng đo thời gian (luyện): thủ công 5 condition vs chuỗi prompt (gồm review) – start/end thật | **Bắt buộc** | – |
| `F2-3/raw_ai_output/*` | Raw output nguyên bản: run1_, run2_, injection_* – không sửa, không xóa lần chạy xấu | **Bắt buộc** | – |
| `F2-3/reviewed/conditions_final.json` | Bộ condition sau review (đã loại hallucination, đã đối chiếu self-check với fixture) | **Bắt buộc** | – |
| `F2-3/f2_llm_calls.csv` | Log token mỗi lần gọi (llm_client) | **Bắt buộc** | ≥ 1 dòng |
| `F2-3/prompt_record.md` | Prompt record theo 08_Templates/Prompt_Record.md | **Bắt buộc** | – |
| `F3_AI_Usage_Escalation_Log.csv` | Dòng F2-3 (và dòng escalation nếu injection làm lộ system prompt/chuỗi giống key) | **Bắt buộc** | ≥ 2 dòng |

Kiểm tra trước khi nộp: `python scripts/check_lab_chain.py F2-3 --mode submit` → nộp **link commit** qua form + cập nhật `evidence/EVIDENCE_INDEX.md`.

## ➡️ Đầu ra được dùng ở lab sau
| Lab sau | File của lab này | Mức | Dùng để làm gì |
|---|---|---|---|
| F6-2 | `F2-3/notebook/F2_prompt_chain.py` | **Bắt buộc** | 1 task = 1 lần chạy trọn chuỗi P1→P2→P3 của chính học viên (prompt version đã chốt, cùng fixture) – không dùng prompt gộp riêng của F6_cost_guardrail.py v1.0. |
| F6-2 | `prompts/PROMPT_LIBRARY.md` | **Bắt buộc** | Ghi đúng prompt ID + version dùng để đo trên 2 model. |
| F6-2 | `F2-3/AI_Output_Evaluation.md` | Khuyến nghị | Cách đo schema/REQ phủ/hallucination/tái lập của F2-3 dùng lại cho điểm chất lượng. |
| A2-3 | `prompts/PROMPT_LIBRARY.md` | Khuyến nghị | Tái dùng khung prompt sinh condition JSON (PR-F2-02) làm gốc cho prompt theo từng kỹ thuật. |
| A6-3 | `prompts/PROMPT_LIBRARY.md` | **Bắt buộc** | Prompt library v1 → nâng lên v2. |

Dùng lại ngoài lab: G1 (đánh giá lại rubric); WS #1 (prompt library v1); A1–A5 (prompt library), A6-3 (v2).

> ⚠️ Lab sau dùng **bản đã fix comment** – sửa xong theo nhận xét review rồi mới chuyển sang lab tiếp theo.

## ✅ Tự kiểm theo rubric (100 điểm, đạt ≥ 70)
- [ ] JSON hợp lệ theo schema — **15**
- [ ] Condition truy vết tới req ID; coverage ≥ 70% benchmark fixture (quy ước 1.3) — **30**
- [ ] Phát hiện & loại hallucination — **20**
- [ ] ≥ 3 ca injection được ghi nhận (hành vi + kiểm soát phát hiện) — **15**
- [ ] Config/version đủ để tái lập (2 lần chạy lại) — **10**
- [ ] Bảng đo thời gian — **10**

**Điều kiện bắt buộc:** Coverage ≥ 70% benchmark fixture; ≥ 3 ca injection

**Critical fail (dừng chấm):** Dữ liệu thật/secret trong prompt

Quy tắc chung: insufficient evidence → 0 điểm tiêu chí; mọi dùng AI có dữ liệu cần cân nhắc → ghi `F3_AI_Usage_Escalation_Log.csv`.
