import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from datetime import date

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="PROHI Carlos", page_icon="🧠", layout="wide")

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.image("./assets/project-logo.jpg", width="stretch")
st.sidebar.info("Use the left menu to navigate to other pages.")

# ── Light styling ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
      .card {padding:1rem;border:1px solid rgba(255,255,255,.1);border-radius:16px}
      .muted {opacity:.7}
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Title & Aims ──────────────────────────────────────────────────────────────
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

# ── Overview (small KPIs + compact chart) ─────────────────────────────────────
st.markdown("### Overview")

@st.cache_data
def synth_overview(n=300, seed=7):
    rng = np.random.default_rng(seed)
    age = rng.integers(18, 90, size=n)
    sbp = rng.normal(130, 18, size=n).clip(80, 220).round().astype(int)
    afib = rng.choice([0, 1], size=n, p=[0.85, 0.15])
    risk = (
        0.35*(age-18)/72 + 0.45*(sbp-80)/140 + 0.2*afib + rng.normal(0, 0.05, n)
    ).clip(0, 1)
    return pd.DataFrame({"Age": age, "SBP": sbp, "AFib": afib, "Risk": risk})

df = synth_overview()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Records", f"{len(df):,}")
k2.metric("Mean Age", f"{df['Age'].mean():.0f}")
k3.metric("AFib Prevalence", f"{(df['AFib'].mean()*100):.1f}%")
k4.metric("Avg Risk", f"{df['Risk'].mean():.2f}")

c1, c2 = st.columns([2, 1])

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    fig = px.histogram(df, x="Risk", nbins=30, title="Risk Distribution (synthetic)")
    fig.update_layout(margin=dict(l=10, r=10, t=40, b=10), height=280)  # Plotly expects numeric height/width
    st.plotly_chart(fig, width="stretch")  # Streamlit sizing (no deprecation)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("**Data notes**")
    st.markdown(
        f"""
- Generated: **{date.today().isoformat()}**  
- SBP range: {int(df['SBP'].min())}–{int(df['SBP'].max())} mmHg  
- Risk range: {df['Risk'].min():.2f}–{df['Risk'].max():.2f}  
- Open **Data Explorer** (left) for interactive edits and downloads.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p class="muted">© PROHI Carlos</p>', unsafe_allow_html=True)
