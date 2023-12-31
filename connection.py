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
import plotly.offline
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
def update_stocks_list() -> None:
    with open("all_stocks.json", "w") as f:
        all_stocks = td.get_stocks_list().as_json()
        json.dump(all_stocks, indent=4, fp=f)

# this function will filter the data for a specific time
def filterTimeSeries(timeSeries: pd.DataFrame, timeFilter: str = None) -> pd.DataFrame:
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

# create a plotly graph from a timeseries
def createPlotlyGraph(timeSeries: pd.DataFrame) -> tuple:
    figure = sub.make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.01,
        # subplot_titles=('Price', 'Volume'),
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

    dark_figure = gpo.Figure(figure)

    dark_figure.update_layout(
        template='plotly_dark'
    )

    return figure, dark_figure

# export the filtered time series graph to an html file
def exportFilteredTimeSeriesGraph(timeSeries: pd.DataFrame, timeFilter: str = None) -> None:
    filteredTS = filterTimeSeries(timeSeries, timeFilter)
    figures = createPlotlyGraph(filteredTS)
    if timeFilter:
        plotly.offline.plot(figures[0], filename=(timeFilter + ".html"), auto_open=False)
        plotly.offline.plot(figures[1], filename=(timeFilter + "_dark" + ".html"), auto_open=False)
    else:
        plotly.offline.plot(figures[0], filename="5 years.html", auto_open=False)
        plotly.offline.plot(figures[1], filename="5 years_dark.html", auto_open=False)

# gets historical stock information and returns it as a plotly figure (ready to graph)
def getStockTimeSeries(symb: str) -> pd.DataFrame:
    time_series = td.time_series(
        symbol=symb,
        interval="1day",
        outputsize=2000
    )
    return time_series.as_pandas()

def getStocksList() -> list:
    df = pd.read_json("all_stocks.json")
    df.drop(['currency', 'exchange', 'mic_code', 'type', 'country'], axis=1, inplace=True)
    df.drop_duplicates(subset='symbol', inplace=True)
    df['autocomplete_name'] = df[['name', 'symbol']].agg(' - '.join, axis=1)
    df.drop(['symbol', 'name'], axis=1, inplace=True)
    df.sort_values(by=['autocomplete_name'], inplace=True)
    returnList = df.to_numpy().flatten().tolist()
    return returnList


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