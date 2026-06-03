import pandas as pd

df = pd.read_csv(
    "data/raw/fund_master.csv",
    sep="\t"
)

expense = (
    df.groupby("plan")["expense_ratio_pct"]
      .mean()
      .sort_values()
)

print("\nAverage Expense Ratio\n")
print(expense)
