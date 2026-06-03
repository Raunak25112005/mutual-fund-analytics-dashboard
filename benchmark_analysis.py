import pandas as pd

df = pd.read_csv(
    "data/raw/benchmark_history.csv",
    sep="\t"
)

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nAvailable Indices")
print(df["index_name"].unique())

# Convert date
df["date"] = pd.to_datetime(df["date"])

# =====================================================
# Latest Index Values
# =====================================================

latest = (
    df.sort_values("date")
    .groupby("index_name")
    .tail(1)
)

print("\nLatest Index Values")

print(
    latest[
        ["index_name", "date", "close_value"]
    ]
)

# =====================================================
# Index Growth
# =====================================================

start = (
    df.sort_values("date")
    .groupby("index_name")
    .head(1)
)

end = (
    df.sort_values("date")
    .groupby("index_name")
    .tail(1)
)

growth = start.merge(
    end,
    on="index_name",
    suffixes=("_start", "_end")
)

growth["growth_pct"] = (
    (
        growth["close_value_end"]
        - growth["close_value_start"]
    )
    / growth["close_value_start"]
    * 100
)

print("\nIndex Growth (%)")

print(
    growth[
        ["index_name", "growth_pct"]
    ]
)

# =====================================================
# Highest Index Return
# =====================================================

print("\nBest Performing Index")

print(
    growth.loc[
        growth["growth_pct"].idxmax()
    ]
)

# =====================================================
# Volatility
# =====================================================

df = df.sort_values(
    ["index_name", "date"]
)

df["daily_return"] = (
    df.groupby("index_name")["close_value"]
    .pct_change()
)

volatility = (
    df.groupby("index_name")["daily_return"]
    .std()
    * 100
)

print("\nVolatility (%)")

print(volatility)

# =====================================================
# Highest Volatility Index
# =====================================================

print("\nMost Volatile Index")

print(
    volatility.idxmax(),
    round(volatility.max(), 2),
    "%"
)

# =====================================================
# Summary
# =====================================================

print("\nMarket Summary")

print(
    "Number of Indices:",
    df["index_name"].nunique()
)

print(
    "Data Points:",
    len(df)
)
