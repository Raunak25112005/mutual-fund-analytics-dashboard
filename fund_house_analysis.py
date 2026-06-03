import pandas as pd

df = pd.read_csv(
    "data/raw/fund_master.csv",
    sep="\t"
)

schemes = (
    df.groupby("fund_house")
      .size()
      .sort_values(ascending=False)
)

print("\nSchemes Per Fund House\n")
print(schemes)

