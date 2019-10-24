import ezdxf
import os
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd 
import numpy as np
import math
import datetime
from datetime import timedelta
import time

def distance(df1,df2):
    dist = math.sqrt((df2['x'] - df1['x'])**2 + (df2['y'] - df1['y'])**2)
    return dist
'''
def compareX(df1,df2):
    result=df1['x']-df2['x']
    return result  
def compareY(df1,df2):
    result=df1['y']-df2['ys']
    return result  
'''
def bruteForce(df1,df2):  
    min = 10000
    for i in range(len(df1['x'])):
        for j in range(len(df2['x'])):
            if (distance(df1.iloc[i], df2.iloc[j]) < min):
                min = distance(df1.iloc[i], df2.iloc[j])
    return min
def pair_up(df):
    start_time = time.time()
    print("pairingup ICL,please wait until 2046")
    l_gp=get_listofgp(df)
    data=[]
    dflist=getall_list(df)
    for i in range(len(dflist)):
        temp_data=[]
        for j in range(len(dflist)):
            if(i==j):
                temp_data.append(0)
            if (i!=j):
                if(i<j):
                    min=bruteForce(dflist[i],dflist[j])
                    temp_data.append(min)
                else:
                    temp_data.append(data[j][i])
        data.append(temp_data)
        
        print(i,"finallyok, and it takes",running_time(start_time))
    result_df = pd.DataFrame(data, columns =l_gp,index=l_gp)
    result_df.to_csv('ICL_PAIRS.csv',index=False) 
    print("all done,saved into csv, and it takes",running_time(start_time))
#
def running_time(start):
    end_time = time.time()
    timespd = end_time-start
    hours = timespd//3600
    timespd = timespd - 3600*hours
    minutes = timespd//60
    seconds = timespd - 60*minutes
    return_time='%d:%d:%d' %(hours,minutes,seconds)
    return return_time
#
def to_listofpt(df,i):
    list_i=df.loc[df['gp'] == i]
    return list_i
def get_listofgp(df):
    lgp=df.gp.unique()
    return lgp
def getall_list(df):
    hgp=get_listofgp(df)
    DF_list = list()
    for i in hgp:
        DF_list.append(to_listofpt(df,i))
    return DF_list

#start_time = time.time()

#path="C:\\Users\\kinsonp\\Desktop\\FYP\\2010"
hfile="CLP_H.csv"
dfile="NLP.csv"
height = pd.read_csv(hfile, header = 0)
height=height.dropna()
data=pd.read_csv(dfile, header = 0)
pair_up(height)
'''
hlist=getall_list(height)
hgp=get_listofgp(height)
#
dlist=getall_list(data)
dgp=get_listofgp(data)
#print(clp)
nlp_gp=[]
first_min=[]
first_min_distance=[]
second_min=[]
second_min_distance=[]
for i in range(len(dgp)):
    nlp_gp.append(i)
    result_dict={}
    for j in range(len(hgp)):
        result_dict[hgp[j]]=bruteForce(dlist[i],hlist[j])
    dis_list=result_dict.items()
    dis_list=sorted(dis_list, key=lambda k: k[1])
    first_min.append(dis_list[0][0])
    first_min_distance.append(dis_list[0][1])
    second_min.append(dis_list[1][0])
    second_min_distance.append(dis_list[1][1])
    end_time = time.time()
    print(i,"finallyok:",end_time-start_time)
zippedList =  list(zip(nlp_gp,first_min,first_min_distance,second_min,second_min_distance))
df = pd.DataFrame(zippedList, columns = ['gp' , '1min','1dis','2min','2dis']) 
df.to_csv('closest.csv',index=False) 
print("all done,saved into csv ",end_time-start_time)


'''