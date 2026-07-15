"""Streamlit entry point for Streamlit Community Cloud."""

from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Vero Pricing Estimator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_path = Path(__file__).resolve().parent / "docs" / "pricing" / "pricing_calculator.html"
if not html_path.exists():
    st.error("Calculator file not found: docs/pricing/pricing_calculator.html")
    st.stop()

calculator_html = html_path.read_text(encoding="utf-8")
st.components.v1.html(calculator_html, height=2600, scrolling=True)
