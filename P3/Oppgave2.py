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



def plotPath():
    N = 20
    L = 100
    totalTime = 10*24*3600
    xcoord=-3000000
    ycoord=-1200000
    X0 = np.array([xcoord, ycoord]).reshape(2,1)
    t0 = np.datetime64('2017-02-01T12:00:00')
    
    datapath = 'NorKyst-800m.nc'
    d  = xr.open_dataset(datapath)
    f=TK.Interpolator(dataset=d)
    
    
    XEuler = DS.forwardEuler(N, totalTime, t0, X0, f)
    XTrapezoid = DS.trapezoid(N, totalTime, t0, X0, f)
    
    plt.figure()
    plt.plot(XEuler[:,0],XEuler[:,1])
    plt.plot(XTrapezoid[:,0],XTrapezoid[:,1])
    
    plt.show()
