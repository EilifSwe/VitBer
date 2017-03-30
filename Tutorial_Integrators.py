# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:47:10 2017

@author: julie
"""
import numpy as np
def euler(X_now,h,time_now,veloccityField):
    dt=h/np.timedelta64(1,'s')
    dx_dt=velocityField(X_now,time_now) #derivative
    X_next=X_now+dt*h*dx_dt
    return X_next