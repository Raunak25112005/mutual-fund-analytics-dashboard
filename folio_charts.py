import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/raw/folio_growth_history.csv",
    sep="\t"
)

plt.figure(figsize=(10, 6))

plt.plot(
    df["month"],
    df["total_folios_crore"],
    marker="o"
)

plt.title("Mutual Fund Folio Growth")
plt.xlabel("Month")
plt.ylabel("Folios (Crore)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "reports/figures/folio_growth.png"
)

print("Chart saved.")
