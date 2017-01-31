import numpy as np
import SpektralDiskretisering as SD
import Halveringsmetoden as HM
import NumeriskIntegral as NI


def temperatur(x,my,sigma,ua,ub,A, U_AVG):
    
    B=SD.calculate_B_Vector(x,my,sigma,ua,ub)
    
    y=SD.calculate_U_Vector(A,B)
    
    u_avg=NI.average(x,y)

    return u_avg-U_AVG
    
#Denne funksjonen skal ta inn en sigma og returnere u_avg-U_AVG

def main():
    a=0 #Startpunkt
    b=10  #Sluttpunkt
    N=20  #Antall punkter
    ua=5 #a Temp
    ub=5 #b Temp
    my=2
    sig1=0
    sig2=100
    TOL = 0.1
    U_AVG = 3
    
    x=np.linspace(a,b,N)
    A=SD.calculate_A_Matrix(x)
    sigma=HM.finn_sigma(sig1,sig2, TOL, temperatur, x, my, ua, ub, A, U_AVG)
    print(sigma)
    
main()