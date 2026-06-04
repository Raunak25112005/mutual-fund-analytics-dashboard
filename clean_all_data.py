from pathlib import Path
import pandas as pd

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

PROCESSED.mkdir(exist_ok=True)

files = [
    "nav_history.csv",
    "aum_history.csv",
    "category_flow_history.csv",
    "folio_growth_history.csv",
    "sip_industry_trends.csv",
    "benchmark_history.csv",
    "fund_master.csv",
    "fund_holdings.csv"
]

for file in files:

    df = pd.read_csv(
        RAW / file,
        sep="\t"
    )

    df = df.drop_duplicates()

    df.columns = [
        c.strip().lower()
        for c in df.columns
    ]

    output_name = (
        file.replace(
            ".csv",
            "_clean.csv"
        )
    )

    df.to_csv(
        PROCESSED / output_name,
        index=False
    )

    print(
        file,
        "->",
        output_name,
        len(df)
    )
