# -*- coding: utf-8 -*-


import numpy as np
from matplotlib import pyplot as plt
import xarray as xr
from scipy.interpolate import RectBivariateSpline
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pyproj

import Oppgave1 as O1
import DiffSolver as DS
import Interpolator_Class as IC

#Plotter en partikkels bane for 3 ulike tidspunkt, og 3 partikler på ulike steder til samme tid.
def plotPath(map):
    totalTime = 10*24*3600
    h = 3600
    xcoord0=-3000000
    ycoord0=-1200000
    xcoord1=-3000000
    ycoord1=-1200000
    xcoord2=-3000000
    ycoord2=-1200000
    
    
    
    t0 = np.datetime64('2017-02-01T12:00:00')
    t1 = np.datetime64('2017-02-05T12:00:00')
    t2 = np.datetime64('2017-02-10T12:00:00')
    
    if(map):
        xcoord0=-3000000
        ycoord0=-1200000
        xcoord1=-3000000
        ycoord1=-1300000
        xcoord2=-3000000
        ycoord2=-1400000
        t1 = np.datetime64('2017-02-01T12:00:00')
        t2 = np.datetime64('2017-02-01T12:00:00')
    
    d  = xr.open_dataset('NorKyst-800m.nc')
    f  = IC.Interpolator(dataset=d)
  
    N = totalTime//h
    print("Lasting ferdig", N)
    
    dt = totalTime//N
    X1 = np.asarray([np.zeros(2).reshape(2,1) for i in range(N+1)])
    X2 = np.asarray([np.zeros(2).reshape(2,1) for i in range(N+1)])
    X3 = np.asarray([np.zeros(2).reshape(2,1) for i in range(N+1)])

    X1[0] = np.array([xcoord0, ycoord0]).reshape(2,1)
    X2[0] = np.array([xcoord1, ycoord1]).reshape(2,1)
    X3[0] = np.array([xcoord2, ycoord2]).reshape(2,1)
    
    for i in range(0, N):
        print(i)
        X1[i+1] = DS.trapezoidStep(t0 + i*dt, dt, X1[i], f)
        X2[i+1] = DS.trapezoidStep(t1 + i*dt, dt, X2[i], f)
        X3[i+1] = DS.trapezoidStep(t2 + i*dt, dt, X3[i], f)
        
    
    if(map): #Plotter på kart med 3 ulike startposisjoner.
        fig = plt.figure(figsize=(12,8))
        ax  = plt.axes(projection=ccrs.NorthPolarStereo())
        land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m', color = '#dddddd')
        ax.add_feature(land_10m)
        ax.coastlines(resolution='10m')
        # Transformerer fra x,y til lat,long:
        p1 = pyproj.Proj(d.projection_stere.proj4)
        p2 = pyproj.Proj(proj='latlong')
        lons0, lats0 = pyproj.transform(p1, p2, X1[:,0,0], X1[:,1,0])
        lons1, lats1 = pyproj.transform(p1, p2, X2[:,0,0], X2[:,1,0])
        lons2, lats2 = pyproj.transform(p1, p2, X3[:,0,0], X3[:,1,0])

        ax.plot(lons0, lats0, transform=ccrs.PlateCarree(), zorder=2, label=("%.2f"%lons0[0],u'\u00b0' + " E" ,"%.2f"%lats0[0],u'\u00b0'+" N"))
        ax.plot(lons1, lats1, transform=ccrs.PlateCarree(), zorder=2, label=("%.2f"%lons1[0],u'\u00b0'+ " E" ,"%.2f"%lats1[0],u'\u00b0'+" N"))
        ax.plot(lons2, lats2, transform=ccrs.PlateCarree(), zorder=2, label=("%.2f"%lons2[0],u'\u00b0'+ " E" ,"%.2f"%lats2[0],u'\u00b0' +" N"))
        plt.legend()
        ax.set_extent((-3, 7, 58, 62)) #kartutsnittets størrelse.
    
        plt.savefig("BaneMap_oppg2a.pdf")

    else:   #Partikler med lik startposisjon til forskjellig tid.
        plt.figure()
        plt.plot(X1[:,0,0], X1[:,1,0],label="$t_0$ = 1. Feb")
        plt.plot(X2[:,0,0], X2[:,1,0],label="$t_0$= 5. Feb")
        plt.plot(X3[:,0,0], X3[:,1,0],label="$t_0$= 10. Feb")
        plt.title("Partikkelbane ved ulike $t_0$.",fontsize=15)
        plt.xlabel("Posisjon, $x$ (m)",fontsize=15)
        plt.ylabel("Posisjon, $y$ (m)",fontsize=15)
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.ticklabel_format(useOffset=False, style='sci',axis='y',scilimits=(0,0))
        plt.legend(loc=2)
        
        plt.savefig("BaneNormal_oppg2a.pdf")
        
        
   
    
    
    plt.style.use('bmh')
    #plt.plot(X[:,0,0],X[:,1,0])
    plt.show()
