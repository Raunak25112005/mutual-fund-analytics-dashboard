k# Mutual Fund Analytics Dashboard

## Executive Summary

The objective of this project was to design and develop an end-to-end Mutual Fund Analytics platform capable of collecting, processing, analyzing, and visualizing mutual fund industry data. The project integrates multiple datasets covering Net Asset Value (NAV) history, Assets Under Management (AUM), Systematic Investment Plan (SIP) trends, folio growth, category-wise fund flows, portfolio holdings, and investor transaction behavior.

The project was implemented using Python, Pandas, SQLite, Matplotlib, and Streamlit. A structured ETL pipeline was developed to clean and transform raw datasets before storing them in a relational database. Exploratory data analysis was performed to understand industry growth patterns and fund-level characteristics. Performance analytics such as CAGR, Sharpe Ratio, Sortino Ratio, Alpha, Beta, and Maximum Drawdown were computed to evaluate mutual fund performance. Advanced analytics including Value at Risk (VaR), Conditional Value at Risk (CVaR), Investor Cohort Analysis, SIP Continuity Analysis, and Portfolio Concentration Analysis were also conducted.

An interactive Streamlit dashboard was developed to present the findings through visualizations and performance summaries. The final solution provides investors and analysts with a consolidated platform for understanding mutual fund performance, risk exposure, and investor behavior.

---

# 1. Introduction

## 1.1 Background

The Indian mutual fund industry has experienced significant growth over the last decade due to increasing investor participation, rising financial awareness, and wider adoption of Systematic Investment Plans (SIPs). As the volume of available data increases, it becomes increasingly important to transform raw information into actionable insights.

Mutual fund analysis requires evaluating multiple dimensions such as fund performance, risk characteristics, investor behavior, sector exposure, and industry trends. Performing such analysis manually is inefficient and difficult to scale. This project addresses that challenge by creating a centralized analytics platform capable of processing large datasets and presenting meaningful insights through an interactive dashboard.

## 1.2 Project Objectives

The primary objectives of this project were:

* Develop a complete ETL pipeline for mutual fund datasets.
* Clean and validate raw financial data.
* Design and implement a SQLite database for structured storage.
* Perform exploratory data analysis on industry trends.
* Calculate performance metrics for mutual fund schemes.
* Evaluate risk using advanced statistical techniques.
* Analyze investor transaction behavior.
* Build a fund recommendation engine.
* Create an interactive dashboard for visualization and reporting.

## 1.3 Scope of the Project

The project focuses on historical analysis of mutual fund data rather than real-time market forecasting. The scope includes data processing, descriptive analytics, performance evaluation, risk measurement, investor behavior analysis, and dashboard development.
# 2. Data Sources

The success of any analytics project depends heavily on the quality and diversity of the underlying datasets. This project utilized multiple datasets covering different aspects of the Indian mutual fund industry. Together, these datasets provided a comprehensive view of fund performance, investor participation, industry growth, and portfolio composition.

## 2.1 Fund Master Dataset

The Fund Master dataset served as the reference table for all mutual fund schemes included in the project. It contained information such as AMFI codes, scheme names, fund houses, category classifications, expense ratios, exit loads, minimum investment requirements, and risk categories. This dataset was used extensively throughout the project for data integration and fund-level analysis.

## 2.2 NAV History Dataset

The NAV History dataset contained daily Net Asset Value records for 40 mutual fund schemes from January 2022 to May 2026. This dataset formed the foundation for performance analytics including daily return calculations, CAGR analysis, Sharpe Ratio, Sortino Ratio, Alpha, Beta, Maximum Drawdown, Value at Risk, and Conditional Value at Risk.

## 2.3 SIP Industry Trends Dataset

The SIP dataset provided monthly information on industry-wide Systematic Investment Plan inflows. This data was used to evaluate investor participation trends and assess the growth of disciplined investment behavior over time.

## 2.4 AUM History Dataset

The Assets Under Management dataset contained AUM figures for major mutual fund houses. This dataset helped identify leading asset managers and evaluate changes in market share within the mutual fund industry.

## 2.5 Folio Growth Dataset

The folio dataset tracked the growth of investor accounts across different periods. Since folio count is often used as an indicator of retail investor participation, the dataset provided valuable insights into the expanding reach of mutual funds among investors.

## 2.6 Category Flow Dataset

This dataset recorded inflows and outflows across different mutual fund categories. The information helped identify investor preferences and changing market sentiment toward various asset classes.

## 2.7 Fund Holdings Dataset

The holdings dataset contained portfolio-level information including stock holdings, sector allocations, and portfolio weights. This dataset was used for concentration analysis and portfolio diversification assessment through the Herfindahl-Hirschman Index (HHI).

## 2.8 Investor Transactions Dataset

The investor transaction dataset consisted of more than 32,000 records representing individual investment transactions. The dataset included investor identifiers, transaction dates, transaction amounts, SIP activity, demographic information, and location data. It formed the basis for investor cohort analysis and SIP continuity analysis.

# 3. ETL Design and Data Processing

The ETL process was one of the most critical components of this project. Raw datasets obtained from multiple sources often contain inconsistencies, formatting issues, missing values, and structural differences that make direct analysis difficult. A structured ETL pipeline was therefore developed to ensure data quality and consistency.

## 3.1 Data Extraction

All datasets were imported into Python using Pandas. The extraction process involved reading CSV and tab-separated files from the project directory and validating successful data loading.

## 3.2 Data Validation

Data quality checks were performed on each dataset to identify missing values, duplicate records, invalid entries, and formatting inconsistencies. Validation scripts were developed to automate these checks and ensure that only reliable data was used for further analysis.

## 3.3 Data Cleaning

The cleaning phase involved removing unnecessary columns, correcting data types, standardizing date formats, handling missing values, and validating numerical fields. Particular attention was given to historical NAV data because even small inconsistencies can significantly affect performance calculations.

## 3.4 Data Transformation

Several derived variables were created during the transformation stage. Daily returns were calculated from NAV values, rolling statistics were generated for performance analysis, and additional analytical metrics were derived to support advanced risk modeling.

## 3.5 Data Storage

After cleaning and transformation, the datasets were stored within a SQLite database. The database provided a centralized storage solution and enabled efficient querying for dashboard development and analytical tasks.

# 4. Database Design

A star-schema-inspired database structure was implemented to organize the data efficiently.

## 4.1 Dimension Table

The primary dimension table, dim_fund, contained descriptive information about mutual fund schemes and served as the central reference point for analytical operations.

## 4.2 Fact Tables

Several fact tables were created to store transactional and historical information:

* fact_nav
* fact_aum
* fact_sip
* fact_folio
* fact_category_flow
* fact_holdings
* fact_benchmark

These tables allowed efficient aggregation and analysis of mutual fund data across multiple dimensions.

## 4.3 Database Validation

Database validation scripts were developed to verify row counts, schema integrity, and successful data loading. Validation results confirmed that all tables were populated correctly and ready for analytical processing.

# 5. Exploratory Data Analysis

Exploratory Data Analysis (EDA) was conducted to understand the structure, trends, and characteristics of the mutual fund industry data before performing advanced analytics. The primary objective of this stage was to identify meaningful patterns, growth trends, and relationships within the datasets.

## 5.1 Assets Under Management (AUM) Analysis

Assets Under Management (AUM) is one of the most important indicators of a mutual fund company's market presence and investor confidence. The analysis revealed a significant concentration of assets among a few leading fund houses.

SBI Mutual Fund emerged as the largest asset manager with an AUM exceeding ₹12,50,000 crore. It was followed by ICICI Prudential Mutual Fund and HDFC Mutual Fund. Together, these institutions accounted for a substantial share of the industry's total assets.

The analysis also highlighted the competitive nature of the mutual fund industry, where a limited number of large fund houses dominate the market while several smaller players continue to compete in specialized segments.

**Figure 1: AUM by Fund House**

## 5.2 SIP Growth Analysis

Systematic Investment Plans (SIPs) have become one of the most popular investment methods among retail investors. The SIP analysis demonstrated strong growth throughout the study period.

Monthly SIP inflows increased from approximately ₹11,517 crore to ₹31,002 crore, representing a growth rate of more than 169%. This increase reflects growing investor awareness, increased participation in capital markets, and greater adoption of long-term investment strategies.

The results indicate that SIPs continue to serve as a primary driver of mutual fund industry growth in India.

**Figure 2: SIP Growth Trend**

## 5.3 Folio Growth Analysis

Investor folios provide an indication of participation levels within the mutual fund ecosystem. The folio analysis revealed steady growth across the study period.

Total folios reached approximately 26.12 crore by the end of the analysis period, indicating continued expansion of the investor base. The growth suggests increasing retail participation and greater penetration of mutual fund products across different investor segments.

**Figure 3: Folio Growth Trend**

## 5.4 Category Flow Analysis

Category flow analysis was performed to evaluate investor preferences across different mutual fund categories.

The results showed varying inflow patterns among categories, reflecting changing market conditions and investor sentiment. Equity-oriented schemes generally attracted stronger inflows during favorable market periods, while debt-oriented categories exhibited more conservative investment behavior.

These trends demonstrate how investor preferences shift in response to economic conditions and market expectations.

**Figure 4: Category-wise Net Inflows**

## 5.5 Portfolio Holdings Analysis

The holdings dataset was analyzed to identify dominant sectors across mutual fund portfolios.

Banking emerged as the most frequently represented sector, followed by Information Technology, Pharmaceuticals, Automobiles, Utilities, and Infrastructure. This distribution highlights the importance of these sectors within diversified mutual fund portfolios and reflects broader trends in the Indian equity market.

## 5.6 Key EDA Findings

The major findings from the exploratory analysis were:

* SBI Mutual Fund maintained the highest AUM among analyzed fund houses.
* SIP inflows grew by more than 169% during the study period.
* Total investor folios crossed 26 crore.
* Banking and Information Technology were among the most represented sectors.
* Investor participation continued to expand steadily across multiple fund categories.

# 6. Performance Analytics

Performance analytics were conducted using historical NAV data for 40 mutual fund schemes. The objective was to evaluate fund performance using return-based and risk-adjusted metrics.

## 6.1 Daily Return Analysis

Daily returns were calculated using historical NAV values according to the formula:

Daily Return = (NAVt / NAVt−1) − 1

The return distribution exhibited characteristics typically observed in equity-oriented investment products, including moderate volatility and occasional extreme positive and negative return events.

The mean daily return across all schemes was approximately 0.063%, while the standard deviation remained close to 1.03%.

## 6.2 CAGR Analysis

Compound Annual Growth Rate (CAGR) was used to evaluate long-term performance across schemes.

Several funds demonstrated strong annualized returns over both one-year and three-year periods. Mid-cap and growth-oriented schemes generally produced higher returns, though often at the cost of increased volatility.

Axis Midcap Fund, Mirae Asset Large Cap Fund, ICICI Prudential Bluechip Fund, and HDFC Mid-Cap Opportunities Fund ranked among the strongest performers during the analysis period.

## 6.3 Sharpe Ratio Analysis

The Sharpe Ratio was calculated to evaluate risk-adjusted returns.

Among all analyzed schemes, Mirae Asset Large Cap Fund achieved the highest Sharpe Ratio of approximately 1.45. Other strong performers included Kotak Flexicap Fund, SBI Bluechip Fund, ICICI Prudential Midcap Fund, and DSP Midcap Fund.

A higher Sharpe Ratio indicates that a fund generated greater returns relative to the level of risk assumed by investors.

## 6.4 Sortino Ratio Analysis

While the Sharpe Ratio considers total volatility, the Sortino Ratio focuses specifically on downside risk.

The Sortino analysis provided a more investor-focused perspective by penalizing only negative return fluctuations. Funds exhibiting high Sortino Ratios demonstrated stronger downside risk management capabilities.

## 6.5 Alpha and Beta Analysis

Alpha and Beta metrics were calculated using benchmark-based regression analysis.

Alpha measured a fund's ability to generate returns beyond those explained by market movements, while Beta quantified sensitivity to benchmark fluctuations.

The analysis identified several schemes with positive Alpha values, indicating the ability to outperform benchmark expectations over time.

## 6.6 Maximum Drawdown Analysis

Maximum Drawdown was calculated to measure the largest peak-to-trough decline experienced by each scheme.

This metric provided valuable insight into downside exposure and capital preservation characteristics. Funds exhibiting smaller drawdowns generally demonstrated stronger resilience during market corrections.

## 6.7 Fund Scorecard

A composite Fund Scorecard was developed to rank schemes using multiple performance indicators.

The scoring methodology combined:

* 30% Three-Year CAGR Rank
* 25% Sharpe Ratio Rank
* 20% Alpha Rank
* 15% Expense Ratio Rank
* 10% Maximum Drawdown Rank

The resulting scorecard provided a balanced framework for evaluating overall fund quality rather than relying on a single metric.

# 7. Advanced Analytics

Advanced analytics extended the project beyond traditional performance measurement and focused on risk management and investor behavior.

## 7.1 Value at Risk (VaR)

Historical Value at Risk (VaR) was calculated at the 95% confidence level.

The analysis identified several schemes with higher downside risk profiles. Funds associated with AMFI codes 119599, 119095, and 101207 exhibited the largest negative VaR values, indicating greater exposure to adverse market movements.

## 7.2 Conditional Value at Risk (CVaR)

Conditional Value at Risk was calculated to estimate the average loss beyond the VaR threshold.

CVaR provides a deeper understanding of tail-risk exposure and helps identify schemes that may experience severe losses during extreme market conditions.

## 7.3 Rolling Sharpe Ratio Analysis

Rolling 90-day Sharpe Ratios were calculated to evaluate changes in risk-adjusted performance over time.

The analysis revealed periods of both strong and weak performance across schemes, demonstrating how risk-return characteristics evolve in response to changing market environments.

**Figure 5: Rolling 90-Day Sharpe Ratio**

## 7.4 Investor Cohort Analysis

Investor transaction data was used to segment investors into cohorts based on their first investment year.

The 2024 cohort contributed approximately ₹349 crore in investments and represented the largest investor segment within the dataset. The results suggest that earlier investor cohorts generally accumulated larger investment amounts over time.

## 7.5 SIP Continuity Analysis

SIP continuity analysis examined investment discipline among investors.

Out of investors meeting the analysis criteria, 1,332 were classified as At-Risk due to large gaps between contributions, while only 30 investors were classified as Active.

This finding highlights the importance of monitoring SIP consistency and investor engagement.

## 7.6 Portfolio Concentration Analysis (HHI)

The Herfindahl-Hirschman Index (HHI) was used to measure portfolio concentration.

Higher HHI values indicate greater dependence on a smaller number of holdings, while lower values suggest better diversification.

The analysis identified meaningful differences in portfolio concentration across schemes.

## 7.7 Fund Recommendation Engine

A simple recommendation engine was developed using risk categories and Sharpe Ratios.

Based on investor risk appetite, the engine recommends suitable schemes with strong risk-adjusted performance characteristics.

For moderate-risk investors, top recommendations included:

* Mirae Asset Large Cap Fund
* Kotak Flexicap Fund
* SBI Bluechip Fund

# 8. Dashboard Development

An interactive dashboard was developed using Streamlit to provide a user-friendly interface for exploring mutual fund analytics.

The dashboard integrates multiple analytical modules and enables users to interact with performance metrics, industry trends, and risk indicators.

Dashboard modules include:

* Overview
* AUM Analysis
* SIP Analysis
* Folio Analysis
* Category Flow Analysis
* NAV Analysis
* Fund Rankings
* Performance Analytics
* Risk Analytics

The dashboard provides a centralized platform for monitoring mutual fund performance and exploring industry trends.

**Figure 6: Dashboard Overview**

**Figure 7: Dashboard Analytics Modules**

# 9. Key Findings

The most important findings of the project are summarized below:

1. SBI Mutual Fund maintained the highest Assets Under Management among analyzed fund houses.
2. SIP inflows increased by more than 169% during the study period.
3. Total mutual fund folios exceeded 26 crore.
4. Mirae Asset Large Cap Fund achieved the highest Sharpe Ratio.
5. Several mid-cap schemes delivered strong CAGR performance.
6. Investor participation continued to grow steadily.
7. Most investors were classified as At-Risk in SIP continuity analysis.
8. Portfolio concentration varied significantly across schemes.
9. Banking and Information Technology emerged as dominant sectors.
10. Risk-adjusted analytics provided more reliable fund rankings than simple return comparisons.

# 10. Limitations

Although the project successfully achieved its objectives, several limitations should be acknowledged:

* The analysis relied on historical data and therefore does not guarantee future performance.
* Investor transaction data was synthetic and used for educational purposes.
* Real-time NAV updates were not integrated.
* Portfolio optimization techniques were not implemented.
* The recommendation engine utilized a simplified ranking approach.

# 11. Recommendations

Based on the results of the project, the following recommendations are proposed:

* Integrate live market and NAV data feeds.
* Implement predictive analytics models for return forecasting.
* Expand investor behavior analysis using real-world datasets.
* Enhance recommendation algorithms through machine learning techniques.
* Introduce portfolio optimization and asset allocation modules.

# 12. Future Scope

Future enhancements may include real-time analytics, machine learning-based forecasting, cloud deployment, API integration, personalized investor dashboards, and automated portfolio monitoring systems.

# 13. Conclusion

This project successfully developed a comprehensive Mutual Fund Analytics platform that combines data engineering, financial analytics, risk management, investor behavior analysis, and dashboard visualization. Through the integration of multiple datasets and analytical techniques, the platform provides meaningful insights into mutual fund performance and industry trends.

The project demonstrates how modern data analytics tools can be applied to financial datasets to support better investment decision-making and improve understanding of market behavior. The final solution serves as a strong foundation for future development into a fully integrated financial analytics platform.

