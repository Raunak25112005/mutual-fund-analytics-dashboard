import pandas as pd

df = pd.read_csv(
    "data/processed/folio_growth_history_clean.csv"
)

print(df.describe())

print(
    "\nLatest Folios:"
)

print(
    df.iloc[-1]
)
