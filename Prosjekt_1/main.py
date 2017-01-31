# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:55:44 2017

@author: julie
"""

import numpy as np
import matplotlib.pyplot as plt

import SpektralDiskretisering as SD

import Halveringsmetoden as HM

import Numeriskintegral as NI





def temperatur(x,sigma,my,ua,ub,A, U_AVG):

    

    B=SD.calculate_B_Vector(x,my,sigma,ua,ub)

    

    y=SD.calculate_U_Vector(A,B)
    

    u_avg=NI.average(x,y)
    print("u_avg:", u_avg)


    return u_avg-U_AVG

    

#Denne funksjonen skal ta inn en sigma og returnere u_avg-U_AVG



def main():

    a=0 #Startpunkt

    b=10  #Sluttpunkt

    N=20  #Antall punkter

    ua=-1 #a Temp

    ub=1 #b Temp

    my=2

    sig1=0.5

    sig2=10

    TOL = 0.000001

    U_AVG = 3

    

    x=np.linspace(a,b,N)

    A=SD.calculate_A_Matrix(x)

    sigma=HM.finn_sigma(sig1,sig2, TOL, temperatur, x, my, ua, ub, A, U_AVG)
    print(sigma)
    print(temperatur(x,2.3781657963991165,my,ua,ub,A, U_AVG))

    

main()