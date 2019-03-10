# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 12:52:33 2018

@author: kinghin
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import io
from sklearn.naive_bayes import MultinomialNB
import seaborn; seaborn.set()

rawdata=io.loadmat('train.mat')
#print(io.whosmat("train.mat"))
#print(rawdata.keys())
#print(rawdata.values())
#print(rawdata[__header__])
#print(rawdata[__version__])
#print(rawdata[__globals__])
#print(type(rawdata))
#print(rawdata['Xtrain'])
#print(rawdata['ytrain'])
print("n_features=",len(rawdata['Xtrain'][0]))
print("n_samples=",len(rawdata['ytrain']))
X=rawdata['Xtrain']
y=rawdata['ytrain'].ravel()
model = MultinomialNB()
model.fit(X, y)
predit=model.predict(X)
print("The accuracy of the classifier:","%.2f" % ((1-(y != predit).sum()/6665) *100),"%","(corr to 2dp)")

testdata=io.loadmat('test.mat')
#print(io.whosmat("test.mat"))
test=testdata['Xtest']
output=model.predict(test)
#print(output.astype(int))
np.savetxt('prediction.txt',output.astype(int), fmt='%i')