# Standard scientific modules:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap
import xray
from datetime import datetime
import statsmodels.api as sm

# My modules:
import atmos.utils as utils
import atmos.plots as ap
import atmos.data as dat
import atmos.variables as av
from atmos.utils import print_if
from atmos.constants import const as constants

# ----------------------------------------------------------------------
# Linear regression

n = 100
x = np.linspace(0,10,n)
y = 2*x - 5 + 2*np.random.random(n)
plt.figure()
plt.scatter(x, y)
x_in = sm.add_constant(x)
fit = sm.OLS(y, x_in).fit()

# ----------------------------------------------------------------------
# Multiple linear regression

nobs = 100
x = np.random.random((nobs, 2))
x = sm.add_constant(x)
beta = [1, .1, .5]
e = np.random.random(nobs)
y = np.dot(x, beta) + e
results = sm.OLS(y, x).fit()
print results.summary()
# ----------------------------------------------------------------------
# Read some data from OpenDAP url

url = ('http://goldsmr3.sci.gsfc.nasa.gov/opendap/MERRA_MONTHLY/'
    'MAIMCPASM.5.2.0/1979/MERRA100.prod.assim.instM_3d_asm_Cp.197901.hdf')

ds = xray.open_dataset(url)
T = ds['T']
ps = ds['PS']
q = ds['QV']
plev = dat.get_plev(T, units='Pa')
lat, lon = dat.get_lat(ps), dat.get_lon(ps)

# t, k = 0, 6
# t, k = 0, 22
t, k = 0, 14
pstr = '%d hPa' % (plev[k]/100)

# ----------------------------------------------------------------------
