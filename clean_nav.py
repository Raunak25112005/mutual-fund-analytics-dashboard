import pandas as pd

df = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

df = df[
    ["amfi_code", "date", "nav"]
]

df["date"] = pd.to_datetime(df["date"])

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print(df.head())
print(df.shape)
