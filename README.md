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
## Project Workflow

1. Data Collection
2. Data Cleaning & Validation
3. Database Design (SQLite)
4. Exploratory Data Analysis
5. Performance Analytics
6. Advanced Risk Analytics
7. Fund Recommendation Engine
8. Interactive Dashboard
9. Reporting & Presentation

---

## Performance Analytics

The following metrics were calculated for all mutual fund schemes:

- Daily Returns
- CAGR (1-Year and 3-Year)
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Fund Scorecard Ranking

---

## Advanced Analytics

Advanced risk and investor analytics include:

- Historical VaR
- Conditional VaR (CVaR)
- Rolling Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Sector Concentration (HHI)
- Fund Recommendation Engine

---

## Dashboard Modules

- Overview
- AUM Analysis
- SIP Analysis
- Folio Analysis
- Category Flow Analysis
- NAV Analysis
- Fund Rankings
- Performance Analytics
- Risk Analytics

---

## Future Enhancements

- Live NAV integration through APIs
- Portfolio optimization module
- Predictive fund return models
- Cloud deployment
- Personalized investor recommendations
