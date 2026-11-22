# F2-3 – Bảng đo thời gian (luyện)

> Ghi start/end NGAY khi bắt đầu/kết thúc – không ước lượng sau (protocol F2-1). Cách chuỗi prompt phải tính cả thời gian review.

| # | Cách làm | Phạm vi (5 condition tương đương – REQ nào) | Start | End | Phút | Gồm review? | Ghi chú |
|---|---|---|---|---|---|---|---|
| 1 | Thủ công (không dùng AI) | REQ-SF-22 (thẻ tín dụng), 5 condition – `reviewed/manual_5_conditions.json` | không ghi | 2026-11-22 ~22:52 | ~17 (**ước lượng**: 3 + 4 + 3 + 2 + 5) | – | **Ước lượng** của học viên cho từng condition, không ghi giờ bắt đầu/kết thúc theo đồng hồ (lệch protocol F2-1). |
| 2 | Chuỗi prompt PR-F2-01→03 | 10 REQ (bộ cuối 28 condition – `reviewed/conditions_final.json`) | 2026-11-22 17:18:43 | 17:19:45 (sinh) + review 20 phút | ~21 (~1 sinh + 20 review) | Có | Thời gian sinh lấy từ `f2_llm_calls.csv` (run1). |

## Chất lượng 5 condition thủ công (đối chiếu SRS REQ-SF-22)
| ID | Nhận xét | Đánh giá |
|---|---|---|
| C-01 | CVV 3 chữ số là **hợp lệ** theo SRS ("CVV 3–4 chữ số"). Kết quả mong đợi "không thanh toán" mâu thuẫn với SRS. Biên ngoài khoảng là 2 hoặc 5 chữ số. | Sai – cần sửa |
| C-02 | SRS không quy định chữ hoa/thường cho tên chủ thẻ. Kết quả "được chấp nhận" là giả định, không có căn cứ trực tiếp. | Thiếu căn cứ |
| C-03 | Đúng phân vùng sai định dạng số thẻ, nhưng chưa có kết quả mong đợi. `source_quote` nên dùng tiêu chí chấp nhận "Trường sai định dạng → không thanh toán, hiển thị lỗi." | Đạt – cần bổ sung |
| C-04 | Đúng hướng, nhưng mơ hồ: chưa nêu "sai" là sai định dạng MM/YYYY hay ngày ở quá khứ. | Đạt một phần |
| C-05 | SRS không có trường "loại thẻ". Condition không truy vết được về SRS, tương đương một hallucination do người viết. | Loại |

Nhận xét (so sánh, giới hạn của phép đo):
- Làm thủ công mất ~17 phút (ước lượng) cho 5 condition của 1 REQ, tức khoảng 3,4 phút/condition. Có 1 condition sai kết quả mong đợi, 1 condition không có căn cứ SRS, 2 condition chưa đủ cụ thể.
- Chuỗi prompt sinh 21 condition cho 10 REQ trong ~1 phút, nhưng vẫn cần review (sửa kỹ thuật, tách, bổ sung) mới thành bộ 28 condition cuối. Tổng ~21 phút (~1 phút sinh + 20 phút review), tức khoảng 0,75 phút/condition trên bộ cuối.
- Giới hạn của phép đo:
  - Chỉ đo 1 lần.
  - Học viên đã đọc fixture và output AI trước khi làm thủ công, nên phần thủ công có thể nhanh hơn thực tế.
  - Phạm vi hai cách không tương đương (1 REQ so với 10 REQ).
  - Phần thủ công là số phút **ước lượng**. Thời gian review 20 phút do học viên tự báo. Không có giờ bắt đầu/kết thúc ghi ngay lúc làm, nên so sánh chỉ mang tính tham khảo.
