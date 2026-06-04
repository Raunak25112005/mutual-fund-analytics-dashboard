-- =====================================================
-- 1. Top 5 Fund Houses By AUM
-- =====================================================

SELECT
    fund_house,
    aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;


-- =====================================================
-- 2. Average NAV Across All Funds
-- =====================================================

SELECT
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav;


-- =====================================================
-- 3. Highest SIP Inflow Recorded
-- =====================================================

SELECT
    MAX(sip_inflow_crore) AS highest_sip_inflow
FROM fact_sip;


-- =====================================================
-- 4. Average SIP Inflow
-- =====================================================

SELECT
    ROUND(AVG(sip_inflow_crore), 2) AS average_sip_inflow
FROM fact_sip;


-- =====================================================
-- 5. Latest Total Folios
-- =====================================================

SELECT
    MAX(total_folios_crore) AS latest_total_folios
FROM fact_folio;


-- =====================================================
-- 6. Category-wise Total Net Inflows
-- =====================================================

SELECT
    category,
    SUM(net_inflow_crore) AS total_inflow
FROM fact_category_flow
GROUP BY category
ORDER BY total_inflow DESC;


-- =====================================================
-- 7. Category-wise Average Net Inflows
-- =====================================================

SELECT
    category,
    ROUND(AVG(net_inflow_crore), 2) AS avg_inflow
FROM fact_category_flow
GROUP BY category
ORDER BY avg_inflow DESC;


-- =====================================================
-- 8. Number of Funds by Risk Category
-- =====================================================

SELECT
    risk_category,
    COUNT(*) AS number_of_funds
FROM dim_fund
GROUP BY risk_category
ORDER BY number_of_funds DESC;


-- =====================================================
-- 9. Number of Schemes by Fund House
-- =====================================================

SELECT
    fund_house,
    COUNT(*) AS schemes_count
FROM dim_fund
GROUP BY fund_house
ORDER BY schemes_count DESC;


-- =====================================================
-- 10. Top Holdings by Portfolio Weight
-- =====================================================

SELECT *
FROM fact_holdings
ORDER BY portfolio_weight_pct DESC
LIMIT 10;
