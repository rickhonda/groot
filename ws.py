import pandas as pd
import numpy as np
import seaborn as sns
import csv, math, pathlib, os.path

from groot.stops import Stops
from groot.turns import Turns

class WorkSample:
    def __init__(self):
        self.time_delta = 3
        self.angle_delta = 45 #60?
        self.pearson = pd.read_csv('groot/pearson.csv')

class Dataset(WorkSample):
    def __init__(
        self,
        data_matrix,
        dataset,
        target_vector,
        ):
        super().__init__()
        self.data_matrix = pd.read_csv(data_matrix)
        self.dataset = dataset
        self.target = target_vector

    def filename(self,b):
        return self.data_matrix['filename'][b]

    def trip(self,n):
#        return pd.read_csv(self.dataset + '/' + self.filename(n))
        return pd.read_csv(self.dataset + '/' + self.data_matrix['filename'][n])

#    def flip(self,n):
#        return pd.read_csv(self.dataset + '/' + self.data_matrix['filename'][n]
    
#    def reformat(self,df): 
#        pass

#>>> asdf = pd.read_csv(td.dataset + "/" + td.data_matrix['filename'][0])


# >>>train.stops(0,30,3).trip(0)

    def stops(
        self, 
        margin_start = 30,
        margin_end = 30,
        stop_speed = 3,
        ):
        return Stops(
            self,
            self.time_delta,
            margin_start,
            margin_end,
            stop_speed,
            )

    def turns(self):
        return Turns(
            self,
            self.angle_delta,
            )

#>>> asdf.ds['train'].collect_sigs(300,'0.05')
    def collect_sigs(self, degrees_of_freedom, sig):
        cores = self.data_matrix.iloc[:degrees_of_freedom+2,].corr()['y'].iloc[:-1,]
        p = self.pearson
        cores = pd.DataFrame(cores.reset_index())

        pp = p[p['deg_f'] ==degrees_of_freedom][sig].iloc[0]
        L = []
        c = 0
        for i in range(len(cores)): 
            if abs(cores.iloc[i]['y']) > pp:
                L.append(cores.iloc[i]['index'])
        return L

    def prune_h0(self): 
        pass
        

#>>> Xt = dt.data_matrix.loc[:,sigs]

#  prob_1 = lambda F :  X.groupby([F]).size().div(len(X))

#>>> asdf = groot.ws.Z(train = dtrain, test = dtest)

class Task:
    def __init__(self, **datasets):
        self.ds = datasets
    def __repr__(self):
        return 'task{!r}'.format(self.ds)

    def collect_sigs(self, degrees_of_freedom, sig, ds_train):
        cores = self.ds[ds_train].data_matrix.iloc[:degrees_of_freedom+2,].corr()['y'].iloc[:-1,]
        p = self.ds[ds_train].pearson
        cores = pd.DataFrame(cores.reset_index())
        pp = p[p['deg_f'] ==degrees_of_freedom][sig].iloc[0]
        L = []
        c = 0
        for i in range(len(cores)): 
            if abs(cores.iloc[i]['y']) > pp:
                L.append(cores.iloc[i]['index'])
        return L

    def prune_h0(self): 
        pass
    
    def chop_dataframe(self):
        pass
