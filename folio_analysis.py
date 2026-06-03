import pandas as pd

df = pd.read_csv(
    "data/raw/folio_growth_history.csv",
    sep="\t"
)

start = df.iloc[0]
end = df.iloc[-1]

total_growth = (
    (end["total_folios_crore"] - start["total_folios_crore"])
    / start["total_folios_crore"]
    * 100
)

print("Total Folio Growth:", round(total_growth, 2), "%")


# ADD THIS PART BELOW

latest = df.iloc[-1]

print("\nLatest Market Share")

print(
    round(
        latest["equity_folios_crore"]
        / latest["total_folios_crore"]
        * 100,
        2
    ),
    "% Equity"
)

print(
    round(
        latest["debt_folios_crore"]
        / latest["total_folios_crore"]
        * 100,
        2
    ),
    "% Debt"
)

print(
    round(
        latest["hybrid_folios_crore"]
        / latest["total_folios_crore"]
        * 100,
        2
    ),
    "% Hybrid"
)


