import pandas as pd

df = pd.read_csv(
    "data/processed/fund_master_clean.csv"
)

corr = df[
    [
        "expense_ratio_pct",
        "exit_load_pct",
        "min_sip_amount",
        "min_lumpsum_amount"
    ]
].corr()

print(corr)

