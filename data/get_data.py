import pandas as pd
import yfinance as yf
import numpy as np
from datetime import timedelta, datetime

stocks_list = ["AAPL", "MSFT", "GOOGL", "AMZN", "FB", "TSLA", "NVDA", "ADBE", "INTC", "CSCO",
    "CRM", "QCOM", "AVGO", "ORCL", "AMD", "IBM", "TXN", "PYPL", "NOW", "INTU",
    "JNJ", "UNH", "PFE", "ABBV", "MRK", "TMO", "ABT", "DHR", "BMY", "LLY",
    "CVS", "AMGN", "GILD", "REGN", "ISRG", "BIIB", "VRTX", "MDT", "ZTS", "SYK",
    "JPM", "BAC", "WFC", "C", "GS", "MS", "BLK", "BK", "TROW", "SCHW",
    "AXP", "COF", "DFS", "PNC", "USB", "TD", "BMO", "RY", "CB", "MMC",
    "PG", "KO", "PEP", "PM", "MO", "CL", "KMB", "HSY", "EL", "MNST",
    "HD", "LOW", "NKE", "TGT", "COST", "MCD", "SBUX", "TJX", "DG", "YUM",
    "XOM", "CVX", "SLB", "COP", "EOG", "PXD", "OXY", "PSX", "VLO", "MPC",
    "HES", "HAL", "BKR", "FANG", "DVN", "APA", "CLR", "LNG", "WMB", "KMI",
    "GE", "HON", "BA", "LMT", "RTX", "CAT", "DE", "MMM", "UNP", "CSX",
    "NSC", "UPS", "FDX", "ETN", "EMR", "ITW", "PH", "ROP", "FAST", "CMI",
    "T", "VZ", "TMUS", "DIS", "NFLX", "CHTR", "CMCSA", "ATVI", "EA", "TTWO",
    "SPOT", "RBLX", "DISCA", "FOX", "NWS", "DISH", "LYV", "ZG", "ZM", "DOCU",
    "LIN", "SHW", "APD", "ECL", "DD", "NEM", "FCX", "ALB", "PPG", "CTVA",
    "MLM", "VMC", "IFF", "AVY", "IP", "WRK", "PKG", "SEE", "CE", "CF",
    "AMT", "PLD", "CCI", "EQIX", "SPG", "DLR", "AVB", "EQR", "O", "PSA",
    "WELL", "ARE", "MAA", "ESS", "VTR", "SUI", "HST", "BXP", "EXR", "SBAC",
    "NEE", "DUK", "SO", "D", "EXC", "AEP", "SRE", "XEL", "ES", "PEG",
    "EIX", "FE", "WEC", "AWK", "ED", "PNW", "ATO", "NI", "CMS", "DTE",
    "META", "SNOW", "PLTR", "UBER", "LYFT", "SQ", "SHOP", "SE", "ROKU", "CRWD",
    "ZS", "DDOG", "PINS", "NET", "OKTA", "MDB", "TEAM", "TWLO", "ASAN", "SPLK",
    "BILL", "AFRM", "DOCS", "APPN", "PATH", "FSLY", "FVRR", "UPWK", "ETSY", "W",
    "RIVN", "LCID", "NKLA", "QS", "FSR", "BYND", "DNA", "BROS", "CELH", "TTCF"
]

new_stocks_list = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "ADBE", "INTC", "CSCO", 
    "CRM", "QCOM", "AVGO", "ORCL", "AMD", "IBM", "TXN", "PYPL", "NOW", "INTU", 
    "JNJ", "UNH", "PFE", "ABBV", "MRK", "TMO", "ABT", "DHR", "BMY", "LLY", 
    "CVS", "AMGN", "GILD", "REGN", "ISRG", "BIIB", "VRTX", "MDT", "ZTS", "SYK", 
    "JPM", "BAC", "WFC", "C", "GS", "MS", "BLK", "BK", "TROW", "SCHW", "AXP", 
    "COF", "DFS", "PNC", "USB", "TD", "BMO", "RY", "CB", "MMC", "PG", "KO", 
    "PEP", "PM", "MO", "CL", "KMB", "HSY", "EL", "MNST", "HD", "LOW", "NKE", 
    "TGT", "COST", "MCD", "SBUX", "TJX", "DG", "YUM", "XOM", "CVX", "SLB", 
    "COP", "EOG", "OXY", "PSX", "VLO", "MPC", "HES", "HAL", "BKR", "FANG", 
    "DVN", "APA", "LNG", "WMB", "KMI", "GE", "HON", "BA", "LMT", "RTX", "CAT", 
    "DE", "MMM", "UNP", "CSX", "NSC", "UPS", "FDX", "ETN", "EMR", "ITW", "PH", 
    "ROP", "FAST", "CMI", "T", "VZ", "TMUS", "DIS", "NFLX", "CHTR", "CMCSA", 
    "EA", "TTWO", "SPOT", "RBLX", "LYV", "ZG", "ZM", "DOCU", "LIN", "SHW", 
    "APD", "ECL", "DD", "NEM", "FCX", "ALB", "PPG", "CTVA", "MLM", "VMC", 
    "IFF", "AVY", "IP", "PKG", "SEE", "CE", "CF", "AMT", "PLD", "CCI", "EQIX", 
    "SPG", "DLR", "AVB", "EQR", "O", "PSA", "WELL", "ARE", "MAA", "ESS", 
    "VTR", "SUI", "HST", "BXP", "EXR", "SBAC", "NEE", "DUK", "SO", "D", 
    "EXC", "AEP", "SRE", "XEL", "ES", "PEG", "EIX", "FE", "WEC", "AWK", "ED", 
    "PNW", "ATO", "NI", "CMS", "DTE", "META", "SNOW", "PLTR", "UBER", "LYFT", 
    "SQ", "SHOP", "SE", "ROKU", "CRWD", "ZS", "DDOG", "PINS", "NET", "OKTA", 
    "MDB", "TEAM", "TWLO", "ASAN", "BILL", "AFRM", "DOCS", "APPN", "PATH", 
    "FSLY", "FVRR", "UPWK", "ETSY", "W", "RIVN", "LCID", "NKLA", "QS", "BYND", 
    "DNA", "BROS", "CELH"
]



def sustainability_data(stock_list):

    df = pd.DataFrame()
    for stock in stocks_list:
        try:
            stocky = yf.Ticker(stock)
            sustainability = stocky.sustainability
            df[stock] = sustainability
        except Exception as e:
         print(f"Fehler beim Laden der Daten für {stock}: {e}")
    print(df.head(10))

    df.to_excel("data.xlsx")


def history_data(stocks_list):
   
   end_date = datetime.today()
   start_date = end_date - timedelta(days = 3 * 365)

   df = pd.DataFrame()
   for stock in stocks_list:
     data = yf.download(stock, start = start_date, end = end_date)
     df[stock] = data["Close"]

   
   df.to_excel("data_history.xlsx")

history_data(new_stocks_list)

