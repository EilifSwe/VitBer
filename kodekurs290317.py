# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:25:23 2017

@author: julie
"""


'''
Ideer:
    - Skal ta omtrent 1 minutt å laste inn den forste

'''
import Tutorial_ParticleTracking as Tut_Tr
import Tutorial_PlottingFunctions as Tut_Plt
import Tutorial_Integrators as Tut_Int
import testkart2 as Tut_Ex
import Tutorial_UtilityFunctions as Tut_UF
import xarray as xr
import numpy as np
if __name__=='__main__':
    MasterFlag= {
            -1: 'TestSpace',
            0: 'CheckOutInterPolator',
            1: 'PlotOnMap'
    }[0] #dictinary
    if MasterFlag== 'CheckOutInterpolator':
        Tut_Tr.simulateParticlesMoving()
    elif MasterFlag== 'CheckOutInterPolator':
        dataSet=xr.open_dataset('NorKyst-900m.nc')
        Tut_Plt.plotTrajectoryOnMap(dataSet)
    else:
        dataSet=xr.open_dataset('Norkust-800m.nc')
        time_initial=dataSet.time[0]
        time_final=time_inital+np.timedelta64(1,'d')
        print(time_initial)
        h=np.timedelta64(3600,'s')
        velocityField=Tut_Ex.Interpolator(dataSet)
        
        X0=np.array([-3e6,-1.3e6]).reshape(2,1)
        print(Tut_Int.euler(X0,h,time_initial,velocityField))
        
        X1 = Tut_UF.particleTrajectory(X0,time_initial,h,time_final,velocityField,Tut_Int.euler)
        
        print(X1)
    