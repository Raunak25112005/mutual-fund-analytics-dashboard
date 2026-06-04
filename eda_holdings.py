import pandas as pd

df = pd.read_csv(
    "data/processed/fund_holdings_clean.csv"
)

print(
    df.groupby("sector")
      .size()
      .sort_values(ascending=False)
)
