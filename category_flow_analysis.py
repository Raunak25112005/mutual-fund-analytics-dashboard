import pandas as pd

df = pd.read_csv(
    "data/raw/category_flow_history.csv",
    sep="\\t",
    engine="python"
)

print("Columns:")
print(df.columns)

print("\nRows:", len(df))
print("Columns:", len(df.columns))

print("\nCategories:")
print(df["category"].unique())

print("\nTop Categories By Average Flow")

avg_flow = (
    df.groupby("category")["net_inflow_crore"]
      .mean()
      .sort_values(ascending=False)
)

print(avg_flow)

