import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
import yfinance as yf

data_s = pd.read_excel("./data/data_sustainability.xlsx")
data_h = pd.read_excel("./data/data_history.xlsx")

st.set_page_config(page_title = "Sustainability Dashboard",layout = "wide")


#Sidebar
st.sidebar.image("./assets/logo.png",caption = "Sustainability Dashboard")
st.sidebar.header("Navigation")

