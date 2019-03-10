import os.path
import numpy as np
import matplotlib.pyplot as plt
import scipy as spy
import pandas as pd
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import timeit

input_file = "training.csv"
input_file2 = "testing.csv"
train_data = pd.read_csv(input_file, header = 0)
test_data = pd.read_csv(input_file2, header = 0)
#print(train_data.keys())
kfold = KFold(n_splits=10)
feature=['actual_weight', 'declared_horse_weight','race_distance', 'trainer_ave_rank', 'jockey_ave_rank','recent_ave_rank','draw','win_odds']
feature_nb=['actual_weight', 'declared_horse_weight','race_distance', 'trainer_ave_rank', 'jockey_ave_rank','recent_ave_rank']
goal='finishing_position'
#1 to yes,0 to no
#
HorseWin_train=[]
HorseWin_test=[]
#
HorseRankTop3_train=[]
HorseRankTop3_test=[]
#
HorseRankTop50Percent_train=[]
HorseRankTop50Percent_test=[]
#
for item in train_data[goal]:
    if int(item)<=3:
        HorseRankTop3_train.append("1")
    else:
        HorseRankTop3_train.append("0")
    if int(item)==1:
        HorseWin_train.append("1")
    else:
        HorseWin_train.append("0")
    if int(item)<=7:
        HorseRankTop50Percent_train.append("1")
    else:
        HorseRankTop50Percent_train.append("0")
#
for item in test_data[goal]:
    if int(item)<=3:
        HorseRankTop3_test.append("1")
    else:
        HorseRankTop3_test.append("0")
    if int(item)==1:
        HorseWin_test.append("1")
    else:
        HorseWin_test.append("0")
    if int(item)<=7:
        HorseRankTop50Percent_test.append("1")
    else:
        HorseRankTop50Percent_test.append("0")
#


X_train= train_data[feature]
X_test= test_data[feature]
#X_train = train_data[feature]
#X_test  = test_data[feature]
lr_predict = []
rid=[]
for item in test_data['race_id']:
    rid.append(item)
hid=[]
for item in test_data['horse_id']:
    hid.append(item)
lr_predict.append(rid)
lr_predict.append(hid)

start_time = timeit.default_timer()

win_lr_model=linear_model.LogisticRegression()
win_lr_model.fit(X_train[:100],HorseWin_train[:100])
win_lr_predict = win_lr_model.predict(X_test)

#
lr_predict.append(win_lr_predict)
lr_model_score = win_lr_model.score(X_test, HorseWin_test)
tn, fp, fn, tp = confusion_matrix(HorseWin_test, win_lr_predict).ravel()
#print (tn, fp, fn, tp)
print("Win")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))


top3_lr_model=linear_model.LogisticRegression()
top3_lr_model.fit(X_train,HorseRankTop3_train)
top3_lr_predict = top3_lr_model.predict(X_test)
lr_predict.append(top3_lr_predict)
lr_model_score = top3_lr_model.score(X_test, HorseRankTop3_test)
tn, fp, fn, tp = confusion_matrix(HorseRankTop3_test, top3_lr_predict).ravel()
#print (tn, fp, fn, tp)
print("Top3")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))
#print("top3 Logistic Regression score:",lr_model_score)

fifty_lr_model=linear_model.LogisticRegression()
fifty_lr_model.fit(X_train,HorseRankTop50Percent_train)
fifty_lr_predict = fifty_lr_model.predict(X_test)
lr_predict.append(fifty_lr_predict)
lr_model_score = fifty_lr_model.score(X_test, HorseRankTop50Percent_test)
tn, fp, fn, tp = confusion_matrix(HorseRankTop50Percent_test, fifty_lr_predict).ravel()
#print (tn, fp, fn, tp)
print("50%")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))
#print("50% Logistic Regression score:",lr_model_score)

df=[('RaceID',lr_predict[0]),('HorseID',lr_predict[1]),
    ('HorseWin',lr_predict[2]),('HorseRankTop3',lr_predict[3]),
    ('HorseRankTop50Percent',lr_predict[4])]

df_lr=pd.DataFrame.from_items(df)
df_lr.to_csv("lr_predictions2.csv", encoding='utf-8', index=False)
stop = timeit.default_timer()
print("Running time: %s seconds" % (stop - start_time))

##sklearn naive b
start_time = timeit.default_timer()
X_train_nb = train_data[feature_nb]
X_test_nb  = test_data[feature_nb]

nb_predict = []
rid=[]
for item in test_data['race_id']:
    rid.append(item)
hid=[]
for item in test_data['horse_id']:
    hid.append(item)
nb_predict.append(rid)
nb_predict.append(hid)

win_nb_model=GaussianNB()
win_nb_model.fit(X_train_nb[:100],HorseWin_train[:100])
win_nb_predict = win_nb_model.predict(X_test_nb)
nb_predict.append(win_nb_predict)
nb_model_score = win_nb_model.score(X_test_nb, HorseWin_test)
tn, fp, fn, tp = confusion_matrix(HorseWin_test, win_nb_predict).ravel()
#print (tn, fp, fn, tp)
#print("win sk_learn nb_model score:",nb_model_score)
print("Win")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))
#
top3_nb_model=GaussianNB()
top3_nb_model.fit(X_train_nb,HorseRankTop3_train)
top3_nb_predict = top3_nb_model.predict(X_test_nb)
nb_predict.append(top3_nb_predict)
nb_model_score = top3_nb_model.score(X_test_nb, HorseRankTop3_test)
tn, fp, fn, tp = confusion_matrix(HorseRankTop3_test, top3_nb_predict).ravel()
#print (tn, fp, fn, tp)
#print("top3 sk_learn nb_model score:",nb_model_score)
print("Top3")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))
#
fifty_nb_model=GaussianNB()
fifty_nb_model.fit(X_train_nb,HorseRankTop50Percent_train)
fifty_nb_predict = top3_nb_model.predict(X_test_nb)
nb_predict.append(fifty_nb_predict)
nb_model_score = fifty_nb_model.score(X_test_nb, HorseRankTop50Percent_test)
tn, fp, fn, tp = confusion_matrix(HorseRankTop50Percent_test, fifty_nb_predict).ravel()
#print (tn, fp, fn, tp)
#print("50% sk_learn nb_model score:",nb_model_score)
print("50%")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))
#

df=[('RaceID',nb_predict[0]),('HorseID',nb_predict[1]),
    ('HorseWin',nb_predict[2]),('HorseRankTop3',nb_predict[3]),
    ('HorseRankTop50Percent',nb_predict[4])]

df_nb=pd.DataFrame.from_items(df)
df_nb.to_csv("nb_predictions2.csv", encoding='utf-8', index=False)

stop = timeit.default_timer()
print("Running time: %s seconds" % (stop - start_time))
##my naive b



#svm
#first prepare the data
start_time = timeit.default_timer()
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
svm_predict = []
rid=[]
for item in test_data['race_id']:
    rid.append(item)
hid=[]
for item in test_data['horse_id']:
    hid.append(item)
svm_predict.append(rid)
svm_predict.append(hid)

win_svm_model = SVC(kernel='linear',C=100)
win_svm_model.fit(matrix_train[:35],HorseWin_train[:35])
win_svm_predict = win_svm_model.predict(matrix_test)
svm_predict.append(win_svm_predict)
svm_model_score = win_svm_model.score(matrix_test, HorseWin_test)
tn, fp, fn, tp = confusion_matrix(HorseWin_test, win_svm_predict).ravel()
print("Win")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))
#print (tn, fp, fn, tp)
#print("win svm_model_score: ",svm_model_score)

top3_svm_model = SVC(kernel='rbf',C=0.7)
top3_svm_model.fit(matrix_train,HorseRankTop3_train)
top3_svm_predict = top3_svm_model.predict(matrix_test)
svm_predict.append(top3_svm_predict)
svm_model_score = top3_svm_model.score(matrix_test, HorseRankTop3_test)
tn, fp, fn, tp = confusion_matrix(HorseRankTop3_test, top3_svm_predict).ravel()
print("Top3")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))
#print (tn, fp, fn, tp)
#print("top3 svm_model_score: ",svm_model_score)

fifty_svm_model = SVC(kernel='rbf',C=0.7)
fifty_svm_model.fit(matrix_train,HorseRankTop50Percent_train)
fifty_svm_predict = fifty_svm_model.predict(matrix_test)
svm_predict.append(fifty_svm_predict)
svm_model_score = fifty_svm_model.score(matrix_test, HorseRankTop50Percent_test)
tn, fp, fn, tp = confusion_matrix(HorseRankTop50Percent_test, fifty_svm_predict).ravel()
print("50%")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))
#print (tn, fp, fn, tp)
#print("50% svm_model_score: ",svm_model_score)

df=[('RaceID',svm_predict[0]),('HorseID',svm_predict[1]),
    ('HorseWin',svm_predict[2]),('HorseRankTop3',svm_predict[3]),
    ('HorseRankTop50Percent',svm_predict[4])]

df_svm=pd.DataFrame.from_items(df)
df_svm.to_csv("svm_predictions2.csv", encoding='utf-8', index=False)

stop = timeit.default_timer()
print("Running time: %s seconds" % (stop - start_time))

#rf
start_time = timeit.default_timer()
rf_predict = []
rid=[]
for item in test_data['race_id']:
    rid.append(item)
hid=[]
for item in test_data['horse_id']:
    hid.append(item)
rf_predict.append(rid)
rf_predict.append(hid)

win_rf_model = RandomForestClassifier(n_estimators=50,random_state=123456)
win_rf_model.fit(X_train, HorseRankTop3_train)
win_rf_predict = win_rf_model.predict(X_test)
rf_predict.append(win_rf_predict)
rf_model_score = win_rf_model.score(X_test, HorseWin_test)
tn, fp, fn, tp = confusion_matrix(HorseWin_test, win_rf_predict).ravel()
print("Win")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))
#print (tn, fp, fn, tp)
#print("win rf_model_score: ",rf_model_score)

top3_rf_model = RandomForestClassifier(n_estimators=100,random_state=123456)
top3_rf_model.fit(X_train, HorseRankTop3_train)
top3_rf_predict = top3_rf_model.predict(X_test)
rf_predict.append(top3_rf_predict)
rf_model_score = top3_rf_model.score(X_test, HorseRankTop3_test)
tn, fp, fn, tp = confusion_matrix(HorseRankTop3_test, top3_rf_predict).ravel()
print("Top3")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))
#print (tn, fp, fn, tp)
#print("top3 rf_model_score: ",rf_model_score)

fifty_rf_model = RandomForestClassifier(n_estimators=100,random_state=123456)
fifty_rf_model.fit(X_train, HorseRankTop3_train)
fifty_rf_predict = fifty_rf_model.predict(X_test)
rf_predict.append(fifty_rf_predict)
rf_model_score = fifty_rf_model.score(X_test, HorseRankTop50Percent_test)
tn, fp, fn, tp = confusion_matrix(HorseRankTop50Percent_test, fifty_rf_predict).ravel()
print("50%")
print("R: ",max(0,tp/(tp+fn)))
print("P: ",max(0,tp/(tp+fp)))
#print (tn, fp, fn, tp)
#print("50% rf_model_score: ",rf_model_score)

df=[('RaceID',rf_predict[0]),('HorseID',rf_predict[1]),
    ('HorseWin',rf_predict[2]),('HorseRankTop3',rf_predict[3]),
    ('HorseRankTop50Percent',rf_predict[4])]

df_nb=pd.DataFrame.from_items(df)
df_nb.to_csv("rf_predictions2.csv", encoding='utf-8', index=False)

stop = timeit.default_timer()
print("Running time: %s seconds" % (stop - start_time))


 