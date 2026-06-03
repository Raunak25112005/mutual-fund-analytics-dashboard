import pandas as pd

# Load Data
df = pd.read_csv(
    "data/raw/aum_history.csv",
    sep="\t"
)

# Basic Information
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Latest Available Data
latest = df[df["date"] == "2025-12-31"]

# Top Fund Houses By AUM
print("\nTop Fund Houses By AUM")

print(
    latest.sort_values(
        "aum_crore",
        ascending=False
    )[
        ["fund_house", "aum_crore"]
    ]
)

# Market Share Calculation
print("\nMarket Share (%)")

total_aum = latest["aum_crore"].sum()

latest["market_share_pct"] = (
    latest["aum_crore"]
    / total_aum
    * 100
)

print(
    latest.sort_values(
        "market_share_pct",
        ascending=False
    )[
        ["fund_house", "market_share_pct"]
    ]
)

# Industry Concentration
top5_share = (
    latest
    .sort_values(
        "aum_crore",
        ascending=False
    )
    .head(5)["market_share_pct"]
    .sum()
)

print("\nIndustry Concentration")

print(
    "Top 5 Fund Houses Control:",
    round(top5_share, 2),
    "%"
)

# Growth Analysis
start = df[df["date"] == "2022-03-31"]

growth = latest.merge(
    start,
    on="fund_house",
    suffixes=("_2025", "_2022")
)

growth["growth_pct"] = (
    (
        growth["aum_crore_2025"]
        - growth["aum_crore_2022"]
    )
    / growth["aum_crore_2022"]
    * 100
)

print("\nGrowth Since 2022")

print(
    growth[
        ["fund_house", "growth_pct"]
    ].sort_values(
        "growth_pct",
        ascending=False
    )
)

# Fastest Growing AMC
print("\nFastest Growing AMC")

print(
    growth.loc[
        growth["growth_pct"].idxmax()
    ]
)

# Largest AMC
print("\nLargest AMC")

print(
    latest.loc[
        latest["aum_crore"].idxmax()
    ]
)
