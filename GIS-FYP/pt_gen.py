import ezdxf
import os
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd 
import numpy as np
import math  

def midpoint(x1,y1,x2,y2):
    x=(x1+x2)/2
    y=(y1+y2)/2
    listx=[]
    listy=[]
    if(distance(x1,y1,x,y)>10):
        pt=midpoint(x1,y1,x,y)
        listx.extend(pt[0])
        listy.extend(pt[1])
    else:
        if(x not in listx):
            listx.append(x)
            listy.append(y)
    if(distance(x,y,x2,y2)>10):
        pt=midpoint(x,y,x2,y2)
        listx.extend(pt[0])
        listy.extend(pt[1])
    return listx,listy
def distance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist
#path="C:\\Users\\kinsonp\\Desktop\\FYP\\2010"
dbfile="CLP.csv"
dfile="2ned"
data=pd.read_csv(dbfile, header = 0)


x=data['x']
y=data['y']
lx=[x[0]]
ly=[y[0]]
lh=[]
lmap=[]
lgp=[]
gp=0
#print(x[0],y[0])
#print(midpoint(x[0],y[0],x[0]+100,y[0]+100))
#print(x[0]+100,y[0]+100)
print(lx)
print(ly)
for i in range(1 ,len(x)):
    if(data['gp'][i]==gp):
        lx.append(x[i])
        ly.append(y[i])
        if(distance(lx[len(lx)-2],ly[len(lx)-2],lx[len(lx)-1],ly[len(lx)-1])>10):
            pt=midpoint(lx[len(lx)-2],ly[len(lx)-2],lx[len(lx)-1],ly[len(lx)-1])
            del lx[-1]
            del ly[-1]
            lx.extend(pt[0])
            ly.extend(pt[1])
            lx.append(x[i])
            ly.append(y[i])
    else:
        for i in range(len(lh),len(lx)):
            lmap.append(dfile)
            lh.append("NA")
            lgp.append(gp)
        gp+=1
        lx.append(x[i])
        ly.append(y[i])
for i in range(len(lh),len(lx)):
            lmap.append(dfile)
            lh.append("NA")
            lgp.append(gp)
zippedList =  list(zip(lx,ly,lh,lmap,lgp))
df = pd.DataFrame(zippedList, columns = ['x' , 'y','H','map','gp']) 
df.to_csv('CLP2.csv',index=False) 
