# Standard scientific modules:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap
import xray

# My modules:
import atmos.utils as utils
import atmos.xrhelper as xr
import atmos.plots as ap
from atmos.data import set_lon, interp_latlon

# ----------------------------------------------------------------------
# Read monthly mean climatologies and do some test calcs
# ----------------------------------------------------------------------

filename = 'data/more/ncep2_climatology_monthly.nc'
ds = xr.ncload(filename)
lat = ds['lat'].values
lon = ds['lon'].values
plev = ds['plev'].values
mon = ds['mon'].values
u = ds['u'].values
v = ds['v'].values
T = ds['T'].values
ps = ds['ps'].values

#xi, yi = np.meshgrid(lon, lat)
k, mon = 9, 7
uplot = u[mon-1, k]
plt.figure()
m = ap.contourf_latlon(lat, lon, uplot, 10)
ap.contour_latlon(lat, lon, ps[mon-1]/100, 50, m=m, colors='black')

#
# plt.contourf(xi, yi, uplot)
# plt.colorbar()
# plt.contour(xi,yi, uplot, np.arange(-40,60,10), colors='black')

# Zonal mean zonal wind
season='jjas'
lon1, lon2 = 60, 100
pmax = 1100
cint = 5

imon = utils.season_months(season)
ilon = (lon >= lon1) & (lon <= lon2)

uplot = u[imon]
uplot = uplot[:,:,:,ilon]
uplot = uplot.mean(axis=3).mean(axis=0)
#clev = ap.clevels(uplot, cint)

topo = ps.mean(axis=0) / 100
topo = topo[:,ilon].mean(axis=1)

plt.figure()
ap.contour_latpres(lat, plev, uplot, cint, topo=topo)

# ----------------------------------------------------------------------
# Check longitude shifting utility
data = ds['ps'].copy().mean(axis=0)/100
data_new = set_lon(data, lonmax=180)
data_new2 = set_lon(data_new, lonmax=360)

plt.figure(figsize=(7,9))
plt.subplot(3,1,1)
ap.pcolor_latlon(data, cmap='hot')
plt.subplot(3,1,2)
ap.pcolor_latlon(data_new, cmap='hot')
plt.subplot(3,1,3)
ap.pcolor_latlon(data_new2, cmap='hot')

print(np.array_equal(data, data_new))
print(np.array_equal(data, data_new2))

# ----------------------------------------------------------------------
# Interpolating onto new lat-lon grid

lat_new = np.arange(90,-90,-1.)
lon_new = np.arange(0.,360,1.)
data_new = interp_latlon(data, lat, lon, lat_new, lon_new)

plt.figure(figsize=(7,8))
plt.subplot(2,1,1)
ap.pcolor_latlon(lat,lon, data, cmap='hot')
plt.subplot(2,1,2)
ap.pcolor_latlon(lat_new, lon_new, data_new, cmap='hot')

# ----------------------------------------------------------------------
# Check sub-sampling

lat_new = lat[::2]
lon_new = lon[::2]
data_new = interp_latlon(data, lat, lon, lat_new, lon_new)

plt.figure(figsize=(7,8))
plt.subplot(2,1,1)
ap.pcolor_latlon(lat,lon, data, cmap='hot')
plt.subplot(2,1,2)
ap.pcolor_latlon(lat_new, lon_new, data_new, cmap='hot')

print(np.array_equal(data[::2,::2], data_new))
# ----------------------------------------------------------------------
# Getting topography

lat_new = lat
data_new, lon_new = set_lon(data, lon, lonmax=180)

topo = get_topo(lat_new, lon_new)

plt.figure(figsize=(7,8))
plt.subplot(2,1,1)
ap.pcolor_latlon(lat,lon, data, cmap='hot')
plt.subplot(2,1,2)
ap.pcolor_latlon(lat_new, lon_new,topo, cmap='hot')

# ----------------------------------------------------------------------
# Topography test 2

lat_new = np.arange(-90,90,0.5)
lon_new = np.arange(0,360,0.5)
topo = get_topo(lat_new, lon_new)

plt.figure()
ap.pcolor_latlon(lat_new, lon_new, topo, cmap='hot')
