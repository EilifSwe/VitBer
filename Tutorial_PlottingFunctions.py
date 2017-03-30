# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:30:05 2017

@author: julie
"""
import numpy as np
from matplotlib import pyplot as plt

import cartopy.crs as ccrs
import cartopy.feature as cfeature

# library for coordinate transformations
import pyproj
def plotTrajectoryOnMap(dataSet):
    