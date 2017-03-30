# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:02:03 2017

@author: julie
"""
import numpy as np


def particleTrajectory(X_initial,time_initial,h,time_final,velocityField,integrator):
    numberOfTimeSteps=int((time_final-time_initial)/h)
    X=np.zeros((numberOfTimeSteps+1+1,*X0.shape))
    
    X[0,:]=X_initial
    time_now=time_initial
    
    for step in range(numberOfTimeSteps + 1):
        h=min(h,time_final-time_now)
        time_now+=h #legger til ny skrittlengde i tid
        
        X[step+1,:] = integrator(X[step,:],h,time_now,velocityField)
    