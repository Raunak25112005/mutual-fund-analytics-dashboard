import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/raw/category_flow_history.csv",
    sep="\t"
)

latest_month = df["month"].max()

latest = df[
    df["month"] == latest_month
]

latest = latest.sort_values(
    "net_inflow_crore",
    ascending=False
)

plt.figure(figsize=(10, 6))

plt.bar(
    latest["category"],
    latest["net_inflow_crore"]
)

plt.title(
    f"Category Inflows ({latest_month})"
)

plt.ylabel("Net Inflow (Crore ₹)")

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/category_inflows.png"
)

print("Chart saved.")
