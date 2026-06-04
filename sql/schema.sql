CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    amfi_code TEXT UNIQUE,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    date_value DATE UNIQUE
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    amfi_code TEXT,
    date_value DATE,
    nav REAL
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    fund_house TEXT,
    date_value DATE,
    aum_crore REAL
);

CREATE TABLE fact_sip (
    sip_id INTEGER PRIMARY KEY,
    month TEXT,
    sip_inflow_crore REAL,
    active_sip_accounts_crore REAL
);

CREATE TABLE fact_folio (
    folio_id INTEGER PRIMARY KEY,
    month TEXT,
    total_folios_crore REAL
);

CREATE TABLE fact_category_flow (
    flow_id INTEGER PRIMARY KEY,
    month TEXT,
    category TEXT,
    net_inflow_crore REAL
);

CREATE TABLE fact_benchmark (
    benchmark_id INTEGER PRIMARY KEY,
    date_value DATE,
    index_name TEXT,
    close_value REAL
);
