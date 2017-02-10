# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import SpektralDiskretisering as SD
import Halveringsmetoden as HM
import NumeriskIntegral as NI
import Parametere as par

#f(x) fra oppgaven
def func1(sigma, x):
    return np.exp(-((x-par.my)**2)/sigma**2)
#f'(sigma) - f derivert med hensyn på sigma
def dfunc1(sigma, x):
    return 2*((x-par.my)**2/sigma**3)*np.exp(-((x-par.my)**2)/sigma**2)

#Funksjonen til error testing
def func2(x):
    return np.exp(x)*np.cos(8*np.pi*x)

#Dobelt deriverte av func2
def ddfunc2(sigma, x):
    return -np.exp(x)*(np.cos(8*np.pi*x)-16*np.pi*np.sin(8*np.pi*x)-64*(np.pi)**2*np.cos(8*np.pi*x))

#Denne funksjonen skal ta inn en sigma og returnere u_avg-U_AVG
def temperatur(x,sigma,A):
    B=SD.calculate_B_Vector(x, par.ua, par.ub, sigma,func1) #Beregner B-vektoren.
    y=SD.calculate_U_Vector(A,B) #Beregner U-vektorenen.
    
    u_avg=NI.average(x,y) #Beregner gjennomsnittsverdien for temperaturen

    return u_avg-par.U_AVG #Returnerer differansen mellom vår u-verdi og oppgitt U-verdi.

#Denne funksjonen returnerer den deriverte av temperaturen med hensyn på sigma
def dtemperatur(x,sigma,A):
    B=SD.calculate_B_Vector(x, 0, 0, sigma, dfunc1) #Beregner B-vektoren.
    y=SD.calculate_U_Vector(A,B) #Beregner U-vektorenen.
    
    ud_avg=NI.average(x,y)

    return ud_avg

def main():
    x = (par.b+par.a)/2. + (par.a-par.b)/2. * np.cos(np.arange(par.N)*np.pi/(par.N-1)) #Lager N chebyshevfordelte punkter.
    A=SD.calculate_A_Matrix(x) #Beregner A-matrisen.
    
    #Finner sigmaverdien vha. funksjon med gjettede sigmaverdier,
    #temperaturfunksjonen og A-matrisa.
    #sigma=HM.finn_sigma(par.sig1,par.sig2,temperatur, x, A)
    sigma, error = HM.finn_sigma_newton(8, x, A, temperatur, dtemperatur)
    print("Sigma: ", sigma) 
    print("Error: ", np.abs(temperatur(x,sigma,A))) #Skriver ut temperaturen
    
    #plotHeatSource(sigma)
    #plotTempProfile(sigma, A, x)
    
def plotHeatSource(sigma):
    x = np.linspace(0, 10, 200)
    plt.plot(x, func(sigma, x))
    plt.show()
    
def plotTempProfile(sigma, A, x):
    B=SD.calculate_B_Vector(x, par.ua, par.ub, sigma,func1)
    y=SD.calculate_U_Vector(A,B)
    plt.plot(x, y)
    plt.show()
    
def error_func(x, y):
    max = 0
    for i in range(0, len(x)):
        val = np.abs(y[i] - func2(x[i]))
        if(val > max):
            max = val
    return max
    
def run_error():
    N_max = 50
    
    N_array = np.linspace(2,N_max,N_max-1)
    e_array_un = [0]*(N_max-1)
    e_array_c = [0]*(N_max-1)
    
    for N in range(2,N_max):
        #Uniform
        x=np.linspace(par.a, par.b, N)
        A = SD.calculate_A_Matrix(x)
        B = SD.calculate_B_Vector(x, par.ua, par.ub, 0, func2)
        y = SD.calculate_U_Vector(A, B)
        e_array_un[N-1] = error_func(x, y)
        
        #Cheby
        x = (par.b+par.a)/2. + (par.a-par.b)/2. * np.cos(np.arange(N)*np.pi/(N-1))
        A = SD.calculate_A_Matrix(x)
        B = SD.calculate_B_Vector(x, par.ua, par.ub, 0, func2)
        y = SD.calculate_U_Vector(A, B)
        e_array_c[N-1] = error_func(x, y)
    
    plt.semilogy()
    plt.plot(N_array, e_array_un)
    plt.plot(N_array, e_array_c)
    plt.show()
    
    
#run_error()
main()
