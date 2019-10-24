import ezdxf
import os
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd 
import numpy as np

path="C:\\Users\\kinsonp\\Desktop\\FYP\\2010"
dfile="2ned"
targetfile=dfile+".dxf"
targetfile=os.path.join(dfile, targetfile)
dxf=os.path.join(path, targetfile)
doc = ezdxf.readfile(dxf)
msp = doc.modelspace()                                                                                                                                             
lx=[]
ly=[]
lh=[]
lmap=[]
lgp=[]

group = msp.groupby(dxfattrib='layer')
for mtext in msp.query("MTEXT"):
    
    t=mtext.texts
    i=0
    if(t.replace('.','',1).isdigit()):
        lh.append(mtext.text)
        lx.append(mtext.dxf.insert[0])
        ly.append(mtext.dxf.insert[1])
        lmap.append(dfile)
        lgp.append(i)
        i=i+1


zippedList =  list(zip(lx,ly,lh,lmap,lgp))
df = pd.DataFrame(zippedList, columns = ['x' , 'y','H','map','gp']) 
df.to_csv('H2.csv',index=False) 