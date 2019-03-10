# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:06:35 2018

@author: kinsonp
"""
import os.path
import numpy as np
import matplotlib.pyplot as plt
import scipy as spy
import pandas as pd

input_file = "data/race-result-race.csv"
input_file2 = "data/race-result-horse.csv"
df_race = pd.read_csv(input_file, header = 0)
race_features=df_race.keys()
#num_race_features=len(df_race.keys())
#print("race_features:",race_features)
#print("num_race_features:",num_race_features)


df_horse = pd.read_csv(input_file2, header = 0)
#horse_features=df_horse.keys()
#num_horse_features=len(df_horse.keys())
#print("horse_features:",horse_features)
#print("num_horse_features:",num_horse_features)
print(len(df_horse['horse_number']))
list=[]
droplist=['WV-A', 'WV', '9 DH', '2 DH', 'WX', 'PU', '1 DH', '8 DH', 'UR', 'FE', '4 DH', '10 DH', 'TNP', '5 DH', 'DISQ', '11 DH', '12 DH', '3 DH', '7 DH', 'WX-A', 'DNF', '6 DH','nan']
for i in range(len(df_horse['finishing_position'])):
    if(df_horse['finishing_position'][i] in droplist):
        list.append(i)
    if(type(df_horse['finishing_position'][i]) == float):
        list.append(i)
#print(len(list))
df_horse=df_horse.drop(df_horse.index[list])
#print(len(df_horse['jockey']))
#check=[]
#for item in df_horse['finishing_position']:
#    if(item not in check):
#        check.append(item)
print("The data is cleaned")
name=[]
for item in df_horse['horse_name']:
        if(item not in name):
            name.append(item)
            

count=0
for i in range(30189+1):
    try:
        xd=df_horse['horse_name'][30189-i]
        count=count+1
    except:
        pass
print("count",count)
d={}
#df_horse['recent_6_runs']=""
print(len(df_horse.keys()))
for names in name:
    d[names]=[0,0,0,0,0,0]
df=pd.DataFrame(data=d)
print(len(df.keys()))
insert_list=[""]
for i in range(1,30190):
    try:
        names=df_horse['horse_name'][i]
        position=df_horse['finishing_position'][i]
        line=""
        
        for j in range(6):
            if df[names][j] !=0:
                if(j==0):
                    line=str(df[names][j])
                else:
                    line=line+"/"+str(df[names][j])
        insert_list.append(line)
        for j in range(6):
            if df[names][j] ==0:
               df[names][j]=position
               break
            elif(j==5):
               df[names][0] =df[names][1]
               df[names][1] =df[names][2]
               df[names][2] =df[names][3]
               df[names][3] =df[names][4]
               df[names][4] =df[names][5]
               df[names][5] =position
        
    except:
        pass
df_horse.insert(loc=0, column='recent_6_runs', value=insert_list)
print('recent_6_runs is inserted')
ave_rank=[]
for string in df_horse['recent_6_runs']:
    count=1
    if string=="":
        ave_rank.append(7)
    else:
        line=""
        for char in string:
            if(char =='/'):
                line+="+"
                count+=1
            else:
                line+=char
        score=eval(line)
        ave_rank.append(score/count)
df_horse.insert(loc=0, column='recent_ave_rank', value=ave_rank)
print('recent_ave_rank is inserted')
#name[] store the name of horse
jockey=[]
for jockeys in df_horse['jockey']:
    if(jockeys not in jockey):
        jockey.append(jockeys)
#jockey[] store the name of jockeys
trainer=[]
for trainers in df_horse['trainer']:
    if trainers not in trainer:
        trainer.append(trainers)
#trainer=[] store the name of trainer
print("Number of horses: ",len(name))
print("Number of jockeys: ",len(jockey))
print("Number of trainers: ",len(trainer))
#
dic={}
for jock in jockey:
    dic[jock]=[0,0]
df_jockey=pd.DataFrame(data=dic)
for i in range(30190):
    try:
        jack=df_horse['jockey'][i]
        df_jockey[jack][0]=int(df_jockey[jack][0])+int(df_horse['finishing_position'][i])
        df_jockey[jack][1]+=1
    except:
        pass
insert_jockey=[]
for jock in df_horse['jockey']:
    add=df_jockey[jock][0]/df_jockey[jock][1]
    insert_jockey.append(add)
df_horse.insert(loc=0, column='jockey_ave_rank', value=insert_jockey)
print('jockey_ave_rank is inserted')
##

dic={}
for train in trainer:
    dic[train]=[0,0]
df_trainer=pd.DataFrame(data=dic)
for i in range(30190):
    try:
        train=df_horse['trainer'][i]
        df_trainer[train][0]=int(df_trainer[train][0])+int(df_horse['finishing_position'][i])
        df_trainer[train][1]+=1
    except:
        pass
insert_trainer=[]
for train in df_horse['trainer']:
    add=df_trainer[train][0]/df_trainer[train][1]
    insert_trainer.append(add)
df_horse.insert(loc=0, column='trainer_ave_rank', value=insert_trainer)
print('trainer_ave_rank is inserted')
#2.2.4
race_dict={}
for i in range(len(df_race['race_id'])):
    if df_race['race_id'][i] not in race_dict.keys():
        race_dict[df_race['race_id'][i]]=df_race['race_distance'][i]
insert_distance=[]
for i in range(30190):
    try:
        id=df_horse['race_id'][i]
        insert_distance.append(race_dict[id])
    except:
        pass
df_horse.insert(loc=0, column='race_distance', value=insert_distance)
#final~~xdd
flag=0
split=0
count=0
for i in range(30190):
    try:
        id=df_horse['race_id'][i]
        count+=1
        if id=="2016-327":
            flag=1
        elif flag==1:
            split=count
            break
    except:
        pass
print(split)
dfs=np.split(df_horse,[split-1],axis=0)
dfs[0].to_csv("training.csv", encoding='utf-8', index=False)
dfs[1].to_csv("testing.csv", encoding='utf-8', index=False)   
df_horse.to_csv("all.csv", encoding='utf-8', index=False)   
print("converted to csv:)")