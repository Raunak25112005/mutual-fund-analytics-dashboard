import pandas as pd

df = pd.read_csv(
    "data/processed/aum_history_clean.csv"
)

print(df.describe())

print("\nTop Fund Houses")

print(
    df.groupby("fund_house")["aum_crore"]
      .max()
      .sort_values(ascending=False)
)
