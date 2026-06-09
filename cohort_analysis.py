import pandas as pd

# Load transactions
df = pd.read_csv(
    "data/raw/investor_transactions.csv",
    sep="\t"
)

# Date conversion
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# First transaction year per investor
first_year = (
    df.groupby("investor_id")["transaction_date"]
    .min()
    .dt.year
)

df["cohort_year"] = df["investor_id"].map(
    first_year
)

# Average investment
avg_amount = (
    df.groupby("cohort_year")["amount_inr"]
    .mean()
)

# Total investment
total_amount = (
    df.groupby("cohort_year")["amount_inr"]
    .sum()
)

# Top fund preference
top_fund = (
    df.groupby(
        ["cohort_year", "amfi_code"]
    )
    .size()
    .reset_index(name="count")
)

top_fund = (
    top_fund.sort_values(
        ["cohort_year", "count"],
        ascending=[True, False]
    )
    .groupby("cohort_year")
    .first()
    .reset_index()
)

report = pd.DataFrame({
    "cohort_year": avg_amount.index,
    "avg_investment": avg_amount.values,
    "total_investment": total_amount.values
})

report = report.merge(
    top_fund[
        ["cohort_year", "amfi_code"]
    ],
    on="cohort_year"
)

report.to_csv(
    "data/processed/cohort_analysis.csv",
    index=False
)

print(report)
print(
    "\nSaved: data/processed/cohort_analysis.csv"
)
