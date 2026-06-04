from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

tables = [
    "fact_nav",
    "fact_aum",
    "fact_sip",
    "fact_folio",
    "fact_category_flow",
    "fact_benchmark",
    "dim_fund",
    "fact_holdings"
]

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}",
        engine
    )

    print(
        table,
        ":",
        count["cnt"][0],
        "rows"
    )
