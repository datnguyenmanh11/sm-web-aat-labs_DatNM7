# Test Plan (T01, rút gọn theo rủi ro) – Giỏ hàng & Checkout – SM-WEB (kịch bản phát hành ShopAssist R1)

> Đầu vào: `02_SRS_Storefront.md` (mục 3.1–3.2), `KB-02_Van_chuyen.md`, review log `A1-4/A1_Review_Log.csv`. Lập ngày 2026-11-27, người lập: DatNM7.
> Khả năng × tác động do học viên chấm (2026-11-27). Ưu tiên và độ sâu suy ra từ điểm theo quy tắc ở mục 1.
> Ghi chú chấm điểm: R-07 chấm 1 × 1, lý do (học viên): "đã có lỗi ở bản trước (duplicate)".

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| Phạm vi | **Trong phạm vi (12 REQ):** REQ-SF-01, 02, 03, 04, 05, 06, 07 (Giỏ hàng); REQ-SF-10, 11, 12, 15, 16 (Checkout). **Ngoài phạm vi:** REQ-SF-13, 14, 20–24 (phương thức thanh toán, hóa đơn), REQ-SF-30–32 (tài khoản), REQ-API-*, REQ-NF-* – thuộc lab sau (A2/A3/A7). |
| Môi trường | UAT Toolshop bản chuẩn https://practicesoftwaretesting.com (trình duyệt Chrome bản mới nhất). Dữ liệu test: tài khoản tự đăng ký bằng email `@example.com` hoặc tài khoản demo công bố trên README Toolshop; sản phẩm có sẵn trên UAT. Chỉ dữ liệu giả (REQ-NF-02). |
| Giả định & phụ thuộc | Ánh xạ SRS ↔ UAT ở mục 4. Phụ thuộc vào câu trả lời BA cho RV-01, RV-02, RV-04, RV-05 (mục 5). REQ-SF-15 chưa triển khai trên UAT → kiểm thử ở mức thiết kế/review. |
| Tiêu chí bắt đầu (entry) / kết thúc (exit) | Xem mục 3. |
| Phạm vi, ưu tiên, độ sâu kiểm thử | Điểm rủi ro **≥ 6:** kiểm thử sâu (BVA + decision table/state transition + đưa vào automation). **3–4:** kiểm thử chuẩn (EP + luồng chính/phụ). **≤ 2:** smoke. |

## 2. Rủi ro và ưu tiên
| ID rủi ro | Mô tả | Khả năng (1–3) | Tác động (1–3) | Điểm | Ưu tiên | Độ sâu | REQ liên quan | Cách kiểm thử |
|---|---|---|---|---|---|---|---|---|
| R-01 | Tính sai ngưỡng miễn phí vận chuyển (SRS 300.000đ ≠ KB-02 500.000đ, chưa rõ tính trước/sau giảm giá) → sai phí trên đơn hàng | 3 | 3 | 9 | Cao | Sâu: BVA + decision table/state transition + automation | REQ-SF-15 · RV-04 (Critical) | Review yêu cầu tới khi BA chốt; sau đó BVA quanh ngưỡng đã chốt (ngưỡng − 1đ, ngưỡng, ngưỡng + 1đ) và decision table nội thành/tỉnh × có/không mã giảm giá. Mức thiết kế (chưa có trên UAT). |
| R-02 | Giới hạn số lượng 1–10 mâu thuẫn với mua sỉ ≥ 20 → chặn sai số lượng hợp lệ hoặc không áp dụng được giảm 5% | 3 | 2 | 6 | Cao | Sâu: BVA + decision table/state transition + automation | REQ-SF-03, REQ-SF-06 · RV-01 (Major) | BVA số lượng 0, 1, 10, 11 trên UAT; giữ REQ-SF-06 ở mức review tới khi BA chốt giới hạn; nếu UAT khác 1–10 → ghi Open Question/defect có bằng chứng. |
| R-03 | Tổng giỏ/thành tiền dòng tính sai khi đổi số lượng hoặc xóa dòng | 2 | 3 | 6 | Cao | Sâu: BVA + decision table/state transition + automation | REQ-SF-04 | EP + kiểm tra tính toán (đổi số lượng, xóa dòng, giỏ nhiều dòng). |
| R-04 | Bỏ qua được bước checkout khi bước trước chưa hợp lệ (chưa đăng nhập, thiếu địa chỉ) | 3 | 3 | 9 | Cao | Sâu: BVA + decision table/state transition + automation | REQ-SF-10, REQ-SF-11 | State transition 4 bước; ca âm: nhảy bước, chưa đăng nhập ở bước 2. |
| R-05 | Thiếu trường địa chỉ bắt buộc mà vẫn sang bước 4, hoặc lỗi không hiển thị tại đúng trường | 2 | 2 | 4 | Trung bình | Chuẩn: EP + luồng chính/phụ | REQ-SF-12 | EP: đủ 5 trường; để trống lần lượt từng trường. |
| R-06 | Thêm được sản phẩm hết hàng vào giỏ / thêm sai số lượng | 2 | 3 | 6 | Cao | Sâu: BVA + decision table/state transition + automation | REQ-SF-01, REQ-SF-02 | EP: còn hàng/hết hàng; kiểm tra số lượng N và biểu tượng giỏ. |
| R-07 | Giỏ hàng mất sau khi đăng xuất và đăng nhập lại | 1 | 1 | 1 | Thấp | Smoke | REQ-SF-07 | State transition đăng nhập → đăng xuất → đăng nhập. |
| R-08 | Không có tiêu chí "hiển thị nhanh" → không có oracle hiệu năng | 1 | 1 | 1 | Thấp | Smoke | REQ-SF-05 · RV-02 (Minor) | Chờ BA cung cấp chỉ số; tạm thời chỉ ghi nhận thời gian tải quan sát được, không kết luận pass/fail. |
| R-09 | Không có tiêu chí "thân thiện" → không đánh giá được giao diện thanh toán | 1 | 1 | 1 | Thấp | Smoke | REQ-SF-16 · RV-05 (Minor) | Chờ BA cung cấp tiêu chí; không viết TC pass/fail cho tới khi có. |

## 3. Tiêu chí bắt đầu / kết thúc
**Entry (bắt đầu thiết kế & thực thi test):**
- UAT Toolshop truy cập được; có tài khoản test `@example.com`.
- Có câu trả lời BA cho lỗi **Critical** (RV-04) trước khi thiết kế test chi tiết cho REQ-SF-15; RV-01 có câu trả lời trước khi thiết kế test cho REQ-SF-06.
- Test plan được mentor review.

**Exit (kết thúc kiểm thử feature):**
- 100% REQ ưu tiên **Cao** trong phạm vi (REQ-SF-01, 02, 03, 04, 10, 11, 12) có TC đã chạy và pass.
- Mọi rủi ro điểm ≥ 6 đã được kiểm thử ở độ sâu tương ứng.
- Không còn defect **Critical** mở; defect Major còn mở có hướng xử lý được chấp thuận.
- Mọi câu hỏi BA (RV-xx) đã đóng hoặc được ghi là rủi ro chấp nhận.

## 4. Môi trường & giả định ánh xạ SRS ↔ Toolshop
| SRS SM-WEB | Toolshop | Giả định / xử lý |
|---|---|---|
| Giỏ hàng, số lượng (REQ-SF-01…04) | Cart, quantity | Giới hạn 1–10 của SRS có thể khác UAT → ghi Open Question/defect kèm bằng chứng. |
| Giỏ hàng giữ sau đăng nhập lại (REQ-SF-07) | Cart của tài khoản đăng nhập | Kiểm thử trên UAT bằng tài khoản test. |
| Checkout 4 bước, đăng nhập (REQ-SF-10, 11) | Checkout: Cart → Sign in → Billing address → Payment | Ánh xạ trực tiếp. |
| Địa chỉ thanh toán 5 trường (REQ-SF-12) | Billing address | Nhãn tiếng Anh. |
| Phí vận chuyển, miễn phí vận chuyển (REQ-SF-15) | Chưa có trên UAT | Kiểm thử ở mức thiết kế/review. |
| Mua sỉ giảm 5% (REQ-SF-06) | Không xác nhận được trên UAT | Mức thiết kế/review tới khi BA chốt RV-01. |
| Tiền tệ VNĐ | UAT dùng tiền tệ khác | Kiểm thử quy tắc ở mức logic. |

## 5. Rủi ro dự án & câu hỏi mở
| ID | Câu hỏi gửi BA | Mức | Ảnh hưởng nếu chưa trả lời |
|---|---|---|---|
| RV-04 | Ngưỡng miễn phí vận chuyển đúng là 300.000đ hay 500.000đ? | Critical | Chặn thiết kế test REQ-SF-15 (R-01). |
| RV-01 | Tối đa là 10 hay cho phép ≥ 20 để áp dụng mua sỉ? | Major | Chặn test REQ-SF-06; ảnh hưởng BVA REQ-SF-03 (R-02). |
| RV-02 | Thời gian tải tối đa là bao nhiêu giây? | Minor | Không có oracle cho REQ-SF-05 (R-08). |
| RV-05 | Có hướng dẫn hay tiêu chí UI/UX cụ thể không? | Minor | Không có oracle cho REQ-SF-16 (R-09). |

Kết quả rà thủ công: học viên tự rà REQ-SF-01, 02, 04, 06, 07, 10, 11, 12 theo 4 nhóm checklist, không phát hiện thêm lỗi ngoài các phát hiện đã ghi ở review log.

Rủi ro dự án: REQ-SF-15 và REQ-SF-06 chưa kiểm được trên UAT → chỉ có bằng chứng ở mức thiết kế; nếu BA trả lời muộn, các REQ này chuyển sang sprint sau.

## 6. Sử dụng AI
| Tác vụ | Công cụ/prompt (version) | Cách kiểm chứng output (checklist: nguồn, traceability, hallucination) | Quyết định giữ/sửa/loại |
|---|---|---|---|
| Rà soát 12 REQ theo checklist (thiếu, mâu thuẫn, mơ hồ, không kiểm thử được) | Colab + Gemini `gemini-3.5-flash-lite`, PR-A1-01 v1.0, temperature 0.2, max_tokens 6000 | Máy: dò trích dẫn SRS/KB nguyên văn (6/6 khớp) + req_id trong phạm vi. Người: đọc lại từng phát hiện với SRS/KB-02, xét trùng, mức độ. | 4 giữ (RV-01, 02, 04, 05), 2 loại – trùng (RV-03, 06), 0 AI bịa. Chi tiết: `A1_Review_Log.csv`, `prompt_record.md`. |
| Soạn nháp test plan (mô tả rủi ro, cách kiểm thử, entry/exit, ánh xạ) từ review log | Trợ lý AI Claude (hội thoại, không lưu dạng prompt ID) | Học viên đối chiếu từng rủi ro với REQ/RV trong review log và bảng ánh xạ của lab guide mục 3 | Khả năng × tác động do **học viên tự chấm**. Ưu tiên và độ sâu tính theo quy tắc mục 1. Phần nháp giữ/sửa sau review của học viên. |
