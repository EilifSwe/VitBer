import numpy as np
from matplotlib import pyplot as plt
import xarray as xr
from scipy.interpolate import RectBivariateSpline
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pyproj

import DiffSolver as DS
import testkart2 as TK

def plotOnMap(list, d):
    fig = plt.figure(figsize=(12,8))
    ax  = plt.axes(projection=ccrs.NorthPolarStereo())
    land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m', color = '#dddddd')
    ax.add_feature(land_10m)
    ax.coastlines(resolution='10m')
    p1 = pyproj.Proj(d.projection_stere.proj4)
    p2 = pyproj.Proj(proj='latlong')
    lons, lats = pyproj.transform(p1, p2, list[0,:], list[1,:])
    
    ax.scatter(lons, lats, transform=ccrs.PlateCarree(), zorder=2, marker = '.')
    
    ax.set_extent((-3, 7, 58, 62))

def plotWithGrid(list, d):
    Nx, Ny = 200, 200
    x = -3010000 + 800 * np.arange(Nx)
    y = -1210000 + 800 * np.arange(Ny)
    
    x, y = np.meshgrid(x, y)
    
    C = np.array([np.zeros(Nx) for i in range(Ny)])
    for p in range(len(list[0])):
        C[int((list[1,p] + 1210000)//800), int((list[0,p] + 3010000)//800)]+= 1
    #C = (x + 2950000)**2 + (y + 1150000)**2
    
    fig = plt.figure(figsize=(12,8))
    ax  = plt.axes(projection=ccrs.NorthPolarStereo())
    land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m', color = '#dddddd')
    ax.add_feature(land_10m)
    ax.coastlines(resolution='10m')
    p1 = pyproj.Proj(d.projection_stere.proj4)
    p2 = pyproj.Proj(proj='latlong')
    lons, lats = pyproj.transform(p1, p2, x, y)
    
    cax = ax.pcolormesh(lons, lats, C, transform=ccrs.PlateCarree(), zorder=2, cmap='hot_r')
    cbar = fig.colorbar(cax, ax = ax, extend = 'both')
    
    ax.set_extent((-3, 7, 58, 62))
    
    

def plotParticlePos(grid):
    Np = 10000
    totalTime = 10*24*3600
    h = 3600
    N = totalTime//h
    xMin=-3010000
    xMax=-2990000
    yMin=-1210000
    yMax=-1190000
    deltaX = xMax - xMin
    deltaY = yMax - yMin
    xList = [xMin + np.random.random() * deltaX for i in range(Np)]
    yList = [yMin + np.random.random() * deltaY for i in range(Np)]
    particleList = np.array(xList + yList).reshape(2, Np)
    
    t0 = np.datetime64('2017-02-01T12:00:00')
    d  = xr.open_dataset('NorKyst-800m.nc')
    f  = TK.Interpolator(dataset=d)

    
    for i in range(0, N):
        if(i % (2*24) == 0):
            print(i//24)
            if(grid):
                plotWithGrid(particleList, d)
            else:
                plotOnMap(particleList, d)
        particleList = DS.trapezoidStep(t0 + i*h, h, particleList, f)
    
    if(grid):
        plotWithGrid(particleList, d)
    else:
        plotOnMap(particleList, d)
    plt.style.use('bmh')
    plt.show()
    
    
    
    
    