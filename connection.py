'''
This file contains all functions that interact with the TwelveData API
for getting the stock data
'''

''' IMPORT MODULES '''
from twelvedata import TDClient
import pandas as pd
from datetime import datetime
import json
import plotly.subplots as sub
import plotly.graph_objects as gpo
import pandas as pd

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
def getStockTimeSeriesGraph(symb: str, oneYear: bool = True) -> pd.DataFrame:
    if oneYear: # get data for 5 years
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

# gets historical stock information and returns it as a plotly figure (ready to graph)
def getStockTimeSeries(symb: str, oneYear: bool = True) -> pd.DataFrame:
    if oneYear: # get data for 5 years
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
    return time_series.as_pandas()

def createPlotlyGraph(time_series: pd.DataFrame) -> gpo.Figure:
    # we want to plot volume and stock price, so we need two rows
    figure = sub.make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        row_heights=[0.8, 0.2],
        vertical_spacing=0.02
    )

    # add the candlestick chart with the price information
    figure.add_trace(
        gpo.Candlestick(
            x=time_series.index,
            open=time_series['open'],
            high=time_series['high'],
            low=time_series['low'],
            close=time_series['close'],
            name="Price"
        ),
        row=1,
        col=1
    )

    # add the volume chart with the volume information
    figure.add_trace(
        gpo.Bar(
            x=time_series.index,
            y=time_series['volume'],
            name="Volume"
        ),
        row=2,
        col=1
    )

    # update the layout for formatting purposes
    figure.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                        label="1 Month",
                        step="month",
                        stepmode="backward"),
                    dict(count=3,
                         label="3 Months",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                        label="6 Months",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="Year-To-Day",
                        step="year",
                        stepmode="todate"),
                    dict(count=1,
                        label="1 Year",
                        step="year",
                        stepmode="backward"),
                    dict(label="5 Years",
                        step="all")
                ])
            ),
            rangeslider=dict(
                visible=False
            ),
            type="date"
        ),
        # yaxis1_title="Stock Price",
        # yaxis2_title="Volume (M)",
        # xaxis2_title="Time",
        # xaxis1_rangeslider_visible = False,
        # xaxis2_rangeslider_visible = True
    )


    return figure

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
    return float(price['price'])

# get the company logo for a specific stock
def getStockLogo(symb: str) -> str:
    imageURL = td.get_logo(symbol=symb)
    imageURL = imageURL.as_json()
    return imageURL['url']