import datetime as period
import matplotlib.pyplot as mpl
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mplperiod
import pandas_datareader.data as net

style.use('bmh')

start=period.datetime(2020,1,1)
end=period.datetime(2020,11,11)

dataframe=net.DataReader('AAPL','yahoo',start,end)

dataframe_ohlc=dataframe['Adj Close'].resample('7D').ohlc()
dataframe_volume=dataframe['Volume'].resample('7D').sum()
print(dataframe_ohlc.head())

dataframe_ohlc.reset_index(inplace=True)
dataframe_ohlc['Date']=dataframe_ohlc['Date'].map(mplperiod.date2num)

ax1=mpl.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax1.xaxis_date()

candlestick_ohlc(ax1,dataframe_ohlc.values,width=2,colorup='g')

mpl.show()
