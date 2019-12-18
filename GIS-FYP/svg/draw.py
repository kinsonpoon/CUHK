import svgwrite
import pandas as pd 
import numpy as np
def poly_list(df):
    gp=0
    data=[]
    temp=[]
    for i in range(len(df['x'])):

        if(df['gp'][i]!=gp):
            data.append(temp)
            temp=[]
            temp.append((df['x'][i],df['y'][i]))
            gp=df['gp'][i]
        else:
            temp.append((df['x'][i],df['y'][i]))
    data.append(temp)
    return data
def text_list(df):
    temp=[]
    data=[]
    for i in range(len(df['x'])):
        data.append((df['x'][i],df['y'][i],df['H'][i]))
    #print(data)
    return data

Nfile="NCL14nwa_proj.csv"
Cfile="ICL14nwa_proj.csv"
Ffile="FP14nwa_proj.csv"
Tfile="char14nwa_proj.csv"
file1="SR14nwa_proj.csv"
nlp = pd.read_csv(Nfile, header = 0)
clp = pd.read_csv(Cfile, header = 0)
FP = pd.read_csv(Ffile, header = 0)
T=pd.read_csv(Tfile, header = 0)
f1=pd.read_csv(file1, header = 0)
map=nlp['map'][0]
sname=str(map)+".svg"

data=poly_list(nlp)
data2=poly_list(clp)
data3=poly_list(FP)
data4=text_list(T)
data5=poly_list(f1)

svg_document = svgwrite.Drawing(filename = sname,size = ("937.5px", "750px"))
for d in data:
    svg_document.add(svg_document.polyline(d,stroke=svgwrite.rgb(129,64,0, '%'), fill='none'))
for d in data2:
    svg_document.add(svg_document.polyline(d,stroke=svgwrite.rgb(189,94,0, '%'), fill='none'))
for d in data3:
    svg_document.add(svg_document.polyline(d,stroke=svgwrite.rgb(79,0,79, '%'), fill='none'))
for d in data5:
    svg_document.add(svg_document.polyline(d,stroke=svgwrite.rgb(190,190,190, '%'), fill='none'))
for d in data4:
    svg_document.add(svg_document.text(d[2],insert = (d[0], d[1]),font_size="3px",fill='black'))


#print(svg_document.tostring())

svg_document.save()