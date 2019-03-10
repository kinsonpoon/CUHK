import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import seaborn
from sklearn.preprocessing import StandardScaler
seaborn.set()
from sklearn.model_selection import train_test_split

df = pd.read_csv('imports-85.data',
            header=None,
            names=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"],
                na_values=("?"))
list=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
#print (list)
#df.info()
#print (df.describe())
df=df.dropna()

#X_train,X_test = train_test_split(df, test_size=0.2,shuffle=False)
dfs = np.split(df, [32], axis=0)
X_train=dfs[1]
X_test=dfs[0]
#Y_train=X_train["price"]
#Y_test= X_test["price"]
#X_train=X_train.drop("price", axis = 1)
#X_test=X_test.drop("price", axis = 1)
#print("Number of training data:",len(X_train))
#print("Number of testing data:",len(X_test))
#print("Number of training data target:",len(Y_train))
#print("Number of testing data target:",len(Y_test))

X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train[["price","horsepower"]])
X_test = X_scaler.transform(X_test[["price","horsepower"]])

#print (X_train["price"])
#X_train.columns
#print(X_train)
#linear reg
#price:X_test[:,0]
#print(X_test[:,1])
xt=[X_train[:,1]]
xt=np.reshape(xt,(127,-1))
yt=[X_train[:,0]]
yt=np.reshape(yt,(127,-1))


model = linear_model.LinearRegression()
model.fit(xt,yt)
xp=[X_test[:,1]]
yp=[X_test[:,0]]
xp=np.reshape(xp,(32,-1))
yp=np.reshape(yp,(32,-1))
model_score = model.score(xp, yp)
#print(model_score)
#print(X_train[:,1])

#print([X_train[:,1]])
#print(train)
#print(train)
#plot

plt.scatter(xp,yp,  color='black')
plt.plot(xp, model.predict(xp), color='blue', linewidth=3)
plt.xlabel("Standardized horsepower")
plt.title("Linear regression on cleaned and standardized test data")
plt.ylabel("Standardized price")
plt.xticks(())
plt.yticks(())

plt.show()







