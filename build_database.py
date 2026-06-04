from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

tables = {
    "fact_nav":
        "data/processed/nav_history_clean.csv",

    "fact_aum":
        "data/processed/aum_history_clean.csv",

    "fact_sip":
        "data/processed/sip_industry_trends_clean.csv",

    "fact_folio":
        "data/processed/folio_growth_history_clean.csv",

    "fact_category_flow":
        "data/processed/category_flow_history_clean.csv",

    "fact_benchmark":
        "data/processed/benchmark_history_clean.csv",

    "dim_fund":
        "data/processed/fund_master_clean.csv",

    "fact_holdings":
        "data/processed/fund_holdings_clean.csv"
}

for table_name, file_path in tables.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table_name}:",
        len(df),
        "rows"
    )

print("\nDatabase Created Successfully")
