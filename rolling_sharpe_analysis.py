import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/processed/nav_with_returns.csv")

df["date"] = pd.to_datetime(df["date"])

# Select 5 key funds
funds = [
    119551,  # SBI Bluechip
    120504,  # ICICI Bluechip
    100032,  # HDFC Top 100
    119093,  # Axis Bluechip
    118989   # Nippon Large Cap
]

plt.figure(figsize=(12,6))

for fund in funds:

    temp = df[df["amfi_code"] == fund].copy()

    temp = temp.sort_values("date")

    rolling_sharpe = (
        temp["daily_return"]
        .rolling(90)
        .mean()
        /
        temp["daily_return"]
        .rolling(90)
        .std()
    ) * (252 ** 0.5)

    plt.plot(
        temp["date"],
        rolling_sharpe,
        label=str(fund)
    )

plt.title("Rolling 90-Day Sharpe Ratio")
plt.xlabel("Date")
plt.ylabel("Sharpe Ratio")
plt.legend()

plt.tight_layout()

plt.savefig(
    "reports/figures/rolling_sharpe_chart.png"
)

print(
    "Saved: reports/figures/rolling_sharpe_chart.png"
)
