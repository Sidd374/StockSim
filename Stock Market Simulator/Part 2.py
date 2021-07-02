import datetime as period
import matplotlib.pyplot as mpl
from matplotlib import style
import pandas as pd
import pandas_datareader.data as net

style.use('ggplot')

start=period.datetime(2020,1,1)
end=period.datetime(2020,11,11)

dataframe=net.DataReader('AAPL','yahoo',start,end)

#df.to_csv('Stock history'.csv')
#df=pd.read_csv('Stock history.csv',parse_dates=True,index_col=0)

dataframe['100ma']=dataframe['Adj Close'].rolling(window=100,min_periods=0).mean()
print(dataframe.tail(10))

ax1=mpl.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2=mpl.subplot2grid((6,1),(5,0),rowspan=5,colspan=1,sharex=ax1)

ax1.plot(dataframe.index,dataframe['100ma'])
ax1.plot(dataframe.index,dataframe['Adj Close'])
ax2.bar(dataframe.index,dataframe['Volume'])

mpl.show()