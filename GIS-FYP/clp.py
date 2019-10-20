import ezdxf
import os
import matplotlib.pyplot as plt
import networkx as nx

path="C:\\Users\\kinsonp\\Desktop\\FYP\\2010\\2ned"
targetfile="2ned.dxf"

dxf=os.path.join(path, targetfile)
doc = ezdxf.readfile(dxf)
msp = doc.modelspace()
group = msp.groupby(dxfattrib='layer')
for layer, entities in group.items():
    if(layer=='ICL'):
        print(layer)
