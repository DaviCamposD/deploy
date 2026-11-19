import pandas as pd
import streamlit as st
import plotly.express as px
import openpyxl 

path = "acidentes.xlsx"
df = pd.read_excel(path)


st.title("Painel Streamlit de acidentes por dia da semana")
st.header("")

st.sidebar.header("🔍 Filtros")
st.sidebar.multiselect(
    "Selecione os Estados:",
    options=localidades_disponiveis,
    default=localidades_padrao
)