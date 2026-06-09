import pandas as pd

# Load data
funds = pd.read_csv(
    "data/raw/fund_master.csv",
    sep="\t"
)

sharpe = pd.read_csv(
    "data/processed/sharpe_ratios.csv"
)

# Merge
df = funds.merge(
    sharpe,
    on="scheme_name"
)

risk = input(
    "Enter risk level (Low / Moderate / High): "
)

risk_map = {
    "Low": ["Low"],
    "Moderate": [
        "Moderate",
        "Moderately High"
    ],
    "High": [
        "High",
        "Very High"
    ]
}

filtered = df[
    df["risk_category"].isin(
        risk_map.get(risk, [])
    )
]

top3 = (
    filtered
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop Recommended Funds:\n")

print(
    top3[
        [
            "scheme_name",
            "fund_house_x",
            "risk_category",
            "sharpe_ratio"
        ]
    ]
)

df = df.rename(
    columns={
        "fund_house_x": "fund_house"
    }
)
