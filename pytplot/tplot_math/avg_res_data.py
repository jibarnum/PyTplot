import pytplot
import pydivide
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d
import pandas as pd

#AVERAGE AT RESOLUTION
#take average of column over discrete periods of time
def avg_res_data(tvar1,res,new_tvar):
    #grab info from tvar
    df = pytplot.data_quants[tvar1].data
    time = df.index
    start_t = df.index[0]
    end_t = df.index[-1]
    df_index = list(df.columns)
    #create list of times spanning tvar range @ specified res
    res_time = np.arange(start_t,end_t+1,res)
    new_res_time = np.array([])
    #find closest time to new resolution times
    for t in res_time:
        if t not in time:
            tdiff = abs(time-t)
            new_res_time = np.append(new_res_time,time[tdiff.argmin()])
        else:
            new_res_time = np.append(new_res_time,t)
    #make sure no duplicate times from resolution time rounding
    new_res_time = np.unique(new_res_time)
    #shift start time array
    start_t = np.roll(new_res_time,1)
    end_t = new_res_time
    start_t = np.delete(start_t,0)
    end_t = np.delete(end_t,0)
    #initialize arrays
    avg_bin_data = []
    avg_bin_time = np.array([])
    #for each time bin
    for it,t in enumerate(start_t):
        #for each data column
        data_avg_bin = np.array([])
        for i in df_index:
            #append localized bin average to data_avg_bin
            data_avg_bin = np.append(data_avg_bin,[(df.loc[start_t[it]:end_t[it]])[i].mean()])
        #append whole array of bin averages (over n columns) to avg_bin_data
        avg_bin_data = avg_bin_data + [data_avg_bin.tolist()]
        avg_bin_time = np.append(avg_bin_time,t)
    #store data in new_tvar
    pytplot.store_data(new_tvar, data={'x':avg_bin_time,'y':avg_bin_data})
    return new_tvar    