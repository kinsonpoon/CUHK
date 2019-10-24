import ezdxf
import os
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd 
import numpy as np
import math

def distance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist
#path="C:\\Users\\kinsonp\\Desktop\\FYP\\2010"
hfile="H.csv"
dfile="CLP.csv"
height = pd.read_csv(hfile, header = 0)
data=pd.read_csv(dfile, header = 0)
print(height.keys())
hpt=[]
for i in range(len(height['x'])):
    hpt.append((height['x'][i],height['y'][i]))
#print(hpt)

oklist={}
for i in range(len(hpt)):
    h=height['H'][i]
    pt=hpt[i]
    for j in range(len(data['x'])):
        if(distance(pt[0],pt[1],data['x'][j],data['y'][j])<=10):
            if(data['gp'][j]not in oklist):
                oklist[data['gp'][j]]=h
            #print('yes',data['gp'][j],"was found",h)
            #print(pt[0],data['x'][j],pt[1],data['y'][j])
        
            j=len(data['x'])+10
print(oklist)
print(len(oklist))
lh=[]
for x in data['gp']:
    if(x in oklist):
        lh.append(oklist[x])
    else:
        lh.append("NA")
lx=data['x']
ly=data['y']
lmap=data['map']
lgp=data['gp']
zippedList =  list(zip(lx,ly,lh,lmap,lgp))
df = pd.DataFrame(zippedList, columns = ['x' , 'y','H','map','gp']) 
df.to_csv('CLP_H.csv',index=False) 