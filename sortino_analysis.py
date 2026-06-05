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

    downside = returns[returns < 0]

    if len(downside) < 10:
        continue

    annual_return = returns.mean() * 252

    downside_std = downside.std() * np.sqrt(252)

    sortino = (
        (annual_return - RF)
        / downside_std
    )

    results.append(
        [amfi_code, sortino]
    )

results = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "sortino_ratio"
    ]
)

results = results.merge(
    funds[
        [
            "amfi_code",
            "scheme_name"
        ]
    ],
    on="amfi_code"
)

results.sort_values(
    "sortino_ratio",
    ascending=False
).to_csv(
    "data/processed/sortino_ratios.csv",
    index=False
)
