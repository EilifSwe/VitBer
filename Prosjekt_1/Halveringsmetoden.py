# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:00:21 2017
@author: julie
"""

#halveringsmetoden
import Parametere as par

def halvering(sLow,sHigh,f, x, A): 
    
    sMid=(sLow+sHigh)/2 #midtpunktet
    if f(x, sMid, A)==0:
        return sLow, sHigh

    elif (f(x, sMid, A)*f(x, sLow, A)<0):
        sLow = sLow
        sHigh = sMid
    elif(f(x, sMid, A)*f(x, sHigh, A)<0):
        sLow = sMid
        sHigh = sHigh
    return sLow, sHigh

def finn_sigma(sLow, sHigh, temp, x, A):
    while (abs(sHigh-sLow)>par.TOL):
        sLow, sHigh=halvering(sLow,sHigh,temp, x, A)
        
    return (sLow+sHigh)/2