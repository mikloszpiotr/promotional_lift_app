
import streamlit as st
import pandas as pd
import numpy as np
import os
from utils.modeling import load_model

st.header('📊 Overview of Promotional Effectiveness')

st.markdown("""
This dashboard helps assess the performance of promotional campaigns by comparing predicted baseline sales vs. actual outcomes.
We use a machine learning model to estimate promotional uplift — the additional sales generated due to promotions.

---

#### 🧠 ML Solution
- **Model**: Gradient Boosted Decision Trees (XGBoost)
- **Goal**: Estimate sales with and without promotion
- **How**: Predict actual sales and simulate counterfactual (no promotion) to compute uplift
""")

model_exists = os.path.exists("models/uplift_model.pkl")
st.text(f"🧠 ML model loaded: {model_exists}")

if 'df' in st.session_state:
    df = st.session_state['df']
    st.write('### Sample Data', df.head())

    if model_exists:
        try:
            model = load_model()

            X_actual = df[['price', 'competitor_price', 'is_promoted']]
            y_pred_actual = model.predict(X_actual)

            X_baseline = X_actual.copy()
            X_baseline['is_promoted'] = 0
            y_pred_baseline = model.predict(X_baseline)

            df['predicted_sales'] = y_pred_actual
            df['predicted_baseline'] = y_pred_baseline
            df['predicted_uplift'] = df['predicted_sales'] - df['predicted_baseline']

            st.write('### 📈 Predicted Sales vs. Baseline')
            st.line_chart(df[['predicted_sales', 'predicted_baseline']])

            st.write('### 📊 Uplift Distribution')
            st.bar_chart(df['predicted_uplift'])

            uplift_roi = (df['predicted_uplift'].sum() / df['predicted_baseline'].sum()) * 100
            st.metric("📈 Estimated ROI Lift", f"{uplift_roi:.2f}%")

            st.markdown("### 🔍 Uplift Summary by Product")
            uplift_summary = df.groupby("product_id").agg(
                avg_uplift=pd.NamedAgg(column="predicted_uplift", aggfunc="mean"),
                total_uplift=pd.NamedAgg(column="predicted_uplift", aggfunc="sum")
            ).sort_values("total_uplift", ascending=False)

            st.dataframe(uplift_summary.style.format({"avg_uplift": "{:.2f}", "total_uplift": "{:.2f}"}))

        except Exception as e:
            st.warning(f"⚠️ Model error: {str(e)}")
    else:
        st.warning("🧠 Model not found. Please train it in the 'Train Model' tab.")
else:
    st.warning("📂 No data loaded. Please upload or load sample data first.")
