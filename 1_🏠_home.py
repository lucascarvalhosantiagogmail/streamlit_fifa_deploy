import streamlit as st
import pandas as pd
from datetime import datetime
import webbrowser

st.set_page_config(
    page_title="Players",
    page_icon="🏠",
    layout="wide"
)


if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall" , ascending=False)
    st.session_state["data"] = df_data




st.markdown("# FIFA 2023 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [Santiago Engenharia](https://santiagoengenharia.com)")

btn = st.link_button(
    "Acesse os dados no Kaggle",
    "https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown(
    "Página de estudo"
)