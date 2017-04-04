import numpy as np
from matplotlib import pyplot as plt
import xarray as xr
from scipy.interpolate import RectBivariateSpline
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pyproj

import DiffSolver as DS
import Interpolator_Class as IC

def plotOnMap(list, d):
    fig = plt.figure(figsize=(12, 8))
    ax  = plt.axes(projection=ccrs.NorthPolarStereo())
    land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m',color = '#dddddd')
    ax.add_feature(land_10m)
    ax.coastlines(resolution='10m')

    p1 = pyproj.Proj(d.projection_stere.proj4)
    p2 = pyproj.Proj(proj='latlong')
    lons, lats = pyproj.transform(p1, p2, list[0,:], list[1,:])
    
    ax.scatter(lons, lats, transform=ccrs.PlateCarree(), zorder=2, marker = '.')
    
    ax.set_extent((0, 6, 59, 61))

def plotAllOnMap(list):
    land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m', color='#dddddd')
    plt.style.use('bmh')
    t0 = np.datetime64('2017-02-01T12:00:00')
    d = xr.open_dataset('NorKyst-800m.nc')
    f = IC.Interpolator(dataset=d)
    totalTime = 10 * 24 * 3600
    h = 3600
    N = totalTime // h
    p1 = pyproj.Proj(d.projection_stere.proj4)
    p2 = pyproj.Proj(proj='latlong')
    counter=0
    countlist=[321,322,323,324,325,326]

    for i in range(0, N+1):
        if (i % (2 * 24) == 0):
            print(i // 24)
            ax = plt.subplot(countlist[counter], projection=ccrs.NorthPolarStereo())
            ax.add_feature(land_10m)
            ax.coastlines(resolution='10m')
            ax.set_extent((0, 6, 59, 61))
            lons, lats = pyproj.transform(p1, p2, list[0, :], list[1, :])
            ax.scatter(lons, lats, transform=ccrs.PlateCarree(), zorder=2, marker='.')
            counter += 1
        list = DS.trapezoidStep(t0 + i * h, h, list, f)

    '''
    #Nr 1:
    plt.subplot(321)
    list = DS.trapezoidStep(t0 + 0 * 24*h, h, list, f)
    lons, lats = pyproj.transform(p1, p2, list[0, :], list[1, :])
    ax.scatter(lons, lats, transform=ccrs.PlateCarree(), zorder=2, marker='.')

    #nr 2:
    plt.subplot(322)
    list = DS.trapezoidStep(t0 + 2 *24* h, h, list, f)
    lons, lats = pyproj.transform(p1, p2, list[0, :], list[1, :])

    ax.scatter(lons, lats, transform=ccrs.PlateCarree(), zorder=2, marker='.')
    
    #Nr 3:
    plt.subplot(323)
    list = DS.trapezoidStep(t0 + 4 *24* h, h, list, f)
    lons, lats = pyproj.transform(p1, p2, list[0, :], list[1, :])

    ax.scatter(lons, lats, transform=ccrs.PlateCarree(), zorder=2, marker='.')


    #nr 4:
    plt.subplot(324)
    list = DS.trapezoidStep(t0 + 6 * 24*h, h, list, f)
    lons, lats = pyproj.transform(p1, p2, list[0, :], list[1, :])

    ax.scatter(lons, lats, transform=ccrs.PlateCarree(), zorder=2, marker='.')

    #nr 5:
    plt.subplot(325)
    list = DS.trapezoidStep(t0 + 8 *24* h, h, list, f)
    lons, lats = pyproj.transform(p1, p2, list[0, :], list[1, :])

    ax.scatter(lons, lats, transform=ccrs.PlateCarree(), zorder=2, marker='.')

    #nr: 6
    plt.subplot(326)
    list = DS.trapezoidStep(t0 + 10 *24* h, h, list, f)
    lons, lats = pyproj.transform(p1, p2, list[0, :], list[1, :])

    ax.scatter(lons, lats, transform=ccrs.PlateCarree(), zorder=2, marker='.')
    '''


def plotWithGrid(list, d):
    Nx, Ny = 200, 200
    x = -3010000 + 800 * np.arange(Nx)
    y = -1210000 + 800 * np.arange(Ny)
    
    x, y = np.meshgrid(x, y)
    
    C = np.array([np.zeros(Nx) for i in range(Ny)])
    for p in range(len(list[0])):
        C[int((list[1,p] + 1210000)//800), int((list[0,p] + 3010000)//800)]+= 1

    
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
    
    
    

def plotParticlePos(grid,allOnMap):
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
    print(particleList)
    print("hei")

    if allOnMap:
        plotAllOnMap(particleList)
        plt.savefig("Concentration_3a_all.pdf")
    else:
        t0 = np.datetime64('2017-02-01T12:00:00')
        d  = xr.open_dataset('NorKyst-800m.nc')
        f  = IC.Interpolator(dataset=d)

        fig= plt.subplots()
        plt.style.use('bmh')
        counter=1
        for i in range(0, N):
            if(i % (2*24) == 0):
                print(i//24)
                if(grid):

                    plotWithGrid(particleList, d)
                    plt.savefig("ConcentrationGrid_oppg3b"+str(i)+".pdf")
                    counter+=1

                else:
                    plotOnMap(particleList, d)
                    plt.savefig("Concentration_oppg3a"+str(i)+".pdf")
                    counter+=1
            particleList = DS.trapezoidStep(t0 + i*h, h, particleList, f)

        if(grid):
            plotWithGrid(particleList, d)
            plt.savefig("ConcentrationGrid_oppg3b_end.pdf")

        else:
            plotOnMap(particleList, d)
            plt.savefig("Concentration_oppg3a_end.pdf")

    
    
    plt.show()