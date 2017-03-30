# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:33:06 2017

@author: julie
"""
import xarray as xr
import numpy as np
import Tutorial_ExampleFileFromWiki as Tut_Ex

def simulateParticlesMoving():
    dataPath='NorKyst-800m.nc'
    dataSet=xr.open_dataset(dataPath) #år tilgang på innhold
    
    velocityField=Tut_Ex.Interpolator(dataset=dataSet)
    #To test the object
    time=dataSet.time[3]
    
    X=np.array([-3e6,-1.3e6]).reshape(2,1) #make to column
    print(velocityField,X,time)
    