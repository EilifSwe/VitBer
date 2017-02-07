# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:00:21 2017
@author: julie
"""

#halveringsmetoden
import Parametere as par

def halvering(sLow,sHigh,f, x, A, fLow,fHigh): 
    
    sMid=(sLow+sHigh)/2 #midtpunktet
    fMid=f(x, sMid, A) #funksjonsverdi i midtpunktet
    if fMid==0:
        return sMid, sMid, fLow, fHigh
    
    elif(fMid*fLow < 0):
        sHigh = sMid
        fHigh=fMid #Denne verdien skal oppdateres
        
    elif(fMid*fHigh<0):
        sLow = sMid
        fLow=fMid #Denne verdien skal oppdateres
    
    return sLow, sHigh, fLow, fHigh

def finn_sigma(sLow, sHigh, temp, x, A):
    fLow=temp(x, sLow, A)
    fHigh=temp(x,sHigh,A)
    fHigh=-100
    while (abs(sHigh-sLow)>par.TOL):
        sLow, sHigh,fLow,fHigh=halvering(sLow,sHigh,temp, x, A,fLow,fHigh)
        #print("Sigma: ", sLow, sHigh)
        
    return (sLow+sHigh)/2
