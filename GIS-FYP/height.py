import ezdxf
import os
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd 
import math
import numpy as np
def distance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist

def ret_4_high(dict1,dict2):
    tof=[]
    for k in dict1.keys():
        tof.append([k,dict1[k]/dict2[k]])
    tof.sort(key = lambda x: x[1],reverse=True)
    return tof
def calculation(df1,df2):
    frames = [df1, df2]
    df1["t"]="NCL"
    df2["t"]="ICL"
    df = pd.concat(frames,ignore_index=True)
    #df=df.sort_values(by=['y'])
    #df=df.sort_values(by=['x'])
    df=df.assign(f = df['x']**2 + df['y']**2).sort_values('f').drop('f', axis=1)
    df=df.reset_index(drop=True)
    #df3=df.loc[df['H'].isin([50,100])]
    #print(df)
    visited=[]
    lis=[]
    h=[]
    indexs=[]
    totfreq={}
    for index, row in df.iterrows():
        if row["t"]=="ICL":
            if(row["gp"] not in lis):
                if(len(h)>2 and row["H"]!=h[len(h)-1]):
                    lis.append(row["gp"])
                    h.append(row["H"])
                    indexs.append(index)
                elif(len(h)<=2):
                    lis.append(row["gp"])
                    h.append(row["H"])
                    indexs.append(index)
        elif(row["t"]!="ICL"):
            if(row["gp"] not in totfreq):
                totfreq[row["gp"]]=1
            else:
                totfreq[row["gp"]]=totfreq[row["gp"]]+1
    #for i in range(len(lis)):
        #print(lis[i],h[i],indexs[i])
    pairs=[]
    for i in range(1,len(lis)-1):
        rowData = df.loc[ range(indexs[i],indexs[i+1]) , : ]
        gp={}
        for index, row in rowData.iterrows():
            if(row["t"]!="ICL"):
                if(row["gp"] not in gp):
                    gp[row["gp"]]=1
                else:
                    gp[row["gp"]]=gp[row["gp"]]+1
        pair=ret_4_high(gp,totfreq)
        #print(pair[0:4])
        temp=[]
        for item in pair[0:4]:
            temp.append(item[0])
        pairs.append(temp)
    print(pairs)
    changing={}
    for i in range(1,len(lis)-1):
        chk=h[i-1]-h[i]
        if(chk>0):
            dis=10
        else:
            dis=-10
        rowData = df.loc[ range(indexs[i],indexs[i+1]) , : ]
        gp=[]
        #print(pairs[i-1])
        try:
            for index, row in rowData.iterrows():
                if(row["t"]!="ICL"):
                    if(row["gp"] in pairs[i-1]):
                        if(row["gp"] not in gp):
                            gp.append(row["gp"])
            for k in range(len(gp)):
                #print(gp[k],h[i-1]+dis*(k+1))
                changing[gp[k]]=h[i-1]+dis*(k+1)
        except:
            for k in range(len(gp)):
                #print(gp[k],h[i-1]+dis*(k+1))
                changing[gp[k]]=h[i-1]+dis*(k+1)
            pass
    return changing


Nfile="NCL14nwa_proj.csv"
Cfile="ICL14nwa_proj.csv"
df1 = pd.read_csv(Nfile, header = 0)
df2 = pd.read_csv(Cfile, header = 0)
df2=df2.dropna()
change=calculation(df1,df2)
for item in change.keys():
    df1.loc[df1['gp'] ==item, 'H'] = change[item]
df1.to_csv("markICL.csv",index=False) 