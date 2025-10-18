import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Data Explorer")

@st.cache_data
def get_base_data(n=200):
    rng = np.random.default_rng(42)
    ages = rng.integers(18, 90, size=n)
    sbp = rng.normal(130, 18, size=n).clip(80, 220).round().astype(int)
    afib = rng.choice([0, 1], size=n, p=[0.85, 0.15])
    risk = (0.35*(ages-18)/72 + 0.45*(sbp-80)/140 + 0.2*afib + rng.normal(0, 0.05, n)).clip(0, 1)
    return pd.DataFrame({"Age": ages, "SBP": sbp, "AFib": afib, "Risk": risk})

@st.cache_data
def to_csv_bytes(df):
    return df.to_csv(index=False).encode("utf-8")

df = get_base_data()
st.download_button(
    label="Download CSV",
    data=to_csv_bytes(df),
    file_name="stroke_demo_data.csv",
    mime="text/csv",
    icon=":material/download:",
)

st.subheader("Risk Inputs")
c1, c2, c3 = st.columns(3)
with c1:
    age_group = st.select_slider(
        "Age group",
        options=["18–39", "40–49", "50–59", "60–69", "70+"],
        value="50–59"
    )
with c2:
    sbp_input = st.number_input(
        "Systolic BP (mmHg)", min_value=80, max_value=220, value=130, step=1
    )
with c3:
    afib_flag = st.toggle("Atrial fibrillation history", value=False)

age_mid = {"18–39": 30, "40–49": 45, "50–59": 55, "60–69": 65, "70+": 75}[age_group]
user_risk = float(np.clip(0.35*(age_mid-18)/72 + 0.45*(sbp_input-80)/140 + 0.2*(1 if afib_flag else 0), 0, 1))
risk_pct = int(round(user_risk * 100))

def risk_label(p):
    if p < 20: return "Low"
    if p < 40: return "Mild"
    if p < 60: return "Moderate"
    if p < 80: return "High"
    return "Very High"

st.subheader("Summary")
s1, s2 = st.columns([1, 1])
with s1:
    m1, m2, m3 = st.columns(3)
    m1.metric("Age group", age_group)
    m2.metric("SBP", f"{int(sbp_input)} mmHg")
    m3.metric("AFib history", "Yes" if afib_flag else "No")
with s2:
    st.write("Estimated risk")
    st.progress(risk_pct if risk_pct > 0 else 1)
    st.caption(f"{risk_pct}% • {risk_label(risk_pct)}")

st.write("## Interactive Plot")
fig = px.histogram(df, x="Risk", nbins=30, title="Risk Distribution (synthetic)")
fig.add_vline(x=user_risk, line_dash="dash")
st.plotly_chart(fig, use_container_width=True)

st.write("## Overview")
k1, k2, k3 = st.columns(3)
k1.metric("Records", len(df))
k2.metric("Avg Risk", f"{df['Risk'].mean():.2f}")
k3.metric("AFib Prevalence", f"{(df['AFib'].mean()*100):.1f}%")

st.write("## Patient Records")
df_view = df.copy()
df_view["AFib"] = df_view["AFib"].astype(bool)

st.data_editor(
    df_view,
    hide_index=True,
    use_container_width=True,
    num_rows="dynamic",
    column_config={
        "Age": st.column_config.NumberColumn("Age (years)", min_value=18, max_value=100, step=1),
        "SBP": st.column_config.NumberColumn("Systolic BP (mmHg)", min_value=80, max_value=220, step=1),
        "AFib": st.column_config.CheckboxColumn("AFib history"),
        "Risk": st.column_config.ProgressColumn("Risk (0–1)", min_value=0.0, max_value=1.0, format="%.2f"),
    },
    disabled=["Risk"],
)
