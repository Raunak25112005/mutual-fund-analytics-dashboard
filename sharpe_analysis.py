import pandas as pd
import numpy as np

RF = 0.065

df = pd.read_csv(
    "data/processed/nav_with_returns.csv"
)

funds = pd.read_csv(
    "data/processed/fund_master_clean.csv"
)

results = []

for amfi_code, group in df.groupby("amfi_code"):

    returns = group["daily_return"].dropna()

    if len(returns) < 50:
        continue

    annual_return = returns.mean() * 252

    annual_vol = returns.std() * np.sqrt(252)

    sharpe = (
        (annual_return - RF)
        / annual_vol
    )

    results.append(
        [
            amfi_code,
            annual_return,
            annual_vol,
            sharpe
        ]
    )

results = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "annual_return",
        "annual_volatility",
        "sharpe_ratio"
    ]
)

results = results.merge(
    funds[
        [
            "amfi_code",
            "scheme_name",
            "fund_house"
        ]
    ],
    on="amfi_code"
)

results = results.sort_values(
    "sharpe_ratio",
    ascending=False
)

results.to_csv(
    "data/processed/sharpe_ratios.csv",
    index=False
)

print(
    results[
        [
            "scheme_name",
            "sharpe_ratio"
        ]
    ].head(10)
)
