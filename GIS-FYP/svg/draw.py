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
Nfile="NCL3seb_proj.csv"
Cfile="ICL3seb_proj.csv"
nlp = pd.read_csv(Nfile, header = 0)
clp = pd.read_csv(Cfile, header = 0)
map=nlp['map'][0]
sname=str(map)+".svg"

data=poly_list(nlp)
data2=poly_list(clp)


svg_document = svgwrite.Drawing(filename = sname,size = ("937.5px", "750px"))
for d in data:
    svg_document.add(svg_document.polyline(d,stroke='blue', fill='none'))
for d in data2:
    svg_document.add(svg_document.polyline(d,stroke='red', fill='none'))


print(svg_document.tostring())

svg_document.save()