# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:55:44 2017
@author: julie
"""

import numpy as np
import matplotlib.pyplot as plt
import SpektralDiskretisering as SD
import Halveringsmetoden as HM
import NumeriskIntegral as NI
import Parametere as par

#Funksjonen fra diff likningen til u
def func(sigma, x):
    return np.exp(-((x-par.my)**2)/sigma**2)


#Denne funksjonen skal ta inn en sigma og returnere u_avg-U_AVG
def temperatur(x,sigma,A):
    B=SD.calculate_B_Vector(x,sigma,func)
    y=SD.calculate_U_Vector(A,B)
    
    u_avg=NI.average(x,y)
    print("u_avg:", u_avg)

    return u_avg-par.U_AVG


def main():
    x=np.linspace(par.a,par.b,par.N)

    A=SD.calculate_A_Matrix(x)

    sigma=HM.finn_sigma(par.sig1,par.sig2,temperatur, x, A)
    print(sigma)
    print(temperatur(x,2.3781657963991165,A))

main()