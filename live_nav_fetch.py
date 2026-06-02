import requests
import pandas as pd
from pathlib import Path
import urllib3

urllib3.disable_warnings()

funds = {
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

save_dir = Path("data/raw")

for name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    print(f"\nFetching {name}")

    response = requests.get(
        url,
        timeout=30,
        verify=False
    )

    print("Status:", response.status_code)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = save_dir / f"{name}.csv"

        nav_df.to_csv(file_path, index=False)

        print(f"Saved {file_path}")

    else:
        print(f"Failed {code}")



