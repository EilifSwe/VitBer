import numpy as np
from matplotlib import pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pyproj

import DiffSolver as DS
import Interpolator_Class as IC

#Plotte 1 figur
def plotOnMap(list, d):
    fig = plt.figure(figsize=(12, 8))
    ax  = plt.axes(projection=ccrs.NorthPolarStereo())
    land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m',color = '#dddddd')
    ax.add_feature(land_10m)
    ax.coastlines(resolution='10m')

    p1 = pyproj.Proj(d.projection_stere.proj4)
    p2 = pyproj.Proj(proj='latlong')
    lons, lats = pyproj.transform(p1, p2, list[0,:], list[1,:])
    
    ax.scatter(lons, lats, transform=ccrs.PlateCarree(), zorder=2, marker = '.',c='b')
    
    ax.set_extent((0, 6, 59, 61))
    
#6 subplots for oppg 3a)
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

    for i in range(0, 5):
        if (i % (2 * 24) == 0):
            print(i // 24)
            ax = plt.subplot(countlist[counter],projection=ccrs.NorthPolarStereo())
            ax.add_feature(land_10m)
            ax.coastlines(resolution='10m')
            ax.set_extent((0, 6, 59, 61))
            ax.set_title("Dag " + str(int(i/24)))
            lons, lats = pyproj.transform(p1, p2, list[0, :], list[1, :])
            ax.scatter(lons, lats, transform=ccrs.PlateCarree(), zorder=2, marker='.', c='r')
            counter += 1
        list = DS.trapezoidStep(t0 + i * h, h, list, f)
    print("Done plotting.")


#plotte enkeltvis med konsentrasjon, 3b)
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
    land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m', color='#dddddd')
    ax.add_feature(land_10m)
    ax.coastlines(resolution='10m')
    p1 = pyproj.Proj(d.projection_stere.proj4)
    p2 = pyproj.Proj(proj='latlong')
    lons, lats = pyproj.transform(p1, p2, x, y)

    cax = ax.pcolormesh(lons, lats, C, transform=ccrs.PlateCarree(), zorder=2, cmap='hot_r')
    cbar = fig.colorbar(cax, ax = ax, extend = 'both')
    
    ax.set_extent((-3, 7, 58, 62))
    
#Plotte 6 subplots med konsentrasjon, oppg3a),    
def plotWithGridAll3b(list):
    Nx, Ny = 200, 200
    x = -3010000 + 800 * np.arange(Nx)
    y = -1210000 + 800 * np.arange(Ny)

    totalTime = 10 * 24 * 3600
    h = 3600
    N = totalTime // h

    x, y = np.meshgrid(x, y)

    t0 = np.datetime64('2017-02-01T12:00:00')
    d = xr.open_dataset('NorKyst-800m.nc')
    f = IC.Interpolator(dataset=d)
    plt.style.use('bmh')

    p1 = pyproj.Proj(d.projection_stere.proj4)
    p2 = pyproj.Proj(proj='latlong')
    land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m', color='#dddddd')
    counter = 0
    countlist = [321, 322, 323, 324, 325, 326]
    fig=plt.figure()
    for i in range(0, N+1):
        if (i % (2 * 24) == 0):
            print(i // 24)
            C = np.array([np.zeros(Nx) for i in range(Ny)])
            for p in range(len(list[0])):
                C[int((list[1, p] + 1210000) // 800), int((list[0, p] + 3010000) // 800)] += 1
            ax = plt.subplot(countlist[counter],projection=ccrs.NorthPolarStereo())
            ax.add_feature(land_10m)
            ax.coastlines(resolution='10m')
            ax.set_extent((1.1, 3.3, 59.4, 60.7))
            ax.set_title("Dag " + str(int(i/24)))
            lons, lats = pyproj.transform(p1, p2, x, y)
            cax = ax.pcolormesh(lons, lats, C, transform=ccrs.PlateCarree(), zorder=2, cmap='hot_r')
            counter += 1
        list = DS.trapezoidStep(t0 + i * h, h, list, f)
    print("Done computing. Plotting left.")
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    cbar = fig.colorbar(cax, cax=cbar_ax)


#Plotte partiklene i 3a) og 3b).
#
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


    if (allOnMap and not grid): #Subplots, oppg 3a)
        plotAllOnMap(particleList)
        #justerer subplottenes plassering
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=-0.5, hspace=None)
        plt.savefig("Concentration_3a_all.pdf")
        
    elif (allOnMap and grid):   #subplots (med konsentrasjon), oppg 3b)
        plotWithGridAll3b(particleList)
        #justerer subplottenes plassering
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=-0.7, hspace=None)
        plt.savefig("Concentration_3b_all.pdf")

    else:   #enkeltplott
        t0 = np.datetime64('2017-02-01T12:00:00')
        d  = xr.open_dataset('NorKyst-800m.nc')
        f  = IC.Interpolator(dataset=d)

        fig= plt.subplots()
        plt.style.use('bmh')
        counter=1
        for i in range(0, N):
            if(i % (2*24) == 0):
                print(i//24)
                if(grid):   #Med konsentrasjon, oppg 3b)

                    plotWithGrid(particleList, d)
                    plt.savefig("ConcentrationGrid_oppg3b"+str(i)+".pdf")
                    counter+=1

                else:      #oppg 3a)
                    plotOnMap(particleList, d)
                    plt.savefig("Concentration_oppg3a"+str(i)+".pdf")
                    counter+=1
            particleList = DS.trapezoidStep(t0 + i*h, h, particleList, f)

        if(grid):   #Siste dag, oppg 3b)
            plotWithGrid(particleList, d)
            plt.savefig("ConcentrationGrid_oppg3b_end.pdf")

        else:       #Siste dag, oppg 3a)
            plotOnMap(particleList, d)
            plt.savefig("Concentration_oppg3a_end.pdf")

    plt.show()
