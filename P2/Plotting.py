import matplotlib.pyplot as plt
import numpy as np

def eta(ksi, xArray, alpha):
    k = floor(ksi)
    x = ksi - k
    return (((-(alpha / 24.) *x + xArray[4*k])*x + xArray[4*k+1])*x + xArray[4*k+2])*x + xArray[4*k+3]

def dEta(ksi, xArray, alpha):
    k = floor(ksi)
    x = ksi - k
    return ((-(alpha / 6.) *x + 3*xArray[4*k])*x + 2*xArray[4*k+1])*x + xArray[4*k+2]
    
def ddEta(ksi, xArray, alpha):
    k = floor(ksi)
    x = ksi - k
    return (-(alpha / 2.) *x + 6*xArray[4*k])*x + 2*xArray[4*k+1]
    
def dddEta(ksi, xArray, alpha):
    k = floor(ksi)
    x = ksi - k
    return -alpha*x + 6*xArray[4*k]
    
def plotEta(nr, N, xArray, alpha):
    ksi = np.linspace(0, N- 1, 100)
    eta = []
    
    if (nr == 0):
        eta = eta(ksi, xArray, alpha)
    elif (nr == 1):
        eta = dEta(ksi, xArray, alpha)
    elif (nr == 2):
        eta = ddEta(ksi, xArray, alpha)
    elif (nr == 3):
        eta = dddEta(ksi, xArray, alpha)
    
    plt.plot(ksi, eta)