import ezdxf
import os
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd 
import math
import numpy as np
from shapely.geometry import Point, Polygon
def distance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist

def get_range(df,startx,starty):
    df1 = df[df['x'] > startx]
    df1=df[df['y'] > starty]
    df1=df1.reset_index(drop=True)
    gpnow=df1["gp"][0]
    resultrow=df1.loc[df1['gp'] == gpnow]
    #print(resultrow)
    return gpnow,df1["H"][0],resultrow['x'].min(),resultrow['x'].max(),resultrow['y'].min(),resultrow['y'].max()
def find_next(df,H,lastgp,max_x,min_y):
    #print(min_x,min_y,max_y)
    #print(lastgp)
    #print("lol")
    df1=df[~(df['gp'] == lastgp)]
    df1 = df1[df1['x'] > max_x]
    df1=df1[df1['y'] > min_y]
    #print(df1)
    #df1=df1[df1['y'] < max_y]
    df1=df1.reset_index(drop=True)
    #print(df1)
    i=0
    
    while(True):
        if(df1["H"][i]!=H):
            gpnext=df1["gp"][i]
            break
        i=i+1
    return gpnext
    #return "dlln"
def find_btwa(df,ncl_dict,max_x,min_y,max_xx,max_yy,H,H2):
    df = df[df['x'] > max_x]
    df = df[df['x'] < max_xx]
    df = df[df['y'] > min_y]
    df = df[df['y'] < min_y+10]
    mylist=[]
    #print(df["gp"].values)
    for val in df["gp"].values:
        #print(val)
        if(val not in mylist):
            mylist.append(val)
    return mylist

def all_ICL(df):
    l=[]
    temp=[]
    for val in df["gp"].values:
        if(val not in l):
            l.append(val)
            resultrow=df.loc[df['gp'] == val]
            resultrow=resultrow.reset_index(drop=True)
            temp.append((val,resultrow["H"][0],resultrow['x'].min(),resultrow['x'].max(),resultrow['y'].min(),resultrow['y'].max()))
    l={}
    for item in temp:
        l[item[0]]=item[1:]

    return l
def start_icl(df1,df2):
    first=[]
    visited=[]
    pairs=[]
    icl_dict=all_ICL(df2)
    first.append(get_range(df2,0,0))
    last=first[0][0]
    i=0
    while(True):
        next_edge=find_next(df2,icl_dict[last][0],last,icl_dict[last][2],icl_dict[last][3])
        pairs.append((last,next_edge))
        last=next_edge
        i=i+1
        if(i>5):
            break
    print(pairs)
    return pairs

def main(df1,df2):
    df1=df1.assign(f = df1['x']**2 + df1['y']**2).sort_values('f').drop('f', axis=1)
    df2=df2.assign(f = df2['x']**2 + df2['y']**2).sort_values('f').drop('f', axis=1)
    pairs=[]
    NCL={}
    ICL_dict=all_ICL(df2)
    #pairs=start_icl(df1,df2)

    
    for icl in ICL_dict.keys():
        try:
            id2=find_next(df2,ICL_dict[icl][0],icl,ICL_dict[icl][2],ICL_dict[icl][3])
            #print(df2,ICL_dict[icl][0],id1,ICL_dict[icl][1],ICL_dict[icl][3],ICL_dict[icl][4])
            pairs.append((icl,id2))
        except:
            pass
    print(pairs)
    
    for p in pairs:
        try:
            H=ICL_dict[p[0]][0]
            H2=ICL_dict[p[1]][0]
            mylist=find_btwa(df1,NCL,ICL_dict[p[0]][2],ICL_dict[p[0]][3],ICL_dict[p[1]][2],ICL_dict[p[1]][4],H,H2)
            hlist=[]
            print(mylist)
            for i in range(int(H-(H-H2)/5),int(H2),int(-(H-H2))/5):
                hlist.append(i)
            i=0
            for line in mylist:
                NCL[line]=hlist[i]
                i=i+1
        except:
            pass
    print(NCL)
'''
    
    id1,H,x,x1,y,y1=get_range(df2,0,0)
    print(id1,H,x,x1,y,y1)

    id2,H2,xx,xx1,yy,yy1=find_next(df2,H,id1,x,y,y1)
    print(id2,H2,xx,xx1,yy,yy1)
    mylist=find_btw(df1,x1,y,xx,yy1)
    hlist=[]
    for i in range(int(H-(H-H2)/5),int(H2),int(-(H-H2)/5)):
        hlist.append(i)

    for i in range(len(mylist)):
        pairs[mylist[i]]=hlist[i]

    return pairs
    '''







Nfile="NCL14nwa_proj.csv"
Cfile="ICL14nwa_proj.csv"
df1 = pd.read_csv(Nfile, header = 0)
df2 = pd.read_csv(Cfile, header = 0)
df2=df2.dropna()
main(df1,df2)