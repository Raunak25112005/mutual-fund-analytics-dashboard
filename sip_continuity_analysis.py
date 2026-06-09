import pandas as pd

# Load data
df = pd.read_csv(
    "data/raw/investor_transactions.csv",
    sep="\t"
)

# Date conversion
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# SIP only
sip_df = df[
    df["transaction_type"]
    .str.upper()
    .str.contains("SIP")
].copy()

results = []

for investor, group in sip_df.groupby(
    "investor_id"
):

    if len(group) < 6:
        continue

    group = group.sort_values(
        "transaction_date"
    )

    gaps = (
        group["transaction_date"]
        .diff()
        .dt.days
        .dropna()
    )

    avg_gap = gaps.mean()

    status = (
        "At-Risk"
        if avg_gap > 35
        else "Active"
    )

    results.append([
        investor,
        len(group),
        round(avg_gap, 2),
        status
    ])

report = pd.DataFrame(
    results,
    columns=[
        "investor_id",
        "sip_count",
        "avg_gap_days",
        "status"
    ]
)

report.to_csv(
    "data/processed/sip_continuity_report.csv",
    index=False
)

print(
    report["status"]
    .value_counts()
)

print(
    "\nSaved: data/processed/sip_continuity_report.csv"
)

