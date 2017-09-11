"""
Extract data from various Internet sources into a pandas DataFrame.
"""
import datetime as dt
import pandas_datareader.data as web

start = dt.datetime(2017, 1, 1)  # dt.datetime(Y, M, D)
end = dt.datetime(2017, 9, 10)
df = web.DataReader('KRX:KOSPI', 'google', start, end)  # web.DataReader("stock_code", "source", start_date, end_date)

print(df.head())
print(len(df))
