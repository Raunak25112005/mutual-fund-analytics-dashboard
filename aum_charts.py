import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/raw/aum_history.csv",
    sep="\t"
)

latest_date = df["date"].max()

latest = df[
    df["date"] == latest_date
].sort_values(
    "aum_crore",
    ascending=False
)

plt.figure(figsize=(10, 6))

plt.bar(
    latest["fund_house"],
    latest["aum_crore"]
)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.title("AUM by Fund House")
plt.ylabel("AUM (Crore ₹)")

plt.tight_layout()

plt.savefig(
    "reports/figures/aum_by_fund_house.png"
)

print("Chart saved.")
