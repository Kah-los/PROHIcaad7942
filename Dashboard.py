import streamlit as st
from datetime import date

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="PROHI Carlos", page_icon="🧠", layout="wide")

# ── Minimal sidebar ───────────────────────────────────────────────────────────
st.sidebar.image("./assets/project-logo.jpg", use_container_width=True)
 
 
st.markdown(
    """
    <style>
      .hero h1 { margin-bottom: .25rem; }
      .tagline { opacity:.8; margin-bottom: 1.25rem; }
      .card { padding:1rem; border:1px solid rgba(255,255,255,.08);
              border-radius:16px; }
      .card h3 { margin:0 0 .5rem 0; }
      .small { opacity:.7; font-size:.9rem; }
      footer { opacity:.6; font-size:.85rem; padding-top:1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="hero">', unsafe_allow_html=True)
st.title("Stroke Risk Dashboard")
st.markdown('<div class="tagline">Concise. Interactive. Reproducible.</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


left, right = st.columns(2)

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Project")
    st.write("One-page overview of the workflow and design choices.")
    st.page_link("pages/1_Project.py", label="Open Project", icon="📄")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Data Explorer")
    st.write("Edit records, test inputs, and view the risk distribution.")
    st.page_link("pages/2_Data_Explorer.py", label="Open Data Explorer", icon="📊")
    st.markdown('</div>', unsafe_allow_html=True)


k1, k2, k3, k4 = st.columns(4)
k1.metric("Pages", "2")
k2.metric("Status", "Active")
k3.metric("Theme", "Dark")
k4.metric("Today", date.today().strftime("%Y-%m-%d"))


st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown(
    '<footer>© PROHI Carlos · Teaching demo (not for clinical use)</footer>',
    unsafe_allow_html=True,
)

