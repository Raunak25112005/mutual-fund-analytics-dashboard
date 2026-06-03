# Mutual Fund Analytics Dashboard

## Overview

A Python-based analytics dashboard for analyzing Indian mutual fund industry trends using historical NAV, SIP, AUM, folio growth, and category flow data.

## Features

* SIP trend analysis
* AUM analysis by fund house
* Folio growth tracking
* Category-wise net inflow analysis
* NAV performance visualization
* Interactive Streamlit dashboard

## Datasets Used

* NAV History
* SIP Industry Trends
* AUM History
* Folio Growth History
* Category Flow History
* Fund Master Data

## Technologies Used

* Python
* Pandas
* Matplotlib
* Streamlit

## Project Structure

data/raw/
reports/figures/
sip_analysis.py
aum_analysis.py
folio_analysis.py
streamlit_app.py

## Key Insights

* SIP inflows grew from ₹11,517 Cr to ₹31,002 Cr.
* SIP CAGR ≈ 28%.
* SBI Mutual Fund is the largest AMC by AUM.
* Mutual fund folios nearly doubled between 2022 and 2025.

## Run Locally

pip install -r requirements.txt

streamlit run streamlit_app.py

