import pandas as pd

df = pd.read_csv(
    "data/raw/sip_industry_trends.csv"
)

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nLatest SIP Data:")
print(df.tail(1))

print("\nHighest SIP Inflow:")
print(
    df.loc[
        df["sip_inflow_crore"].idxmax()
    ]
)

print("\nAverage SIP Inflow:")
print(
    round(
        df["sip_inflow_crore"].mean(),
        2
    )
)
