import numpy as np
import matplotlib.pyplot as plt

import LinearSystem as LS
import SystemConstants as SC

def eta(ksi, xArray, alpha):
    k = int(np.floor(ksi))
    x = ksi - k
    return (((-(alpha / 24.) *x + xArray[4*k])*x + xArray[4*k+1])*x + xArray[4*k+2])*x + xArray[4*k+3]

def dEta(ksi, xArray, alpha):
    k = int(np.floor(ksi))
    x = ksi - k
    return ((-(alpha / 6.) *x + 3*xArray[4*k])*x + 2*xArray[4*k+1])*x + xArray[4*k+2]
    
def ddEta(ksi, xArray, alpha):
    k = int(np.floor(ksi))
    x = ksi - k
    return (-(alpha / 2.) *x + 6*xArray[4*k])*x + 2*xArray[4*k+1]
    
def dddEta(ksi, xArray, alpha):
    k = int(np.floor(ksi))
    x = ksi - k
    
    return -alpha*x + 6*xArray[4*k]
    
def plotEta(nr, N, xArray, alpha):
    ksi = np.linspace(0, N - 0.00001, 1000)
    etaArray = []
    
    func = None
    
    if (nr == 0):
        func = eta
    elif (nr == 1):
        func = dEta
    elif (nr == 2):
        func = ddEta
    elif (nr == 3):
        func = dddEta
    
    for i in ksi:
        etaArray.append(func(i, xArray, alpha))
    
    plt.plot(ksi, etaArray)
    plt.show()

#Main
def main():
    N = 20
    beta=53.05*np.ones(N)
    
    alpha = 10
    
    A = LS.makeAMatrix(N, beta)
    
    #updateAMatrix(beta, A, N)
    #printMatrix(A)
    U = LS.makeUVector(N, alpha)

    xArray = LS.calculateXVector(A, U)
    plotSubEta(0, N, xArray, alpha)
    
def plotSubEta(nr,N,xArray,alpha):
    
    fig_solution = plt.figure(figsize=(15,10))
    
    ax_y = fig_solution.add_subplot(411)
    plt.setp(ax_y.get_xticklabels(), visible=False)
    plotEta(0, N,xArray, alpha)
    plt.title("$\eta(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta$)",fontsize=20)

    
    ax_dy = fig_solution.add_subplot(412, sharex=ax_y)
    plt.setp(ax_dy.get_xticklabels(), visible=False)
    plotEta(1, N, xArray, alpha)
    plt.title("$\eta'(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta'$)",fontsize=20)
                
    ax_ddy = fig_solution.add_subplot(413, sharex=ax_y)
    plt.setp(ax_ddy.get_xticklabels(), visible=False)
    plotEta(2, N, xArray, alpha)
    plt.title("$\eta''(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta''$)",fontsize=20)
    
    ax_dddy = fig_solution.add_subplot(414, sharex=ax_y)
    plotEta(3, N, xArray, alpha)
    plt.title("$\eta'''(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.xlabel("$k$ (antall kroker), ($\\xi$)",fontsize=20)
    plt.ylabel("Utslag, ($\eta'''$)",fontsize=20)
    
    plt.tight_layout()
    plt.savefig("eta_ksi_vitber2.pdf")