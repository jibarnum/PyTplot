# Copyright 2017 Regents of the University of Colorado. All Rights Reserved.
# Released under the MIT license.
# This software was developed at the University of Colorado's Laboratory for Atmospheric and Space Physics.
# Verify current version before use at: https://github.com/MAVENSDC/PyTplot

import pickle
from . import tplot_common

def tplot_save(names, filename=None):
    
    if not isinstance(names, list):
        names = [names]
    
    #Check that we have all available data
    for name in names: 
        if isinstance(tplot_common.data_quants[name].data, list):
            for data_name in tplot_common.data_quants[name].data:
                if data_name not in names:
                    names.append(data_name)
    
    #Pickle it up
    to_pickle =[]
    for name in names:    
        if name not in tplot_common.data_quants.keys():
            print("That name is currently not in pytplot") 
            return
        to_pickle.append(tplot_common.data_quants[name])
    
    num_quants = len(to_pickle)
    to_pickle = [num_quants] + to_pickle
    temp_tplot_opt_glob = tplot_common.tplot_opt_glob
    to_pickle.append(temp_tplot_opt_glob)
    
    if filename==None:
        filename='var_'+'-'.join(names)+'.pytplot'
    
    pickle.dump(to_pickle, open(filename, "wb"))
    
    return