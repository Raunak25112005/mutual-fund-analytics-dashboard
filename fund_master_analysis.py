import pandas as pd

df = pd.read_csv(
    "data/raw/fund_master.csv",
    sep="\t",
    engine="python"

)

print(df.columns.tolist())

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nFund Houses")
print(df["fund_house"].unique())

print("\nCategories")
print(df["category"].unique())

print("\nSub Categories")
print(df["sub_category"].unique())

print("\nRisk Categories")
print(df["risk_category"].unique())

