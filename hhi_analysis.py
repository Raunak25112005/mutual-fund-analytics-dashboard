import pandas as pd

# Load holdings
df = pd.read_csv(
    "data/raw/fund_holdings.csv",
    sep="\t"
)

# HHI calculation
hhi = (
    df.groupby("amfi_code")["weight_pct"]
    .apply(lambda x: (x/100).pow(2).sum())
    .reset_index()
)

hhi.columns = [
    "amfi_code",
    "HHI"
]

hhi = hhi.sort_values(
    "HHI",
    ascending=False
)

hhi.to_csv(
    "data/processed/hhi_report.csv",
    index=False
)

print(hhi.head(10))

print(
    "\nSaved: data/processed/hhi_report.csv"
)
