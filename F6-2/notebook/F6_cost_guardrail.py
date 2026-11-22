"""Lab F6-2 – đo cost per task trên 2 model + guardrail ngân sách/rate limit/backoff (SM-WEB).
Điền đơn giá theo BẢNG GIÁ TRẢ PHÍ công khai của từng model (ghi URL + ngày tra) – kể cả khi đang dùng free tier.
Chấm chất lượng output bằng rubric F6-1 (05b_Tai_lieu_bo_sung.md) và ghi vào 08_Templates/F6_Model_Quality_Cost.csv.
"""
import os
import pandas as pd
from llm_client import LLM, Budget, BudgetExceeded

# ĐƠN GIÁ LÀ VÍ DỤ – thay bằng giá thật (USD / 1M token)
MODELS = {
    os.getenv("LLM_MODEL_A", "model-A"): (0.30, 2.50),
    os.getenv("LLM_MODEL_B", "model-B"): (0.10, 0.40),
}
PROMPT = open("../f2_fixtures/fixture_srs_cart_checkout.md", encoding="utf-8").read() if os.path.exists("../f2_fixtures/fixture_srs_cart_checkout.md") else ""
TASK = "Sinh test condition dạng JSON (id, req_id, condition, technique, priority, source_quote) cho các yêu cầu sau:\n<SRS>\n" + PROMPT + "\n</SRS>"

for model, (pin, pout) in MODELS.items():
    log = f"f6_calls_{model.replace('/', '_')}.csv"
    llm = LLM(model=model, budget=Budget(max_tokens=20_000), price_in_per_m=pin, price_out_per_m=pout, log_file=log)
    try:
        for i in range(3):                      # 3 lần = 3 task, lấy trung bình
            out = llm.chat(TASK, max_tokens=1500)
            open(f"raw_{model.replace('/', '_')}_{i+1}.json", "w", encoding="utf-8").write(out)
    except BudgetExceeded as e:
        print("Guardrail dừng đúng:", e)
    df = pd.read_csv(log)
    print(model, "cost per task (USD quy đổi):", round(df.cost_usd_equiv.mean(), 6))

# Thử guardrail: ngân sách rất nhỏ phải dừng
tiny = LLM(budget=Budget(max_tokens=500), log_file="f6_guardrail_test.csv")
try:
    for i in range(10):
        tiny.chat("Sinh 5 test condition (JSON) cho yêu cầu: số lượng mỗi sản phẩm trong giỏ từ 1 đến 10.", max_tokens=400)
except BudgetExceeded as e:
    print("Guardrail dừng đúng:", e)
