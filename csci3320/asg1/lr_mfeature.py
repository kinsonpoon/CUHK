import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import seaborn
from sklearn.preprocessing import StandardScaler

seaborn.set()

df = pd.read_csv('imports-85.data',
            header=None,
            names=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"],
                na_values=("?"))
df=df.dropna()
X_train=df
#print("Number of training data:",len(X_train))
X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(df[["horsepower","engine-size","peak-rpm"]])
Y_target=X_scaler.fit_transform(df[["price"]])
#print("Number of training data:",len(X_train))
#print("Number of target data:",len(Y_target))

#print(X_train)
#print(Y_target)
model = linear_model.LinearRegression()
model.fit(X_train,Y_target)

xTx = X_train.T.dot(X_train)
XtX = np.linalg.inv(xTx)
XtX_xT = XtX.dot(X_train.T)
theta = XtX_xT.dot(Y_target)
printline="("+str(theta[0][0])+","+str(theta[1][0])+","+str(theta[2][0])+")"
print("Parameter theta calculated by normal equation:"+printline)




sgd = linear_model.SGDRegressor(max_iter=100)
sgd=sgd.fit(X_train,Y_target.ravel())
#print(sgd.n_iter_)
#print(sgd.intercept_)

printline2="("+str(float(sgd.coef_[0]))+","+str(float(sgd.coef_[1]))+","+str(float(sgd.coef_[2]))+")"
print("Parameter theta calculated by SGD:"+printline2)