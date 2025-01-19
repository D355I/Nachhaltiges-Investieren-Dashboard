import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
import yfinance as yf

st.set_page_config(page_title = "Sustainability Dashboard",layout = "wide")


data_s = pd.read_excel("./data/data_sustainability.xlsx")
data_h = pd.read_excel("./data/data_history.xlsx")

st.title("Welcome to the Stock Sustainability Analysis Dashboard")
st.write("""
**Welcome to the Stock Sustainability Analysis Dashboard**

This powerful and user-friendly Streamlit dashboard provides a comprehensive tool for analyzing and comparing the sustainability of 228 different stocks. Designed to assist investors and sustainability enthusiasts, it offers in-depth insights into the environmental, social, and governance (ESG) performance of publicly traded companies.

With the ability to download additional stocks, users can continuously expand their analysis to cover an even broader range of companies. The dashboard is divided into two primary sections:

- **Info Page**: Gain detailed information about each stock, including company profiles and ESG-related data, helping you to understand the broader sustainability context of each investment.
  
- **Analytics Page**: Dive into the performance analysis of the stocks, where you can evaluate both their financial development and sustainability metrics. This section enables side-by-side comparisons, empowering you to make informed decisions on sustainable investments.

Whether you're a seasoned investor or just beginning to explore sustainable finance, this dashboard serves as a valuable resource to guide your decision-making process.
""")

st.sidebar.image("./assets/logo.png",caption = "Sustainability Dashboard")

