import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/raw/nav_history.csv",
    sep="\t"
)

print(df.columns.tolist())

df["date"] = pd.to_datetime(df["date"])

plt.figure(figsize=(12, 6))

for code in df["amfi_code"].unique():

    fund_data = df[
        df["amfi_code"] == code
    ]

    plt.plot(
        fund_data["date"],
        fund_data["nav"],
        label=str(code)
    )

plt.title("NAV Performance")
plt.xlabel("Date")
plt.ylabel("NAV")

plt.legend()

plt.tight_layout()

plt.savefig(
    "reports/figures/nav_performance.png"
)

print("Chart saved.")
