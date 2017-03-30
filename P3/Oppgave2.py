# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:17:47 2017

@author: julie
"""

import numpy as np
from matplotlib import pyplot as plt
import xarray as xr
from scipy.interpolate import RectBivariateSpline
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pyproj

import Oppgave1 as O1
import DiffSolver as DS
import testkart2 as TK

def plotPath(map):
    totalTime = 10*24*3600
    h = 3600
    xcoord=-3000000
    ycoord=-1200000
    X0 = np.array([xcoord, ycoord]).reshape(2,1)
    
    t0 = np.datetime64('2017-02-01T12:00:00')
    t1 = np.datetime64('2017-02-05T12:00:00')
    t2 = np.datetime64('2017-02-10T12:00:00')
    
    d  = xr.open_dataset('NorKyst-800m.nc')
    f  = TK.Interpolator(dataset=d)
  
    N = totalTime//h
    print("Lasting ferdig", N)
    
    dt = totalTime//N
    X1 = np.asarray([np.zeros(2).reshape(2,1) for i in range(N+1)])
    X2 = np.asarray([np.zeros(2).reshape(2,1) for i in range(N+1)])
    X3 = np.asarray([np.zeros(2).reshape(2,1) for i in range(N+1)])

    X1[0] = X0
    X2[0] = X0
    X3[0] = X0
    
    for i in range(0, N):
        print(i)
        X1[i+1] = DS.trapezoidStep(t0 + i*dt, dt, X1[i], f)
        X2[i+1] = DS.trapezoidStep(t1 + i*dt, dt, X2[i], f)
        X3[i+1] = DS.trapezoidStep(t2 + i*dt, dt, X3[i], f)
        
    
    if(map):
        fig = plt.figure(figsize=(12,8))
        ax  = plt.axes(projection=ccrs.NorthPolarStereo())
        land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m', color = '#dddddd')
        ax.add_feature(land_10m)
        ax.coastlines(resolution='10m')
        p1 = pyproj.Proj(d.projection_stere.proj4)
        p2 = pyproj.Proj(proj='latlong')
        lons0, lats0 = pyproj.transform(p1, p2, X1[:,0,0], X1[:,1,0])
        lons1, lats1 = pyproj.transform(p1, p2, X2[:,0,0], X2[:,1,0])
        lons2, lats2 = pyproj.transform(p1, p2, X3[:,0,0], X3[:,1,0])
        
        ax.plot(lons0, lats0, transform=ccrs.PlateCarree(), zorder=2)
        ax.plot(lons1, lats1, transform=ccrs.PlateCarree(), zorder=2)
        ax.plot(lons2, lats2, transform=ccrs.PlateCarree(), zorder=2)
        
        ax.set_extent((-5, 15, 57, 67))
    else:
        plt.plot(X1[:,0,0], X1[:,1,0])
        plt.plot(X2[:,0,0], X2[:,1,0])
        plt.plot(X3[:,0,0], X3[:,1,0])
        
   
    
    
    plt.style.use('bmh')
    #plt.plot(X[:,0,0],X[:,1,0])
    plt.show()
