import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title = "Sustainability Dashboard",layout = "wide")
st.subheader("Sustainability Dashboard")

data_s = pd.read_excel("./data/data_sustainability.xlsx")
data_h = pd.read_excel("./data/data_history.xlsx")
st.write(data_s.head(5))
st.write(data_h.head(5))

st.sidebar.image("./assets/logo.png",caption = "Sustainability Dashboard")