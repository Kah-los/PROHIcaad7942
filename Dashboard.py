import streamlit as st
import numpy as np
st.set_page_config(
    page_title="PROHI Carlos",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")
tab = st.sidebar.radio(
    "Navigate",
    ["Home","Project","Data"]

)

# # Page information
# Main content based on selected tab
if tab == "Home":
    st.write("# Welcome to Stroke Risk Prediction Dashboard")
    st.write("## Aims:")
    st.markdown("""
    The final project aims to apply data science concepts and skills on a medical case study that you and your team select from a public data source.
    The project assumes that you bring the technical Python skills from previous courses (DSHI: Data Science for Health Informatics),
    as well as the analytical skills to argue how and why specific techniques could enhance the problem domain related to the selected dataset.
    """)


elif tab == "Project":
    st.write("## Project")
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

elif tab == "Data":
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px

    @st.cache_data
    def get_data():
        df = pd.DataFrame(
            np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
        )
        return df
    @st.cache_data
    def convert_for_download(df):
        return df.to_csv().encode("utf-8")

    df = get_data()
    csv = convert_for_download(df)

    st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
      )
    @st.cache_data
    def get_data():
        df = pd.DataFrame(
            np.random.randn(50, 2), columns=["Age", "Stroke risk"]
        )
        return df

    df = get_data()

    st.write("## Interactive Plot")
    fig = px.scatter(df, x="Age", y="Stroke risk", title="Stroke Risk Scatter Plot")
    st.plotly_chart(fig, use_container_width=True)

    st.write("## Aquired Data")
    st.dataframe(df)

    add_slider = st.slider(
        'Select a range of values',
        0.0, 100.0, (25.0,75.0)
        
    )