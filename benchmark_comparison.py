import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/cagr_table.csv"
)

top5 = (
    df.sort_values(
        "cagr_3y",
        ascending=False
    )
    .head(5)
)

plt.figure(
    figsize=(10,6)
)

plt.bar(
    top5["scheme_name"],
    top5["cagr_3y"]
)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/benchmark_comparison.png"
)

print(
    "Chart Saved"
)
