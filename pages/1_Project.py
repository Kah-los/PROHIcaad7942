import streamlit as st

st.title("Project")

st.markdown("""
This mini-project summarizes my end-to-end workflow from the DSHI course.
I cleaned and explored a patient-level dataset, engineered features (age groups, BMI bands, hypertension/diabetes flags),
and built a baseline logistic regression and a tree-based model to predict stroke risk.
I evaluated models with stratified cross-validation and focused on recall and AUC to prioritize case finding.
Insights were translated into an interactive dashboard for descriptive trends and simple ‘what-if’ exploration.
While the app here uses synthetic data, the structure mirrors the original workflow: inputs on the left, 
live charts and key figures on the right, and a table preview.
The goal is to demonstrate clear, reproducible steps from data preparation to communication of results.
""")
