from . import tplot_common
from . import tplot_utilities


def get_timespan(name):
    if name not in tplot_common.data_quants.keys():
        print("That name is currently not in pytplot") 
        return
    print("Start Time: " + tplot_utilities.int_to_str(tplot_common.data_quants[name].trange[0]))
    print("End Time:   " + tplot_utilities.int_to_str(tplot_common.data_quants[name].trange[1]))
    
    return(tplot_common.data_quants[name].trange[0], tplot_common.data_quants[name].trange[1])