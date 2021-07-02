import datetime as period
from matplotlib import style
import pandas_datareader.data as net
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as mlp

style.use('bmh')

start=period.datetime(2020,1,1)
end=period.datetime(2020,11,11)

dataframe=net.DataReader('AAPL','yahoo',start,end)

days=60
dataframe['Prediction']=dataframe[['Close']].shift(-days)
print(dataframe.head())
print()

ndf=dataframe['Close']
print(ndf.head())
print()

X=np.array(dataframe.drop(['Prediction'],1))[:-days]

Y=np.array(dataframe['Prediction'])[:-days]

X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.25)

tree=DecisionTreeRegressor().fit(X_train,Y_train)

X_future=dataframe.drop(['Prediction'],1)[:-days]
X_future=X_future.tail(days)
X_future=np.array(X_future)
print(X_future)
print()

tree_prediction=tree.predict(X_future)
print(tree_prediction)
print()

result=tree_prediction

vdata=dataframe[X.shape[0]:]
vdata['Prediction']=result

mlp.title('Apple')
mlp.ylabel('Close Price in USD($)')
mlp.plot(dataframe['Close'])
mlp.plot(vdata[['Close','Prediction']])
mlp.legend(['Original Prices','Actual Prices','Predicted Prices'])
mlp.show()