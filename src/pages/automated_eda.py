# src/pages/automated_eda.py

import streamlit as st
from ydata_profiling import ProfileReport
from src.data_loader import load_and_merge_datasets

def show_automated_eda():
    st.markdown(
    '<h3>📊 EDA Automatizado con librería <span style="color: orange;">ydata</span>',
    unsafe_allow_html=True
    )
    
    df = load_and_merge_datasets()
    
    if df is not None:
        # Crear el perfil con ydata-profiling
        profile = ProfileReport(df, title="EDA - Dataset Unificado", explorative=True)
        # Mostrarlo en Streamlit
        st.components.v1.html(profile.to_html(), height=1000, scrolling=True)

    else:
        st.warning("⚠️ No se pudo cargar el dataset unificado.")


