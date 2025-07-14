
import streamlit as st
import pandas as pd

st.header('📂 Upload Promotional Data')

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df
    st.success("File uploaded successfully!")
    st.write(df.head())
