import pandas as pd

df = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

results = []

for amfi_code, group in df.groupby("amfi_code"):

    group = group.sort_values("date")

    running_max = group["nav"].cummax()

    drawdown = (
        group["nav"]
        /
        running_max
        - 1
    )

    max_dd = drawdown.min()

    results.append(
        [amfi_code, max_dd]
    )

pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "max_drawdown"
    ]
).to_csv(
    "data/processed/max_drawdown.csv",
    index=False
)
