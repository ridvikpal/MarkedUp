from twelvedata import TDClient
import pandas as pd
import mplfinance as mpf

# td = TDClient(apikey="2d748ba087024b199c77cce35b2f8d78")

# time_series = td.time_series(
#     symbol="AAPL",
#     interval="1day",
#     outputsize=10,
#     timezone="America/New_York",
# )

# result = time_series.as_pandas()

# result.to_csv("test.csv", encoding="utf-8")

# print(result)

appleData = pd.read_csv("test.csv", encoding="utf-8", index_col=0)


appleData.index = pd.to_datetime(appleData.index)


# print(appleData.dtypes)
# print(appleData)

# print(appleData.index.month)

mpf.plot(appleData, type="candle")
