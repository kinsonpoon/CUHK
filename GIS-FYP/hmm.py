import ezdxf
import os
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd 
import numpy as np

def layer_and_color_key(entity):
    # return None to exclude entities from result container
    if entity.dxf.layer == '0':  # exclude entities from default layer '0'
        return None
    else:
        return entity.dxf.layer, entity.dxf.color
def xdd(msp):
    group = msp.groupby= msp.groupby(dxfattrib='layer')
    for layer, entities in group.items():
        print(layer)
        color=""
        for entity in entities:
            color=entity.dxf.color
        print(color)
        print('-'*40)
path="C:\\Users\\kinsonp\\Desktop\\FYP\\2011"
dfile="14nwa"
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
xdd(msp)
'''
i=0
dictlayer={}
for layer, entities in group.items():
    print(layer)
    ene=[]
    print(len(entities))
    e.dxf.color
        for entity in entities:
        #print(len(entities))
        
            #ene.append(entity.dxftype())
            if(entity.dxftype()=="LWPOLYLINE"):
                pt=entity.get_points()
                if(len(pt)==4):
                    ene.extend(pt)
                
                    graph=nx.Graph()
                    i=0
                    for x in pt:
                        graph.add_node(i,pos=(x[0],x[1]))
                        i+=1
    #print(ene)
                    pos=nx.get_node_attributes(graph,'pos')
                    nx.draw(graph,pos,node_size=100,node_color="r",edge_color="r")
                    plt.show()
                
                #print(pt)
                
    dictlayer[layer]=ene
            
#print(dictlayer)
#df = pd.DataFrame(lx,ly,lmap,lgp)
'''

