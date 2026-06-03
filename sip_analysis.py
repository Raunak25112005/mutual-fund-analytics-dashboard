import pandas as pd

# Load Data
df = pd.read_csv(
    "data/raw/sip_industry_trends.csv",
    sep="\t"
)

# Basic Information
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Latest Record
print("\nLatest SIP Data:")
print(df.tail(1))

# Highest SIP Inflow
print("\nHighest SIP Inflow:")
print(
    df.loc[
        df["sip_inflow_crore"].idxmax()
    ]
)

# Average SIP Inflow
print("\nAverage SIP Inflow:")
print(
    round(
        df["sip_inflow_crore"].mean(),
        2
    )
)

# SIP Growth Since Beginning
first = df.iloc[0]
latest = df.iloc[-1]

growth = (
    (
        latest["sip_inflow_crore"]
        - first["sip_inflow_crore"]
    )
    / first["sip_inflow_crore"]
    * 100
)

print("\nSIP Growth Since 2022:")
print(round(growth, 2), "%")

# Highest YoY Growth
print("\nHighest YoY Growth:")

yoy_df = df.dropna(subset=["yoy_growth_pct"])

print(
    yoy_df.loc[
        yoy_df["yoy_growth_pct"].idxmax()
    ]
)

import pandas as pd

# Load Data
df = pd.read_csv(
    "data/raw/sip_industry_trends.csv",
    sep="\t"
)

# Basic Information
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Latest Record
print("\nLatest SIP Data:")
print(df.tail(1))

# Highest SIP Inflow
print("\nHighest SIP Inflow:")
print(
    df.loc[
        df["sip_inflow_crore"].idxmax()
    ]
)

# Average SIP Inflow
print("\nAverage SIP Inflow:")
print(
    round(
        df["sip_inflow_crore"].mean(),
        2
    )
)

# SIP Growth Since Beginning
first = df.iloc[0]
latest = df.iloc[-1]

growth = (
    (
        latest["sip_inflow_crore"]
        - first["sip_inflow_crore"]
    )
    / first["sip_inflow_crore"]
    * 100
)

print("\nSIP Growth Since 2022:")
print(round(growth, 2), "%")

# Highest YoY Growth
print("\nHighest YoY Growth:")

yoy_df = df.dropna(subset=["yoy_growth_pct"])

print(
    yoy_df.loc[
        yoy_df["yoy_growth_pct"].idxmax()
    ]
)

import pandas as pd

# Load Data
df = pd.read_csv(
    "data/raw/sip_industry_trends.csv",
    sep="\t"
)

# Basic Information
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Latest Record
print("\nLatest SIP Data:")
print(df.tail(1))

# Highest SIP Inflow
print("\nHighest SIP Inflow:")
print(
    df.loc[
        df["sip_inflow_crore"].idxmax()
    ]
)

# Average SIP Inflow
print("\nAverage SIP Inflow:")
print(
    round(
        df["sip_inflow_crore"].mean(),
        2
    )
)

# SIP Growth Since Beginning
first = df.iloc[0]
latest = df.iloc[-1]

growth = (
    (
        latest["sip_inflow_crore"]
        - first["sip_inflow_crore"]
    )
    / first["sip_inflow_crore"]
    * 100
)

print("\nSIP Growth Since 2022:")
print(round(growth, 2), "%")

# Highest YoY Growth
print("\nHighest YoY Growth:")

yoy_df = df.dropna(subset=["yoy_growth_pct"])

print(
    yoy_df.loc[
        yoy_df["yoy_growth_pct"].idxmax()
    ]
)

# CAGR Calculation
years = 4

cagr = (
    (
        latest["sip_inflow_crore"]
        / first["sip_inflow_crore"]
    ) ** (1 / years)
    - 1
) * 100

print("\nSIP CAGR:")
print(round(cagr, 2), "%")

# Industry Snapshot
print("\nIndustry Snapshot")

print(
    "Current SIP Inflow:",
    latest["sip_inflow_crore"],
    "crore"
)

print(
    "Active SIP Accounts:",
    latest["active_sip_accounts_crore"],
    "crore"
)

print(
    "New SIP Accounts:",
    latest["new_sip_accounts_lakh"],
    "lakh"
)

print(
    "SIP AUM:",
    latest["sip_aum_lakh_crore"],
    "lakh crore"
)

print(
    "YoY Growth:",
    latest["yoy_growth_pct"],
    "%"
)
import pandas as pd

# Load Data
df = pd.read_csv(
    "data/raw/sip_industry_trends.csv",
    sep="\t"
)

# Basic Information
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Latest Record
print("\nLatest SIP Data:")
print(df.tail(1))

# Highest SIP Inflow
print("\nHighest SIP Inflow:")
print(
    df.loc[
        df["sip_inflow_crore"].idxmax()
    ]
)

# Average SIP Inflow
print("\nAverage SIP Inflow:")
print(
    round(
        df["sip_inflow_crore"].mean(),
        2
    )
)

# SIP Growth Since Beginning
first = df.iloc[0]
latest = df.iloc[-1]

growth = (
    (
        latest["sip_inflow_crore"]
        - first["sip_inflow_crore"]
    )
    / first["sip_inflow_crore"]
    * 100
)

print("\nSIP Growth Since 2022:")
print(round(growth, 2), "%")

# Highest YoY Growth
print("\nHighest YoY Growth:")

yoy_df = df.dropna(subset=["yoy_growth_pct"])

print(
    yoy_df.loc[
        yoy_df["yoy_growth_pct"].idxmax()
    ]
)

# CAGR Calculation
years = 4

cagr = (
    (
        latest["sip_inflow_crore"]
        / first["sip_inflow_crore"]
    ) ** (1 / years)
    - 1
) * 100

print("\nSIP CAGR:")
print(round(cagr, 2), "%")

import pandas as pd

# Load Data
df = pd.read_csv(
    "data/raw/sip_industry_trends.csv",
    sep="\t"
)

# Basic Information
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Latest Record
print("\nLatest SIP Data:")
print(df.tail(1))

# Highest SIP Inflow
print("\nHighest SIP Inflow:")
print(
    df.loc[
        df["sip_inflow_crore"].idxmax()
    ]
)

# Average SIP Inflow
print("\nAverage SIP Inflow:")
print(
    round(
        df["sip_inflow_crore"].mean(),
        2
    )
)

# SIP Growth Since Beginning
first = df.iloc[0]
latest = df.iloc[-1]

growth = (
    (
        latest["sip_inflow_crore"]
        - first["sip_inflow_crore"]
    )
    / first["sip_inflow_crore"]
    * 100
)

print("\nSIP Growth Since 2022:")
print(round(growth, 2), "%")

# Highest YoY Growth
print("\nHighest YoY Growth:")

yoy_df = df.dropna(subset=["yoy_growth_pct"])

print(
    yoy_df.loc[
        yoy_df["yoy_growth_pct"].idxmax()
    ]
)

# CAGR Calculation
years = 4

cagr = (
    (
        latest["sip_inflow_crore"]
        / first["sip_inflow_crore"]
    ) ** (1 / years)
    - 1
) * 100

print("\nSIP CAGR:")
print(round(cagr, 2), "%")

# Industry Snapshot
print("\nIndustry Snapshot")

print(
    "Current SIP Inflow:",
    latest["sip_inflow_crore"],
    "crore"
)

print(
    "Active SIP Accounts:",
    latest["active_sip_accounts_crore"],
    "crore"
)

print(
    "New SIP Accounts:",
    latest["new_sip_accounts_lakh"],
    "lakh"
)

print(
    "SIP AUM:",
    latest["sip_aum_lakh_crore"],
    "lakh crore"
)

print(
    "YoY Growth:",
    latest["yoy_growth_pct"],
    "%"
)
