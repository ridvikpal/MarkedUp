'''
This file contains all functions that interact with the TwelveData API
for getting the stock data
'''

''' IMPORT MODULES '''
from twelvedata import TDClient
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
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

# this function will filter the data for a specific time
def filterTimeSeries(timeSeries: pd.DataFrame, timeFilter: str) -> pd.DataFrame:
    today = datetime.today().date()
    today = pd.Timestamp(today)
    # today = today.strftime("%Y-%m-%d")
    match timeFilter:
        case "1 month":
            one_month = datetime.today().date() + relativedelta(months=-1)
            one_month = pd.Timestamp(one_month)
            return timeSeries.loc[(timeSeries.index >= one_month) & (timeSeries.index <= today)]
        case "3 months":
            three_months = datetime.today().date() + relativedelta(months=-3)
            three_months = pd.Timestamp(three_months)
            return timeSeries.loc[(timeSeries.index >= three_months) & (timeSeries.index <= today)]
        case "6 months":
            six_months = datetime.today().date() + relativedelta(months=-6)
            six_months = pd.Timestamp(six_months)
            return timeSeries.loc[(timeSeries.index >= six_months) & (timeSeries.index <= today)]
        case "1 year":
            one_year = datetime.today().date() + relativedelta(years=-1)
            one_year = pd.Timestamp(one_year)
            return timeSeries.loc[(timeSeries.index >= one_year) & (timeSeries.index <= today)]
    return timeSeries

def createPlotlyGraph(timeSeries: pd.DataFrame, timeFrame: str) -> gpo.Figure:
    figure = sub.make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        subplot_titles=('Price', 'Volume'),
        row_heights=[0.8, 0.2]
    )

    figure.add_trace(
        gpo.Candlestick(
            x=timeSeries.index,
            open=timeSeries['open'],
            high=timeSeries['high'],
            low=timeSeries['low'],
            close=timeSeries['close'],
            name='Price'
        ),
        row=1,
        col=1
    )

    figure.add_trace(
        gpo.Bar(
            x=timeSeries.index,
            y=timeSeries['volume'],
            name='Volume'
            # showlegend=False
        ),
        row=2,
        col=1
    )

    figure.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=False
            ),
            type='date'
        )
    )

    return figure

# gets historical stock information and returns it as a plotly figure (ready to graph)
def getStockTimeSeriesGraph(symb: str) -> gpo.Figure:
    time_series = td.time_series(
        symbol=symb,
        interval="1day",
        outputsize=2000,
        end_date=datetime.today(),
        start_date=datetime(2000, 1, 1)
    )

    figure = time_series.as_plotly_figure()
    figure.update_layout(
        title_text=None,
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
        )
    )
    return figure

# gets historical stock information and returns it as a plotly figure (ready to graph)
def getStockTimeSeries(symb: str, oneYear: bool = True) -> pd.DataFrame:
    time_series = td.time_series(
        symbol=symb,
        interval="1day",
        outputsize=2000,
        end_date=datetime.today(),
        start_date=datetime(2000, 1, 1)
    )
    return time_series.as_pandas()

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