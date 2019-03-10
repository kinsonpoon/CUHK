import random
import math
import numpy as np
import pandas as pd
 
class NaiveBayes(object):
    def __init__(self):
        self.X=[]
        self.y=[]
        self.features=['actual_weight', 'declared_horse_weight','race_distance', 'trainer_ave_rank', 'jockey_ave_rank','recent_ave_rank']
        self.summaries[0]['actual_weight']=[]
        self.summaries[0]['declared_horse_weight']=[]
        self.summaries[0]['race_distance']=[]
        self.summaries[0]['trainer_ave_rank']=[]
        self.summaries[0]['jockey_ave_rank']=[]
        self.summaries[0]['recent_ave_rank']=[]
        self.summaries[1]['actual_weight']=[]
        self.summaries[1]['declared_horse_weight']=[]
        self.summaries[1]['race_distance']=[]
        self.summaries[1]['trainer_ave_rank']=[]
        self.summaries[1]['jockey_ave_rank']=[]
        self.summaries[1]['recent_ave_rank']=[]
    def fit(self,X,y):
        self.X=X
        self.y=y
        for i in range(len(self.y)):
            if(self.y[i]=="0"):
                for item in self.features:
                    self.summaries[0][item].append(self.X[item])
            else:
                for item in self.features:
                    self.summaries[1][item].append(self.X[item])
        list[0]=[]
        list[1]=[]
        for item in self.features:
            list[0].append([np.mean(self.summaries[0][item]),np.std(self.summaries[0][item])])
            list[1].append([np.mean(self.summaries[0][item]),np.std(self.summaries[0][item])])
    def calculateProbability(x):
        exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
        return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
        