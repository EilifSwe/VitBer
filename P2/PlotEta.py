import numpy as np
import matplotlib.pyplot as plt

import LinearSystem as LS
import SystemConstants as SC

def eta(k, xArray, alpha):
    #k = int(np.floor(ksi))
    #x = ksi - k
    x=np.linspace(0.0,1.0,200)
    
    return (((-(alpha / 24.) *x + xArray[4*k])*x + xArray[4*k+1])*x + xArray[4*k+2])*x + xArray[4*k+3]

def dEta(k, xArray, alpha):
    #k = int(np.floor(ksi))
    #x = ksi - k
    x=np.linspace(0.0,1.0,200)
    return ((-(alpha / 6.) *x + 3*xArray[4*k])*x + 2*xArray[4*k+1])*x + xArray[4*k+2]
    
def ddEta(k, xArray, alpha):
   # k = int(np.floor(ksi))
    #x = ksi - k
    x=np.linspace(0.0,1.0,200)
    return (-(alpha / 2.) *x + 6*xArray[4*k])*x + 2*xArray[4*k+1]
    
def dddEta(k, xArray, alpha):
   # k = int(np.floor(ksi))
    #x = ksi - k
    x=np.linspace(0.0,1.0,200)
    
    return -alpha*x + 6*xArray[4*k]
    
def plotEta(nr, N, xArray, alpha):
    ksi = np.linspace(0, N - 0.00001, 1000)
    ksi_1=np.linspace(0.0,1.0,200)
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
    
    for k in range(N): #N =number og solution intervals 
        if(k==N-1):
            lines=plt.plot(ksi_1 + k, func(k, xArray, alpha),label=r'$\eta$ - numerical')
            plt.setp(lines,color='b',linewidth=2.3)
        else:
            lines=plt.plot(ksi_1 + k, func(k, xArray, alpha))
            plt.setp(lines,color='b',linewidth=2.3)


    
def plotSubEta(nr,N,xArray,alpha):
    
    fig_solution = plt.figure(figsize=(15,10))
    #xi_minus_k=np.linspace(0.0,1.0,200)
    
    ax_y = fig_solution.add_subplot(411)
    plt.setp(ax_y.get_xticklabels(), visible=False)
    plotEta(0, N,xArray, alpha)
    plt.title("$\eta(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta$)",fontsize=20)
    plt.grid()
    
    ax_dy = fig_solution.add_subplot(412, sharex=ax_y)
    plt.setp(ax_dy.get_xticklabels(), visible=False)
    plotEta(1, N, xArray, alpha)
    plt.title("$\eta'(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta'$)",fontsize=20)
    plt.grid()            
    ax_ddy = fig_solution.add_subplot(413, sharex=ax_y)
    plt.setp(ax_ddy.get_xticklabels(), visible=False)
    plotEta(2, N, xArray, alpha)
    plt.title("$\eta''(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta''$)",fontsize=20)
    plt.grid()
    
    ax_dddy = fig_solution.add_subplot(414, sharex=ax_y)
    plotEta(3, N, xArray, alpha)
    plt.title("$\eta'''(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.xlabel("$k$ (antall kroker), ($\\xi$)",fontsize=20)
    plt.ylabel("Utslag, ($\eta'''$)",fontsize=20)
    
    plt.grid()
    plt.tight_layout()
    plt.savefig("eta_ksi2_vitber2.pdf")
    
def plotEtaAnalytic(N,alpha,beta,xArray):
    plt.figure(figsize=(10,4))
    for i in range(N):
        if i==(N-1):
            x=np.linspace(0+i,1+i,200)
            etaAnalytic=-(alpha / 24.)*(x-i)**4 + (alpha/12.)*(x-i)**3 + -(alpha/24.)*(x-i)**2 -(alpha/beta)
            lines=plt.plot(x,etaAnalytic,label=r'$\eta$ - analytical')
            plt.setp(lines,color='r',linewidth=2.1)
        else:
            x=np.linspace(0+i,1+i,200)
            etaAnalytic=-(alpha / 24.)*(x-i)**4 + (alpha/12.)*(x-i)**3 + -(alpha/24.)*(x-i)**2 -(alpha/beta)
            lines=plt.plot(x,etaAnalytic)
            plt.setp(lines,color='r',linewidth=2.1)
    #lines.set_label("$\eta$ - analytical")
    
    plt.title("$\eta(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.xlabel("$k$ (antall kroker), ($\\xi$)",fontsize=20)
    plt.ylabel("Utslag, ($\eta$)",fontsize=20)
    lines2=plotEta(0,4,xArray,alpha)
    #lines2[1].set_label('$\eta$ - analytical')
    plt.legend()
    #plt.text(3.35,-0.197,r'$\beta=53.05$',fontsize=15)
    plt.tight_layout()
    plt.savefig("etaAnalytic_vitber2.pdf")
    #Main
def main():
    N = 8
    beta=53.05*np.ones(N)
    #beta=0.05*np.ones(N)
    
    alpha = 1.061
    
    A = LS.makeAMatrix(N, beta)
    
    #updateAMatrix(beta, A, N)
    #printMatrix(A)
    U = LS.makeUVector(N, alpha)

    xArray = LS.calculateXVector(A, U)
    #plotSubEta(0, N, xArray, alpha)
    plt.figure()
    plotEtaAnalytic(4,alpha,53.05,xArray)
    #plotEtaAnalytic(4,alpha,0.05,xArray)
