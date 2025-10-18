import streamlit as st

st.set_page_config(page_title="PROHI Carlos", page_icon="🧠", layout="centered")

st.sidebar.image("./assets/project-logo.jpg", width="stretch")
st.sidebar.info("Use the left menu to navigate to other pages.")

st.title("Welcome to Stroke Risk Prediction Dashboard")
st.caption("Teaching demo • Not for clinical use")

st.subheader("Aims")
st.markdown(
    """
The final project aims to apply data science concepts and skills to a medical case study selected from a public dataset.  
It demonstrates how analytical and technical Python skills from **Data Science for Health Informatics (DSHI)**  
can be applied to understand, model, and visualize health data in a reproducible and interpretable way.  

The project emphasizes:
- Using data-driven methods to identify stroke-related risk patterns  
- Building transparent and ethical decision-support tools  
- Presenting results through clear, interactive dashboards
"""
)
