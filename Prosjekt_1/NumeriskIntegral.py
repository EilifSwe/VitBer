import numpy as np
import Parametere as par

#Bruker trapesmetoden. x er en liste med N punkter. y er U-matrisen.
def trapezoid(x, y):
    N = len(x)
    I = 0
    for i in range(0, N-1):
        I += 0.5*(y[i]+y[i+1])*(x[i+1]- x[i])
    return I

#Til å finne gjennomsnittsverdien til funksjonen(snittemperatur)
def average(x, y):
    N = len(x)
    intervall = x[N-1] - x[0]
    return trapezoid(x, y) / intervall
    
    
