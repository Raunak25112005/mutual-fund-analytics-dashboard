import pandas as pd
import numpy as np
from scipy.stats import linregress

nav = pd.read_csv(
    "data/processed/nav_with_returns.csv"
)

benchmark = pd.read_csv(
    "data/processed/benchmark_history_clean.csv"
)

benchmark["benchmark_return"] = (
    benchmark["close_value"]
    .pct_change()
)

results = []

benchmark_returns = (
    benchmark["benchmark_return"]
    .dropna()
    .reset_index(drop=True)
)

for amfi_code, group in nav.groupby("amfi_code"):

    fund_returns = (
        group["daily_return"]
        .dropna()
        .reset_index(drop=True)
    )

    n = min(
        len(fund_returns),
        len(benchmark_returns)
    )

    if n < 50:
        continue

    slope, intercept, r, p, se = linregress(
        benchmark_returns[:n],
        fund_returns[:n]
    )

    alpha = intercept * 252
    beta = slope

    results.append(
        [
            amfi_code,
            alpha,
            beta
        ]
    )

pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "alpha",
        "beta"
    ]
).to_csv(
    "data/processed/alpha_beta.csv",
    index=False
)
