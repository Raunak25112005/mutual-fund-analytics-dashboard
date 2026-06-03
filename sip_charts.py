import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/raw/sip_industry_trends.csv",
    sep="\t"
)

plt.figure(figsize=(10, 6))

plt.plot(
    df["month"],
    df["sip_inflow_crore"]
)

plt.title("SIP Inflow Growth")
plt.xlabel("Month")
plt.ylabel("SIP Inflow (Crore ₹)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "reports/figures/sip_growth.png"
)

print("Chart saved.")
