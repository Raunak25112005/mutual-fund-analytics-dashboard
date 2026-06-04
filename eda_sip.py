import pandas as pd

df = pd.read_csv(
    "data/processed/sip_industry_trends_clean.csv"
)

print(df.describe())

growth = (
    (
        df.iloc[-1]["sip_inflow_crore"]
        -
        df.iloc[0]["sip_inflow_crore"]
    )
    /
    df.iloc[0]["sip_inflow_crore"]
) * 100

print(
    "\nSIP Growth:",
    round(growth,2),
    "%"
)
