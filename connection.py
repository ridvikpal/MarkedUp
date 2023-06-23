from twelvedata import TDClient
import pandas as pd
import mplfinance as mpf
from datetime import datetime
import json

td = TDClient(apikey="2d748ba087024b199c77cce35b2f8d78")

# this function updates the stock json list and stores it in the application
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
    return all_stocks

# gets stock information and returns it as a dataframe
def getStockTimeSeries() -> pd.DataFrame:
    pass

def main() -> None:
    all_stocks = update_stocks_list()
    for x in all_stocks:
        # print(x['symbol'])
        print(x['symbol'])

if __name__ == "__main__":
    main()

# time_series = td.time_series(
#     symbol="AAPL",
#     interval="1day",
#     outputsize=2000,
#     end_date=datetime.today(),
#     start_date=datetime(2000, 1, 1),
#     timezone="America/New_York",
# )

# appleData = time_series.as_pandas()

# # result.to_csv("test.csv", encoding="utf-8")

# appleData = appleData.reindex(index=appleData.index[::-1])

# print(appleData)
# time_series.as_pyplot_figure().show()

# appleData = pd.read_csv("test.csv", encoding="utf-8", index_col=0)


# appleData.index = pd.to_datetime(appleData.index)


# print(appleData.dtypes)
# print(appleData)

# print(appleData.index.month)

# mpf.plot(appleData, type="candle")