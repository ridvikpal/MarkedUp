'''
This file contains all functions that interact with the TwelveData API
for getting the stock data
'''

''' IMPORT MODULES '''
from twelvedata import TDClient
import pandas as pd
from datetime import datetime
import json
import plotly.graph_objects as gpo

''' CREATE GLOBAL TDCLIENT OBJECT '''
# allows data from TwelveData API
td = TDClient(apikey="2d748ba087024b199c77cce35b2f8d78")

''' FUNCTION DEFINITIONS '''
# this function updates the stock json list and then returns the data as a dataframe
""" The information is stored as:
    "symbol",
    "name",
    "currency",
    "exchange",
    "mic_code",
    "country",
    "type"
"""
def update_stocks_list() -> pd.DataFrame:
    # with open("all_stocks.json", "w") as f:
        # all_stocks = td.get_stocks_list().as_json()
        # json.dump(all_stocks, indent=4, fp=f)
    df = pd.read_json("all_stocks.json")
    return df

# gets historical stock information and returns it as a plotly figure (ready to graph)
def getStockTimeSeriesGraph(symb: str, fiveYear: bool = False) -> gpo.Figure:
    if fiveYear: # get data for 5 years
        time_series = td.time_series(
            symbol=symb,
            interval="1day",
            outputsize=2000,
            end_date=datetime.today(),
            start_date=datetime(2000, 1, 1)
        )
    else: # get data for a month
        time_series = td.time_series(
            symbol=symb,
            interval="1day",
            outputsize=30,
            end_date=datetime.today(),
            start_date=datetime(2000, 1, 1)
        )
    return time_series.as_plotly_figure()

# lookup from the dataframe for a specific stock from partial name
def getStockInformation(partialName: str, country: str, df: pd.DataFrame) -> pd.DataFrame:
    row = df[(df['name'].str.contains(pat=partialName, case=False)) & (df['country'] == country)]
    return row

# get a trading style quote for a specific stock
def getStockQuote(symb: str) -> pd.DataFrame:
    stockQuote = td.quote(
        symbol=symb,
        interval="5min"
    )
    return stockQuote.as_pandas()

# gets the live price for a specific stock
def getLivePrice(symb: str) -> float:
    price = td.price(symbol=symb).as_json()
    return price['price']

# get the company logo for a specific stock
def getStockLogo(symb: str) -> str:
    imageURL = td.get_logo(symbol=symb)
    imageURL = imageURL.as_json()
    return imageURL['url']