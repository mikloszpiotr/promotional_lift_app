
import streamlit as st
import pandas as pd

st.header('📊 Overview of Promotional Effectiveness')

st.markdown("""
This dashboard helps assess the performance of promotional campaigns.
We display baseline vs. actual sales and estimate uplift.
""")

if 'df' in st.session_state:
    df = st.session_state['df']
    st.write('### Sample Data', df.head())
    st.line_chart(df[['sales', 'baseline_sales']])
else:
    st.warning("Please upload or load data first.")
