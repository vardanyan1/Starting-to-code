# -*- coding: utf-8 -*-
"""Stock_1 start.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lmYPk4OsKUg19LwKlcWNTGvpL9Yy0OUf
"""

!pip install https://github.com/matplotlib/mpl_finance/archive/master.zip

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from google.colab import files
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()


df = web.get_data_yahoo('TSLA', start, end)

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

#df.to_csv('tsla.csv')
# files.download('tsla.csv')

# df['Adj Close'].plot()

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])

ax2.bar(df.index, df['Volume'])

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df.dropna(inplace=True)
df.head()

df_ohlc = df['Adj Close'].resample('10D').ohlc()   # Open High Low Close
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1, sharex=ax1)

ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)



