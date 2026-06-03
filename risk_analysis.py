
import pandas as pd

df = pd.read_csv(
    "data/raw/fund_master.csv",
    sep="\t"
)

risk = df["risk_category"].value_counts()

print(risk)
