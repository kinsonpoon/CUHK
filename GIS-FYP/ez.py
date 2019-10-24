import ezdxf
import matplotlib.pyplot as plt
import networkx as nx
import os
#def Height(entities):
 #   continue
 
path="C:\\Users\\kinsonp\\Desktop\\FYP\\2010"
dfile="2ned"
targetfile=dfile+".dxf"
targetfile=os.path.join(dfile, targetfile)
def NCL(entities):
    graph=nx.Graph()
    i=0
    last=""
    for entity in entities:
            
        #print(i)
        print(entity.dxftype())
        if(entity.dxftype()=="LWPOLYLINE"):
            pt=entity.get_points()
            lx=[]
            ly=[]
            for x in pt:
                lx.append(x[0])
                ly.append(x[1])
            for j in range(len(lx)-1):
                
                if(j!=0):
                    new_name=str(i)+"F"+str(j)
                   # print(name,new_name)
                    graph.add_edge(name,new_name)
                name=str(i)+"F"+str(j)
                
                graph.add_node(name,pos=(lx[j],ly[j]))
        else:
            pt=[]
            pt.append(entity.dxf.start)
            pt.append(entity.dxf.end)
            name=str(i)+"F0"
            name1=str(i)+"F1"
            graph.add_node(name,pos=(pt[0][0],pt[0][1]))
            graph.add_node(name1,pos=(pt[1][0],pt[1][1]))
            graph.add_edge(name,name1)
        i+=1    
    return graph
def ICL(entities):
    graph=nx.Graph()
    i=0
    print(len(entities))
    for entity in entities:
            
        #print(entity.dxfattribs)
        if(entity.dxftype()=="LWPOLYLINE"):
            pt=entity.get_points()
        else:
            pt=[]
            pt.append(entity.dxf.start)
            pt.append(entity.dxf.end)
        lx=[]
        ly=[]
        for x in pt:
            lx.append(x[0])
            ly.append(x[1])

        for j in range(len(lx)-1):
                
            if(j!=0):
                new_name=str(i)+"I"+str(j)
                   # print(name,new_name)
                graph.add_edge(name,new_name)
            name=str(i)+"I"+str(j)
                
            graph.add_node(name,pos=(lx[j],ly[j]))
            
        i+=1
    return graph
def FP(entities):
    graph=nx.Graph()
    i=0
    last=""
    for entity in entities:
            
        #print(i)
        #print(entity.dxftype())
        
        if(entity.dxftype()=="LWPOLYLINE"):
            pt=entity.get_points()
            lx=[]
            ly=[]
            for x in pt:
                lx.append(x[0])
                ly.append(x[1])
            for j in range(len(lx)-1):
                
                if(j!=0):
                    new_name=str(i)+"F"+str(j)
                   # print(name,new_name)
                    graph.add_edge(name,new_name)
                name=str(i)+"F"+str(j)
                
                graph.add_node(name,pos=(lx[j],ly[j]))
            '''    
        if(last!=""):
            first=str(i)+"S"+"0"
            print(last,first,name)
            graph.add_edge(first,last)
        last=str(i)+"S"+str(len(lx)-2)
            '''
        
        else:
            pt=[]
            pt.append(entity.dxf.start)
            pt.append(entity.dxf.end)
            name=str(i)+"F0"
            name1=str(i)+"F1"
            graph.add_node(name,pos=(pt[0][0],pt[0][1]))
            graph.add_node(name1,pos=(pt[1][0],pt[1][1]))
            graph.add_edge(name,name1)
        i+=1    
    return graph
dxf=os.path.join(path, targetfile)
doc = ezdxf.readfile(dxf)
msp = doc.modelspace()


N=nx.Graph()
F=nx.Graph()
I=nx.Graph()
G=nx.Graph()
group = msp.groupby(dxfattrib='layer')
i=0
heightlist=[]
for mtext in msp.query("MTEXT"):
    
    t=mtext.text
    if(mtext.dxf.insert[2]==0.0 and t.replace('.','',1).isdigit() and int(t)%10==0):
        heightlist.append(mtext.text)
        print(mtext.text,"at",mtext.dxf.insert[0],mtext.dxf.insert[1] )
        G.add_node(str(len(heightlist)-1)+t,pos=(mtext.dxf.insert[0],mtext.dxf.insert[1]))
    '''
    if(t.replace('.','',1).isdigit()):
        print("MTEXT content: {}".format(mtext.text))
        
        print(mtext.dxf.insert)
        '''
        #G.add_node(t,pos=(mtext.dxf.insert[0],mtext.dxf.insert[1]))
pos=nx.get_node_attributes(G,'pos')        
nx.draw(G,pos,node_size=100,node_color="r",edge_color="r")
for layer, entities in group.items():

    #s'''
    if(layer=='NCL'):
        print(layer)
        N=NCL(entities)
        G=nx.compose(G,N)
        pos=nx.get_node_attributes(N,'pos')
        nx.draw(N,pos,node_size=10,node_color="r",edge_color="r")
        
        #print(lx,ly)
        print('-'*40)
    '''
    if(layer=='FP'):
        print(layer)
        F=FP(entities)
        G=nx.compose(G,F)
        pos=nx.get_node_attributes(F,'pos')
        nx.draw(F,pos,node_size=10,node_color="b",edge_color="b")
    
    if(layer=='ICL'):
        print(layer)
        I=ICL(entities)
        G=nx.compose(G,I)
        pos=nx.get_node_attributes(I,'pos')
        nx.draw(I,pos,node_size=10,node_color="y",edge_color="y")
        '''
    

plt.show()
        #print(lx,ly)
print('-'*40)

