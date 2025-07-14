
import streamlit as st
import pandas as pd
import numpy as np
from utils.modeling import load_model

st.header('📊 Overview of Promotional Effectiveness')

st.markdown("""
This dashboard helps assess the performance of promotional campaigns.
We display baseline vs. actual sales and estimate uplift.
""")

if 'df' in st.session_state:
    df = st.session_state['df']
    st.write('### Sample Data', df.head())

    try:
        model = load_model()
        # Predict actual sales
        X_actual = df[['price', 'competitor_price', 'is_promoted']]
        y_pred_actual = model.predict(X_actual)

        # Predict baseline (by forcing is_promoted = 0)
        X_baseline = X_actual.copy()
        X_baseline['is_promoted'] = 0
        y_pred_baseline = model.predict(X_baseline)

        # Save for charting
        df['predicted_sales'] = y_pred_actual
        df['predicted_baseline'] = y_pred_baseline
        df['predicted_uplift'] = df['predicted_sales'] - df['predicted_baseline']

        st.write('### Predicted Sales vs Baseline')
        st.line_chart(df[['predicted_sales', 'predicted_baseline']])

        st.write('### Estimated Uplift Distribution')
        st.bar_chart(df['predicted_uplift'])

        uplift_roi = (df['predicted_uplift'].sum() / df['predicted_baseline'].sum()) * 100
        st.metric("📈 Estimated ROI Lift", f"{uplift_roi:.2f}%")

    except Exception as e:
        st.warning("Model not found or failed to predict. Train model first.")
else:
    st.warning("Please upload or load data first.")
