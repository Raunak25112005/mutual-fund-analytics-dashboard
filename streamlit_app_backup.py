import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    layout="wide"
)

st.title("📈 Indian Mutual Fund Analytics Dashboard")

# =====================================================
# LOAD DATA
# =====================================================

sip_df = pd.read_csv(
    "data/raw/sip_industry_trends.csv",
    sep="\t"
)

aum_df = pd.read_csv(
    "data/raw/aum_history.csv",
    sep="\t"
)

folio_df = pd.read_csv(
    "data/raw/folio_growth_history.csv",
    sep="\t"
)

category_df = pd.read_csv(
    "data/raw/category_flow_history.csv",
    sep="\t"
)

# =====================================================
# KPI CARDS
# =====================================================

latest_sip = sip_df.iloc[-1]

latest_aum = aum_df[
    aum_df["date"] == "2025-12-31"
]

total_aum = latest_aum["aum_crore"].sum()

latest_folio = folio_df.iloc[-1]

largest_amc = latest_aum.loc[
    latest_aum["aum_crore"].idxmax()
]["fund_house"]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Latest SIP Inflow",
        f"₹{latest_sip['sip_inflow_crore']:,} Cr"
    )

with col2:
    st.metric(
        "Total Industry AUM",
        f"₹{total_aum:,} Cr"
    )

with col3:
    st.metric(
        "Total Folios",
        f"{latest_folio['total_folios_crore']} Cr"
    )

with col4:
    st.metric(
        "Largest AMC",
        largest_amc
    )

st.divider()

# =====================================================
# SIDEBAR
# =====================================================

page = st.sidebar.selectbox(
    "Select Module",
    [
        "Overview",
        "AUM Analysis",
        "SIP Analysis",
        "Folio Analysis",
        "Category Flows",
        "NAV Analysis"
    ]
)

# =====================================================
# OVERVIEW
# =====================================================

if page == "Overview":

    st.header("Dashboard Overview")

    st.image(
        "reports/figures/aum_by_fund_house.png"
    )

    st.image(
        "reports/figures/sip_growth.png"
    )

# =====================================================
# AUM ANALYSIS
# =====================================================

elif page == "AUM Analysis":

    st.header("AUM Analysis")

    st.image(
        "reports/figures/aum_by_fund_house.png"
    )

    latest_aum = latest_aum.sort_values(
        "aum_crore",
        ascending=False
    )

    st.dataframe(
        latest_aum[
            ["fund_house", "aum_crore"]
        ]
    )

# =====================================================
# SIP ANALYSIS
# =====================================================

elif page == "SIP Analysis":

    st.header("SIP Analysis")

    st.line_chart(
        sip_df.set_index("month")[
            "sip_inflow_crore"
        ]
    )

    st.dataframe(
        sip_df.tail(12)
    )

# =====================================================
# FOLIO ANALYSIS
# =====================================================

elif page == "Folio Analysis":

    st.header("Folio Analysis")

    st.line_chart(
        folio_df.set_index("month")[
            "total_folios_crore"
        ]
    )

    st.dataframe(
        folio_df
    )

# =====================================================
# CATEGORY FLOWS
# =====================================================

elif page == "Category Flows":

    st.header("Category Flows")

    latest_month = category_df["month"].max()

    latest_category = category_df[
        category_df["month"] == latest_month
    ]

    st.bar_chart(
        latest_category.set_index(
            "category"
        )["net_inflow_crore"]
    )

    st.dataframe(
        latest_category
    )

# =====================================================
# NAV ANALYSIS
# =====================================================

elif page == "NAV Analysis":

    st.header("NAV Analysis")

    st.image(
        "reports/figures/nav_performance.png"
    )

    st.info(
        "NAV performance chart generated from historical NAV data."
    )
