import pandas as pd
import numpy as np

# Load NAV history
df = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(
    ["amfi_code", "date"]
)

# Daily returns
df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
      .pct_change()
)

print("\nDaily Return Summary")

print(
    df["daily_return"].describe()
)

# Save

df.to_csv(
    "data/processed/nav_with_returns.csv",
    index=False
)

print(
    "\nSaved:",
    "data/processed/nav_with_returns.csv"
)
