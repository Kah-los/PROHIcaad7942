import streamlit as st
from datetime import date

# ---------- Page config ----------
st.set_page_config(page_title="PROHI Carlos", page_icon="🧠", layout="wide")

# ---------- Sidebar ----------
st.sidebar.image("./assets/project-logo.jpg", use_container_width=True)
st.sidebar.info("Use the left menu to open each page (Project, Data Explorer, etc.).")

# ---------- Header ----------
st.title("Welcome to Stroke Risk Prediction Dashboard")
st.caption("Teaching demo • Not for clinical use")

st.subheader("Aims")
st.markdown(
    """
This project applies data-science concepts to a medical case study using a public dataset.
It demonstrates a reproducible path from **data preparation** → **exploration** → **interactive communication**.
"""
)

# ---------- KPIs / At-a-glance ----------
k1, k2, k3, k4 = st.columns(4)
k1.metric("Pages", "2")
k2.metric("Status", "Active")
k3.metric("Theme", "Dark")
k4.metric("Today", date.today().strftime("%Y-%m-%d"))

st.divider()

# ---------- What’s inside ----------
c1, c2 = st.columns([1, 1])
with c1:
    st.subheader("What you can do here")
    st.markdown(
        """
- **Project**: Read a concise summary of the end-to-end workflow and design choices.
- **Data Explorer**: Interact with synthetic patient records, try unique risk inputs (Age band, SBP, AFib),
  view a live risk distribution, and edit rows with a modern table.
- **Downloads**: Export filtered data directly from the explorer page.
        """
    )
with c2:
    st.subheader("How to navigate")
    st.markdown(
        """
1. Use the **sidebar** to switch pages.
2. Start with **Project** to understand the context.
3. Open **Data Explorer** to interact with the demo data and UI widgets.
        """
    )

st.divider()

# ---------- Notes ----------
st.subheader("Notes")
st.markdown(
    """
- The app uses **Streamlit’s multipage pattern** (`pages/` folder) for a clean structure.
- Visuals, inputs, and layout intentionally differ from other examples to ensure originality.
- Replace synthetic data with your own sources as needed.
"""
)

st.caption("© PROHI Carlos — built with Streamlit")
