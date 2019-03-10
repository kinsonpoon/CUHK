import os.path
import numpy as np
import matplotlib.pyplot as plt
import scipy as spy
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import math

input_file = "training.csv"
input_file2 = "testing.csv"
train_data = pd.read_csv(input_file, header = 0)
test_data = pd.read_csv(input_file2, header = 0)
#print(train_data.keys())

feature=['actual_weight', 'declared_horse_weight','race_distance', 'trainer_ave_rank', 'jockey_ave_rank','recent_ave_rank','draw','win_odds']
goal="finish_time"
#svm
#first prepare the data
#convert the time to mini second
time_train=train_data[goal]
time_test=test_data[goal]
#
Y_train_t=[]
Y_train=[]
Y_test_t=[]
Y_test=[]
for item in time_train:
    time=0
    time=int(item[0])*3600+(int(item[2])*10+int(item[3]))*60+int(item[5])*10+int(item[6])
    Y_train_t.append([time])
    Y_train.append(time)
for item in time_test:
    time=0
    time=int(item[0])*3600+(int(item[2])*10+int(item[3]))*60+int(item[5])*10+int(item[6])
    Y_test_t.append([time])
    Y_test.append(time)
#standardlize the data
X_scaler = StandardScaler()
std_matrix_train= X_scaler.fit_transform(train_data[feature])
std_matrix_test= X_scaler.fit_transform(test_data[feature])
std_Y_train=X_scaler.fit_transform(Y_train_t)
std_Y_test= X_scaler.fit_transform(Y_test_t) 

#matrix
matrix_train=[]
matrix_test=[]
#print(len(train_data[goal]))
#print(len(test_data[goal]))
for i in range(len(train_data[goal])):
    temp=[]
    for features in feature:
        temp.append(train_data[features][i])
    matrix_train.append(temp)
    
for i in range(len(test_data[goal])):
    temp=[]
    for features in feature:
        temp.append(test_data[features][i])
    matrix_test.append(temp)
#build the model
#svr_model=SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.2, gamma='auto',
#    kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
#svr_model.fit(matrix_train,Y_train)
#mse = mean_squared_error(Y_test, svr_model.predict(matrix_test))
#print("without normalization SMSE: %.4f" % math.sqrt(mse))
#svr_model_score=svr_model.score(matrix_test,Y_test)

#
svr_model=SVR(C=100.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.5, gamma='auto',
    kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
svr_model.fit(std_matrix_train,Y_train)
mse = mean_squared_error(Y_test, svr_model.predict(std_matrix_test))
svr_rmse=math.sqrt(mse)
svr_pred_list=svr_model.predict(std_matrix_test)
df=[('svr_pred_list',svr_pred_list)]
df = pd.DataFrame.from_items(df)
df.to_csv("svr_pred_list.csv", encoding='utf-8', index=False)
#svr_model_score=svr_model.score(std_matrix_test,std_Y_test)
#print(svr_model_score)
#

#Gradient Boosting Regression Tree Model(GBRT)
params = {'n_estimators': 500, 'max_depth': 8, 'min_samples_split': 2,
          'learning_rate': 0.05, 'loss': 'ls'}
#
#gbrt_model = GradientBoostingRegressor(**params)
#
#gbrt_model.fit(matrix_train,Y_train)
#mse = mean_squared_error(Y_test, gbrt_model.predict(matrix_test))
#print("without normalization SMSE: %.4f" % math.sqrt(mse))
#gbrt_score=gbrt_model.score(std_matrix_test,std_Y_test)
#print(gbrt_score)
#
gbrt_model = GradientBoostingRegressor(**params)

gbrt_model.fit(std_matrix_train,Y_train)
mse = mean_squared_error(Y_test, gbrt_model.predict(std_matrix_test))
gbrt_rmse=math.sqrt(mse)
gbrt_pred_list=gbrt_model.predict(std_matrix_test)
df=[('gbrt_pred_list',gbrt_pred_list)]
df = pd.DataFrame.from_items(df)
df.to_csv("gbrt_pred_list.csv", encoding='utf-8', index=False)
#gbrt_score=gbrt_model.score(std_matrix_test,std_Y_test)
#print(gbrt_score)
#calculate of the predit data
all=480
dict={}
Top_1=0
Top_3=0

for i in range(len(test_data['race_id'])-1):
    id=test_data['race_id'][i]
    dict[svr_pred_list[i]]=i
    if(int(test_data['finishing_position'][i])==1):
        first=i
    if(int(test_data['finishing_position'][i])==2):
        second=i
    if(int(test_data['finishing_position'][i])==3):
        third=i
    if(id!=test_data['race_id'][i+1]):
        Min=min(dict.keys())
        if(dict[Min]==first):
            Top_1+=1
            Top_3+=1
        elif(dict[Min]==second or dict[Min]==third):
            Top_3+=1
             
        dict={}
print("svr_model",svr_rmse,Top_1/all,Top_3/all,Top_1+Top_3)
#
dict={}
Top_1=0
Top_3=0

for i in range(len(test_data['race_id'])-1):
    id=test_data['race_id'][i]
    dict[gbrt_pred_list[i]]=i
    if(int(test_data['finishing_position'][i])==1):
        first=i
    if(int(test_data['finishing_position'][i])==2):
        second=i
    if(int(test_data['finishing_position'][i])==3):
        third=i
    if(id!=test_data['race_id'][i+1]):
        Min=min(dict.keys())
        if(dict[Min]==first):
            Top_1+=1
            Top_3+=1
        elif(dict[Min]==second or dict[Min]==third):
            Top_3+=1
             
        dict={}
print("gbrt_model",gbrt_rmse,Top_1/all,Top_3/all,Top_1+Top_3)
































