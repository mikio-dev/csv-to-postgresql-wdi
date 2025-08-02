import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

st.title("World Population - WDI Sample Dashboard")


@st.cache_data
def load_data():
    engine = create_engine(os.getenv("DATABASE_URL"))
    df = pd.read_sql("SELECT * FROM wdi_data", engine)
    return df


df = load_data()

countries = df["Country Name"].unique()
selected = st.selectbox("Select a country", countries)

filtered = df[df["Country Name"] == selected]
chart_data = filtered.pivot_table(index="Year", values="Value", aggfunc="mean")
st.line_chart(chart_data)
