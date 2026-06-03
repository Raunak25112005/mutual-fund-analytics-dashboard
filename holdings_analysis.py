import pandas as pd

# Load Data
df = pd.read_csv(
    "data/raw/fund_holdings.csv",
    sep="\t"
)

# Basic Information
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nUnique Funds:")
print(df["amfi_code"].nunique())

print("\nUnique Stocks:")
print(df["stock_symbol"].nunique())

print("\nUnique Sectors:")
print(df["sector"].nunique())

# =====================================================
# Most Common Stocks Across Funds
# =====================================================

print("\nMost Common Stocks Across Funds")

print(
    df["stock_name"]
    .value_counts()
    .head(10)
)

# =====================================================
# Sector Allocation
# =====================================================

print("\nSector Allocation (%)")

sector_weights = (
    df.groupby("sector")["weight_pct"]
    .sum()
    .sort_values(ascending=False)
)

print(sector_weights)

# =====================================================
# Top Holdings By Weight
# =====================================================

print("\nTop Holdings By Weight")

print(
    df[
        ["stock_name", "sector", "weight_pct"]
    ]
    .sort_values(
        "weight_pct",
        ascending=False
    )
    .head(10)
)

# =====================================================
# Banking Exposure
# =====================================================

banking = df[
    df["sector"] == "Banking"
]

print("\nTotal Banking Exposure")

print(
    round(
        banking["weight_pct"].sum(),
        2
    ),
    "%"
)

# =====================================================
# IT Exposure
# =====================================================

it = df[
    df["sector"] == "IT"
]

print("\nTotal IT Exposure")

print(
    round(
        it["weight_pct"].sum(),
        2
    ),
    "%"
)

# =====================================================
# Top Sectors
# =====================================================

print("\nTop 5 Sectors")

print(
    sector_weights.head(5)
)

# =====================================================
# Top Stock By Total Portfolio Weight
# =====================================================

stock_weights = (
    df.groupby("stock_name")["weight_pct"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Stocks By Aggregate Weight")

print(
    stock_weights.head(10)
)

# =====================================================
# Largest Single Holding
# =====================================================

print("\nLargest Single Holding")

print(
    df.loc[
        df["weight_pct"].idxmax()
    ]
)

# =====================================================
# Sector Diversification
# =====================================================

print("\nSector Diversification")

print(
    df.groupby("sector")
    .size()
    .sort_values(ascending=False)
)

# =====================================================
# Industry Summary
# =====================================================

print("\nIndustry Summary")

print(
    "Total Funds Analysed:",
    df["amfi_code"].nunique()
)

print(
    "Total Stocks Analysed:",
    df["stock_symbol"].nunique()
)

print(
    "Total Sectors:",
    df["sector"].nunique()
)

print(
    "Largest Sector:",
    sector_weights.idxmax()
)

print(
    "Most Common Stock:",
    df["stock_name"]
    .value_counts()
    .idxmax()
)
