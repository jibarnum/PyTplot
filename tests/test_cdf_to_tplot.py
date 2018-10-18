import pytplot

def test_cdf_euv_read():
    pytplot.cdf_to_tplot("C:/Code Repos/PyTplot/tests/testfiles/mvn_euv_l2_bands_20170619_v09_r03.cdf")
    pytplot.tplot(0, testing=True)

def test_cdf_swe_read():
    pytplot.cdf_to_tplot("C:/Code Repos/PyTplot/tests/testfiles/mvn_swe_l2_svyspec_20170619_v04_r04.cdf")
    pytplot.options('diff_en_fluxes', 'colormap', 'magma')
    pytplot.options('diff_en_fluxes', 'ztitle', 'FLUX')
    pytplot.options('diff_en_fluxes', 'ytitle', 'Energy')
    pytplot.options("diff_en_fluxes", "spec", 1)
    pytplot.options("diff_en_fluxes", "crosshair_y", "banana")
    pytplot.options("diff_en_fluxes", "crosshair_z", "tomato")
    pytplot.options("diff_en_fluxes", 'panel_size', 1)
    pytplot.options('diff_en_fluxes', 'ylog', 1)
    pytplot.options('diff_en_fluxes', 'zlog', 1)
    pytplot.tplot(1, testing=True)