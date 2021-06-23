#rwspy
#from .a2 import * 
import pandas as pd
import numpy as np
import seaborn as sns
import csv, math, pathlib, os.path

# import scipy.stats as stats

#>>> ds = groot.link('trip_data','model_data_train.csv','y')
#from groot.stops import Stops

def link(
    data_matrix = None,
    dataset = None,
    target_vector = None,
 #   time_delta = 3,
 #   angle_delta = 30,
):
    from groot.ws import Dataset
    return Dataset(
        data_matrix,
        dataset,
        target_vector,
#        time_delta,
#        angle_delta,
        )


if __name__ == "__main__":
    import groot.__main__
    __main__.main()

"""
td = groot.link('model_data_train.csv', 'trip_data', 'y')
td_ = groot.link('model_data_test.csv', 'work_sample_test_trips')
task = groot.ws.Task(train=td, test=td_)
task.ds['train'].trip(0)
t0 = task.ds['train'].trip(0)
task.ds['train'].turns().delta(t0)
"""
