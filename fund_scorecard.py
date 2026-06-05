import pandas as pd

cagr = pd.read_csv(
    "data/processed/cagr_table.csv"
)

sharpe = pd.read_csv(
    "data/processed/sharpe_ratios.csv"
)

alpha = pd.read_csv(
    "data/processed/alpha_beta.csv"
)

drawdown = pd.read_csv(
    "data/processed/max_drawdown.csv"
)

funds = pd.read_csv(
    "data/processed/fund_master_clean.csv"
)

score = (
    cagr.merge(
        sharpe[
            ["amfi_code","sharpe_ratio"]
        ],
        on="amfi_code"
    )
    .merge(
        alpha,
        on="amfi_code"
    )
    .merge(
        drawdown,
        on="amfi_code"
    )
    .merge(
        funds[
            [
                "amfi_code",
                "expense_ratio_pct"
            ]
        ],
        on="amfi_code"
    )
)

score["return_rank"] = score["cagr_3y"].rank(
    ascending=False
)

score["sharpe_rank"] = score["sharpe_ratio"].rank(
    ascending=False
)

score["alpha_rank"] = score["alpha"].rank(
    ascending=False
)

score["expense_rank"] = score["expense_ratio_pct"].rank(
    ascending=True
)

score["drawdown_rank"] = score["max_drawdown"].rank(
    ascending=False
)

score["fund_score"] = (
    0.30 * score["return_rank"]
    +
    0.25 * score["sharpe_rank"]
    +
    0.20 * score["alpha_rank"]
    +
    0.15 * score["expense_rank"]
    +
    0.10 * score["drawdown_rank"]
)

score.sort_values(
    "fund_score"
).to_csv(
    "data/processed/fund_scorecard.csv",
    index=False
)

print(
    score.sort_values(
        "fund_score"
    ).head(10)
)
