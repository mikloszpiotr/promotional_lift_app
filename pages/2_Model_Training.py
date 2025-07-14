
import streamlit as st
from utils.preprocessing import load_and_prepare_data
from utils.modeling import train_gbdt_model, save_model
import os

st.header('🧠 Train Uplift Model')

if st.button('Train Model'):
    (X_train, X_test, y_train, y_test), df = load_and_prepare_data('data/sample_promotions.csv')
    model = train_gbdt_model(X_train, y_train)
    save_model(model)
    st.success('Model trained and saved successfully!')
    st.session_state['df'] = df
