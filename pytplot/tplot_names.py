from . import tplot_common

def tplot_names():
    for key, _ in tplot_common.data_quants.items():
        if isinstance(tplot_common.data_quants[key].data, list):
            if isinstance(key, int):
                names_to_print = tplot_common.data_quants[key].name + "  data from: "
                for name in tplot_common.data_quants[key].data:
                    names_to_print = names_to_print + " " + name
                print(key, ":", names_to_print)
        else:
            if isinstance(key, int):
                names_to_print = tplot_common.data_quants[key].name
                print(key, ":", names_to_print)
        
    return