import pandas as pd

fund_master = pd.read_csv(
    "data/raw/fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/nav_history.csv"
)

master_codes = set(
    fund_master["amfi_code"].astype(str)
)

nav_codes = set(
    nav_history["amfi_code"].astype(str)
)

missing_codes = master_codes - nav_codes

print("Fund Master Codes :", len(master_codes))
print("NAV History Codes :", len(nav_codes))
print("Missing Codes     :", len(missing_codes))

if len(missing_codes) > 0:
    print("\nMissing AMFI Codes:")
    print(list(missing_codes)[:20])
else:
    print("\nAll codes validated.")
