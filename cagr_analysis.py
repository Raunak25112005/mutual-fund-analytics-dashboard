import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

funds = pd.read_csv(
    "data/processed/fund_master_clean.csv"
)

df["date"] = pd.to_datetime(df["date"])

results = []

for amfi_code, group in df.groupby("amfi_code"):

    group = group.sort_values("date")

    latest_date = group["date"].max()

    latest_nav = group.iloc[-1]["nav"]

    # 1 Year CAGR

    one_year_data = group[
        group["date"] >= latest_date - pd.DateOffset(years=1)
    ]

    if len(one_year_data) > 0:

        start_nav = one_year_data.iloc[0]["nav"]

        cagr_1y = (
            latest_nav / start_nav
        ) - 1

    else:

        cagr_1y = np.nan

    # 3 Year CAGR

    three_year_data = group[
        group["date"] >= latest_date - pd.DateOffset(years=3)
    ]

    if len(three_year_data) > 0:

        start_nav = three_year_data.iloc[0]["nav"]

        cagr_3y = (
            (latest_nav / start_nav)
            ** (1 / 3)
        ) - 1

    else:

        cagr_3y = np.nan

    results.append(
        [
            amfi_code,
            cagr_1y,
            cagr_3y
        ]
    )

results = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "cagr_1y",
        "cagr_3y"
    ]
)

results = results.merge(
    funds[
        [
            "amfi_code",
            "scheme_name",
            "fund_house"
        ]
    ],
    on="amfi_code",
    how="left"
)

results = results.sort_values(
    "cagr_3y",
    ascending=False
)

results.to_csv(
    "data/processed/cagr_table.csv",
    index=False
)

print(
    results.head(10)
)
