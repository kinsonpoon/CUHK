import os.path
import numpy as np
import matplotlib.pyplot as plt
import scipy as spy
import pandas as pd
from random import shuffle
print("Regression(normalization)")
input_file = "testing.csv"
svr = pd.read_csv("svr_pred_list.csv", header = 0)
gbrt = pd.read_csv("gbrt_pred_list.csv", header = 0)
result = pd.read_csv(input_file, header = 0)
#
list=[]
time=[]
count=0
total=0
for i in range(len(svr['svr_pred_list'])-1):
    list.append(i)
    id=result['race_id'][i]
    if(id !=result['race_id'][i+1]):
        for num in list:
            time.append(svr['svr_pred_list'][num])
        for i in range(len(time)-1):
            for j in range(i,len(time)):
                if(time[i]>time[j]):
                    time[i],time[j]=time[j],time[i]
                    list[i],list[j]=list[j],list[i]
        if(result['win_odds'][list[0]]>=4 and result['win_odds'][list[0]]<=30 and time[1]-time[0]>40 and result['jockey_ave_rank'][list[0]]<=8 and result['trainer_ave_rank'][list[0]]<=8):
            if(result['finishing_position'][list[0]]==1):
                count+=result['win_odds'][list[0]]
            else:
                count=count-1

        time=[]
        list=[]
total+=count
print("svr income: ",count)
#
list=[]
time=[]
count=0
for i in range(len(gbrt['gbrt_pred_list'])-1):
    list.append(i)
    id=result['race_id'][i]
    if(id !=result['race_id'][i+1]):
        for num in list:
            time.append(gbrt['gbrt_pred_list'][num])
        for i in range(len(time)-1):
            for j in range(i,len(time)):
                if(time[i]>time[j]):
                    time[i],time[j]=time[j],time[i]
                    list[i],list[j]=list[j],list[i]
        if(result['win_odds'][list[0]]>=4 and result['win_odds'][list[0]]<=30 and (time[1]-time[0])>=30 and result['jockey_ave_rank'][list[0]]<=9 and result['trainer_ave_rank'][list[0]]<=9):
            if(result['finishing_position'][list[0]]==1):
                count+=result['win_odds'][list[0]]
            else:
                count=count-1

        time=[]
        list=[]
total+=count
print("gbrt income: ",count)
#
count=0
print("Regression(Without normalization)")
input_file = "testing.csv"
svr = pd.read_csv("svr_pred_list2.csv", header = 0)
gbrt = pd.read_csv("gbrt_pred_list2.csv", header = 0)
result = pd.read_csv(input_file, header = 0)
#
list=[]
time=[]

for i in range(len(svr['svr_pred_list'])-1):
    list.append(i)
    id=result['race_id'][i]
    if(id !=result['race_id'][i+1]):
        for num in list:
            time.append(svr['svr_pred_list'][num])
        for i in range(len(time)-1):
            for j in range(i,len(time)):
                if(time[i]>time[j]):
                    time[i],time[j]=time[j],time[i]
                    list[i],list[j]=list[j],list[i]
        if(result['win_odds'][list[0]]>=4 and result['win_odds'][list[0]]<=30 and time[1]-time[0]>40 and result['jockey_ave_rank'][list[0]]<=8 and result['trainer_ave_rank'][list[0]]<=8):
            if(result['finishing_position'][list[0]]==1):
                count+=result['win_odds'][list[0]]
            else:
                count=count-1

        time=[]
        list=[]
print("svr income: ",count)
#
total+=count
count=0
list=[]
time=[]

for i in range(len(gbrt['gbrt_pred_list'])-1):
    list.append(i)
    id=result['race_id'][i]
    if(id !=result['race_id'][i+1]):
        for num in list:
            time.append(gbrt['gbrt_pred_list'][num])
        for i in range(len(time)-1):
            for j in range(i,len(time)):
                if(time[i]>time[j]):
                    time[i],time[j]=time[j],time[i]
                    list[i],list[j]=list[j],list[i]
        if(result['win_odds'][list[0]]>=4 and result['win_odds'][list[0]]<=30 and (time[1]-time[0])>=20 and result['jockey_ave_rank'][list[0]]<=9 and result['trainer_ave_rank'][list[0]]<=9):
            if(result['finishing_position'][list[0]]==1):
                count+=result['win_odds'][list[0]]
            else:
                count=count-1

        time=[]
        list=[]
print("gbrt income: ",count)
#lr_predictions.csv = noramlized,lr_predictions2.csv=without noramlized
total+=count
count=0
input_file = "lr_predictions2.csv"
input_file2 = "testing.csv"
pred = pd.read_csv(input_file, header = 0)
result = pd.read_csv(input_file2, header = 0)
prediction=pred['HorseWin']
Win=result['finishing_position']
Odds=result['win_odds']
race=result['race_id']

print("Classification(Without normalization)")
list=[]
Max=0
for i in range(len(race)-1):
    if(prediction[i]==1):
        list.append(i)
    id=race[i]
    if(id !=race[i+1]):
        #checkout
        shuffle(list)
        for num in list:
            if(Odds[num]>=5 and Odds[num]<=30 and result['jockey_ave_rank'][num]<=7 and result['trainer_ave_rank'][num]<=7):
                #buy
                if(prediction[num]==Win[num]):
                    count+=Odds[num]
                else:
                    count=count-1
                list=[]
                Max=0
        list=[]
        Max=0
    
print("lr Income: ",count)
#
pred = pd.read_csv("nb_predictions2.csv", header = 0)
total+=count
count=0
prediction=pred['HorseWin']
for i in range(len(race)-1):
    if(prediction[i]==1):
        list.append(i)
    id=race[i]
    if(id !=race[i+1]):
        #checkout
        shuffle(list)
        for num in list:
            if(Odds[num]>=5 and Odds[num]<=30 and result['jockey_ave_rank'][num]<=7 and result['trainer_ave_rank'][num]<=7):
                #buy
                if(prediction[num]==Win[num]):
                    count+=Odds[num]
                else:
                    count=count-1
                list=[]
                Max=0
        list=[]
        Max=0
print("nb Income: ",count)
#
pred = pd.read_csv("svm_predictions2.csv", header = 0)
total+=count
count=0
prediction=pred['HorseWin']

coming=""
for i in range(len(race)-1):
    if(prediction[i]==1):
        list.append(i)
    id=race[i]
    if(id !=race[i+1]):
        #checkout
        shuffle(list)
        for num in list:
            if(Odds[num]>=5 and Odds[num]<=30 and result['jockey_ave_rank'][num]<=7 and result['trainer_ave_rank'][num]<=7):
                #buy
                if(prediction[num]==Win[num]):
                    count+=Odds[num]
                else:
                    count=count-1
                list=[]
                Max=0
        list=[]
        Max=0
print("svm Income: ",count)
#
pred = pd.read_csv("rf_predictions2.csv", header = 0)
total+=count
count=0
prediction=pred['HorseWin']
coming=""
for i in range(len(race)-1):
    if(prediction[i]==1):
        list.append(i)
    id=race[i]
    if(id !=race[i+1]):
        #checkout
        shuffle(list)
        for num in list:
            if(Odds[num]>=5 and Odds[num]<=30 and result['jockey_ave_rank'][num]<=7 and result['trainer_ave_rank'][num]<=7):
                #buy
                if(prediction[num]==Win[num]):
                    count+=Odds[num]
                else:
                    count=count-1
                list=[]
                Max=0
        list=[]
        Max=0
print("rf Income: ",count)
#
total+=count
count=0
input_file = "lr_predictions.csv"
input_file2 = "testing.csv"
pred = pd.read_csv(input_file, header = 0)
result = pd.read_csv(input_file2, header = 0)
prediction=pred['HorseWin']
Win=result['finishing_position']
Odds=result['win_odds']
race=result['race_id']

print("Classification(Normalization)")
list=[]
Max=0
for i in range(len(race)-1):
    if(prediction[i]==1):
        list.append(i)
    id=race[i]
    if(id !=race[i+1]):
        #checkout
        shuffle(list)
        for num in list:
            if(Odds[num]>=5 and Odds[num]<=30 and result['jockey_ave_rank'][num]<=7 and result['trainer_ave_rank'][num]<=7):
                #buy
                if(prediction[num]==Win[num]):
                    count+=Odds[num]
                else:
                    count=count-1
                list=[]
                Max=0
        list=[]
        Max=0
    
print("lr Income: ",count)
#
total+=count
count=0
pred = pd.read_csv("nb_predictions.csv", header = 0)

prediction=pred['HorseWin']
for i in range(len(race)-1):
    if(prediction[i]==1):
        list.append(i)
    id=race[i]
    if(id !=race[i+1]):
        #checkout
        shuffle(list)
        for num in list:
            if(Odds[num]>=5 and Odds[num]<=30 and result['jockey_ave_rank'][num]<=7 and result['trainer_ave_rank'][num]<=7):
                #buy
                if(prediction[num]==Win[num]):
                    count+=Odds[num]
                else:
                    count=count-1
                list=[]
                Max=0
        list=[]
        Max=0
print("nb Income: ",count)
#
pred = pd.read_csv("svm_predictions.csv", header = 0)
total+=count
count=0
prediction=pred['HorseWin']

coming=""
for i in range(len(race)-1):
    if(prediction[i]==1):
        list.append(i)
    id=race[i]
    if(id !=race[i+1]):
        #checkout
        shuffle(list)
        for num in list:
            if(Odds[num]>=5 and Odds[num]<=30 and result['jockey_ave_rank'][num]<=7 and result['trainer_ave_rank'][num]<=7):
                #buy
                if(prediction[num]==Win[num]):
                    count+=Odds[num]
                else:
                    count=count-1
                list=[]
                Max=0
        list=[]
        Max=0
print("svm Income: ",count)
#
pred = pd.read_csv("rf_predictions.csv", header = 0)
total+=count
count=0
prediction=pred['HorseWin']
coming=""
for i in range(len(race)-1):
    if(prediction[i]==1):
        list.append(i)
    id=race[i]
    if(id !=race[i+1]):
        #checkout
        shuffle(list)
        for num in list:
            if(Odds[num]>=5 and Odds[num]<=30 and result['jockey_ave_rank'][num]<=7 and result['trainer_ave_rank'][num]<=7):
                #buy
                if(prediction[num]==Win[num]):
                    count+=Odds[num]
                else:
                    count=count-1
                list=[]
                Max=0
        list=[]
        Max=0
total+=count
print("rf Income: ",count)
print("total",total)