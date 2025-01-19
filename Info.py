import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
import yfinance as yf

st.set_page_config(page_title = "Sustainability Dashboard",layout = "wide")


data_s = pd.read_excel("./data/data_sustainability.xlsx")
data_h = pd.read_excel("./data/data_history.xlsx")

st.title("Welcome to the Sustainability Dashboard")
st.write("This Dashboard ist made for financial Advertisiment of bsjfbadf<bidBHhibb")


#Sidebar
st.sidebar.image("./assets/logo.png",caption = "Sustainability Dashboard")
st.sidebar.header("Information")




#Switcher
stocks = st.sidebar.selectbox(
    "Select Stocks",
    options=data_s.columns[1:],
    
)

st.sidebar.text("Select Stock to get Overview")



def get_stock_info(stock):
    ticker = yf.Ticker(stock)
    info = ticker.info
    country = info.get("country")
    industry = info.get("industry")
    sector = info.get("sector", "N/A")
    employees =  info.get("fullTimeEmployees")
    summary = info.get("longBusinessSummary", "N/A")

    return country, industry, sector, employees, summary
    

country, industry, sector, employees, summary = get_stock_info(stocks)

st.write(f"Country: {country}")
st.write(f"Industry: {industry}")
st.write(f"Sector: {sector}")
st.write(f"Employees: {employees}") 
st.write(f"Summary: \n\n{summary}")

def stock_activity(stock):
    if stock in data_h.columns:
        stock_data = data_h[["Date", stock]].dropna()
        
        stock_data = stock_data.rename(columns={stock: "Closing Price"})
        
        # Erstellen der Grafik mit Plotly
        fig = px.line(
            stock_data,
            x="Date",
            y="Closing Price",
            title=f"Price History of {stock} - 3 Years",
            labels={"Date": "Date", "Closing Price": "Price (USD)"},
        )
        
        st.plotly_chart(fig)
   
stock_activity(stocks)
