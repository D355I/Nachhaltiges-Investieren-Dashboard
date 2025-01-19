import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
import yfinance as yf

st.set_page_config(page_title = "Sustainability Dashboard",layout = "wide")

data_s = pd.read_excel("./data/data_sustainability.xlsx")
data_h = pd.read_excel("./data/data_history.xlsx")

#Sidebar
st.sidebar.image("./assets/logo.png",caption = "Sustainability Dashboard")
st.sidebar.header("Navigation")