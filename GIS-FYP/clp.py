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
def get_gadget(msp):
    x_max=[]
    y_max=[]
    group = msp.groupby(dxfattrib='layer')
    for layer, entities in group.items():
        if(layer=='SITE'):
            for entity in entities:
                if(entity.dxftype()=="LWPOLYLINE"):
                    pt=entity.get_points()
                    if(len(pt)==4):
                        if(distance(pt[0][0],pt[0][1],pt[1][0],pt[1][1])>=3000):
                            for x in pt:
                                x_max.append(x[0])
                                y_max.append(x[1])
    return min(x_max),min(y_max)
def makedf(lx,ly,lh,lmap,lgp,name):
    filename=name+str(lmap[0])+"_proj.csv"
    xmin,ymin=get_gadget(msp)
    lx=[round((x-xmin)/4,3) for x in lx]
    ly=[round((y-ymin)/4,3) for y in ly]
    zippedList =  list(zip(lx,ly,lh,lmap,lgp))
    df = pd.DataFrame(zippedList, columns = ['x' , 'y','H','map','gp']) 
    df.to_csv(filename,index=False) 
def get_txt(msp,dfile):
    lx=[]
    ly=[]
    lt=[]
    lmap=[]
    lgp=[]
    for mtext in msp.query("MTEXT"):
        t=mtext.text
        
        #print(t)
        #print(mtext.dxf.insert)
        if(mtext.dxf.insert[2]==0.0 and t.replace('.','',1).isdigit() and int(t)%10==0):
            lt.append(mtext.text)
            lx.append(mtext.dxf.insert[0])
            ly.append(mtext.dxf.insert[1])
            lmap.append(dfile)
            lgp.append("X")
        elif(t.isalpha() and ord(mtext.text[0])!=92 and t!="Ruin" and t!="Fence" and t!="Pipeline"):
            lt.append(mtext.text)
            lx.append(mtext.dxf.insert[0])
            ly.append(mtext.dxf.insert[1])
            lmap.append(dfile)
            lgp.append("X")
    makedf(lx,ly,lt,lmap,lgp,"char")
    
def RKA(entities):
    lx=[]
    ly=[]
    lh=[]
    lmap=[]
    lgp=[]
    j=0
    for entity in entities:
        if(entity.dxftype()=="LWPOLYLINE"):
            pt=entity.get_points()
            length=len(pt)
            if(length>50):
                for i in range(0,length,2):
                    lx.append(pt[i][0])
                    ly.append(pt[i][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
                if pt[length-1][0]not in lx:
                    lx.append(pt[length-1][0])
                    ly.append(pt[length-1][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            elif(length>200):
                for i in range(0,length,4):
                    lx.append(pt[i][0])
                    ly.append(pt[i][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
                if pt[length-1][0] not in lx :
                    lx.append(pt[length-1][0])
                    ly.append(pt[length-1][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            else:
                for x in pt:
                    lx.append(round(x[0],1))
                    ly.append(round(x[1],1))
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            j=j+1
    makedf(lx,ly,lh,lmap,lgp,"RKA") 
def HW(entities):
    lx=[]
    ly=[]
    lh=[]
    lmap=[]
    lgp=[]
    j=0
    for entity in entities:
        if(entity.dxftype()=="LWPOLYLINE"):
            pt=entity.get_points()
            length=len(pt)
            if(length>50):
                for i in range(0,length,2):
                    lx.append(pt[i][0])
                    ly.append(pt[i][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
                if pt[length-1][0]not in lx:
                    lx.append(pt[length-1][0])
                    ly.append(pt[length-1][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            elif(length>200):
                for i in range(0,length,4):
                    lx.append(pt[i][0])
                    ly.append(pt[i][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
                if pt[length-1][0] not in lx :
                    lx.append(pt[length-1][0])
                    ly.append(pt[length-1][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            else:
                for x in pt:
                    lx.append(round(x[0],1))
                    ly.append(round(x[1],1))
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            j=j+1
    makedf(lx,ly,lh,lmap,lgp,"HW") 
def ICL(entities):
    lx=[]
    ly=[]
    lh=[]
    lmap=[]
    lgp=[]
    j=0
    for entity in entities:
        if(entity.dxftype()=="LWPOLYLINE"):
            pt=entity.get_points()
            length=len(pt)
            if(length>50):
                for i in range(0,length,2):
                    lx.append(pt[i][0])
                    ly.append(pt[i][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
                if pt[length-1][0]not in lx:
                    lx.append(pt[length-1][0])
                    ly.append(pt[length-1][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            elif(length>200):
                for i in range(0,length,4):
                    lx.append(pt[i][0])
                    ly.append(pt[i][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
                if pt[length-1][0] not in lx :
                    lx.append(pt[length-1][0])
                    ly.append(pt[length-1][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            else:
                for x in pt:
                    lx.append(round(x[0],1))
                    ly.append(round(x[1],1))
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            j=j+1
    makedf(lx,ly,lh,lmap,lgp,"ICL")
def NCL(entities):
    lx=[]
    ly=[]
    lh=[]
    lmap=[]
    lgp=[]
    j=0
    for entity in entities:
        if(entity.dxftype()=="LWPOLYLINE"):
            pt=entity.get_points()
            length=len(pt)
            if(length>50):
                for i in range(0,length,2):
                    lx.append(pt[i][0])
                    ly.append(pt[i][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
                if pt[length-1][0]not in lx:
                    lx.append(pt[length-1][0])
                    ly.append(pt[length-1][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            elif(length>200):
                for i in range(0,length,4):
                    lx.append(pt[i][0])
                    ly.append(pt[i][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
                if pt[length-1][0] not in lx :
                    lx.append(pt[length-1][0])
                    ly.append(pt[length-1][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            else:
                for x in pt:
                    lx.append(round(x[0],1))
                    ly.append(round(x[1],1))
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            j=j+1
    makedf(lx,ly,lh,lmap,lgp,"NCL")
def FP(entities):
    lx=[]
    ly=[]
    lh=[]
    lmap=[]
    lgp=[]
    j=0
    for entity in entities:
        if(entity.dxftype()=="LWPOLYLINE"):
            pt=entity.get_points()
            length=len(pt)
            if(length>50):
                for i in range(0,length,2):
                    lx.append(pt[i][0])
                    ly.append(pt[i][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
                if pt[length-1][0]not in lx:
                    lx.append(pt[length-1][0])
                    ly.append(pt[length-1][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            elif(length>200):
                for i in range(0,length,4):
                    lx.append(pt[i][0])
                    ly.append(pt[i][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
                if pt[length-1][0] not in lx :
                    lx.append(pt[length-1][0])
                    ly.append(pt[length-1][1])
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
            else:
                for x in pt:
                    lx.append(round(x[0],1))
                    ly.append(round(x[1],1))
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
        else:
            pt=[]
            pt.append(entity.dxf.start)
            pt.append(entity.dxf.end)
            for x in pt:
                    lx.append(round(x[0],1))
                    ly.append(round(x[1],1))
                    lmap.append(dfile)
                    lh.append("NA")
                    lgp.append(j)
        j=j+1
        
    makedf(lx,ly,lh,lmap,lgp,"FP")
def tran(group,dfile):
    for layer, entities in group.items():
        if(layer=='ICL'):
            ICL(entities)
        if(layer=='NCL'):
           NCL(entities)
        if(layer=='FP'):
            FP(entities)
        if(layer=="cwf_f"):
            for entity in entities:
                print(entity.dxftype())
            #HW(entities)
        if(layer=="RKA"):
            RKA(entities)
    
path="C:\\Users\\kinsonp\\Desktop\\FYP\\2011"
dfile="3seb"
targetfile=dfile+".dxf"
targetfile=os.path.join(dfile, targetfile)
dxf=os.path.join(path, targetfile)
doc = ezdxf.readfile(dxf)
msp = doc.modelspace()


#get_txt(msp,dfile)
group = msp.groupby(dxfattrib='layer')
tran(group,dfile)

'''
for layer, entities in group.items():
    if(layer=='NCL'):
        print(layer)
        for entity in entities:
            if(entity.dxftype()=="LWPOLYLINE"):
                pt=entity.get_points()
                #print(i)
            else:
                pt=[]
                pt.append(entity.dxf.start)
                pt.append(entity.dxf.end)
            for x in pt:
                lx.append(round(x[0],1))
                ly.append(round(x[1],1))
                lmap.append(dfile)
                lh.append("NA")
                lgp.append(i)
            i=i+1
#df = pd.DataFrame(lx,ly,lmap,lgp)
makedf(lx,ly,lh,lmap,lgp)
'''
