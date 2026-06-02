import pandas as pd

df = pd.read_csv("data/raw/aum_history.csv")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nFund Houses:")
print(df["fund_house"].nunique())

latest = df[df["date"] == df["date"].max()]

print("\nTop AUM Funds:")
print(
    latest.sort_values(
        "aum_crore",
        ascending=False
    )[["fund_house", "aum_crore"]]
)
