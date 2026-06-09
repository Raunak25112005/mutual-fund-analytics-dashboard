import pandas as pd
import numpy as np

# Load NAV returns
df = pd.read_csv("data/processed/nav_with_returns.csv")

# Remove missing returns
df = df.dropna(subset=["daily_return"])

results = []

for amfi_code, group in df.groupby("amfi_code"):

    returns = group["daily_return"]

    var_95 = np.percentile(returns, 5)

    cvar_95 = returns[returns <= var_95].mean()

    results.append([
        amfi_code,
        var_95,
        cvar_95
    ])

report = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "VaR_95",
        "CVaR_95"
    ]
)

report = report.sort_values(
    "VaR_95"
)

report.to_csv(
    "data/processed/var_cvar_report.csv",
    index=False
)

print(report.head(10))
print("\nSaved: data/processed/var_cvar_report.csv")
