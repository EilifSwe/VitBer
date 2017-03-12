import numpy as np
import matplotlib.pyplot as plt

import LinearSystem as LS
import SystemConstants as SC
#eta-funksjonen
def eta(k, xArray, alpha):
    x=np.linspace(0.0,1.0,200)
    return (((-(alpha / 24.) *x + xArray[4*k])*x + xArray[4*k+1])*x + xArray[4*k+2])*x + xArray[4*k+3]
#forstederiverte
def dEta(k, xArray, alpha):
    x=np.linspace(0.0,1.0,200)
    return ((-(alpha / 6.) *x + 3*xArray[4*k])*x + 2*xArray[4*k+1])*x + xArray[4*k+2]
#andrederiverte    
def ddEta(k, xArray, alpha):
    x=np.linspace(0.0,1.0,200)
    return (-(alpha / 2.) *x + 6*xArray[4*k])*x + 2*xArray[4*k+1]
#tredjederiverte    
def dddEta(k, xArray, alpha):
    x=np.linspace(0.0,1.0,200)
    return -alpha*x + 6*xArray[4*k]
    
def plotEta(nr, N, xArray, alpha):
    ksi_1=np.linspace(0.0,1.0,200) #plotter en krok om gangen, derfor intervall mellom 0 og 1. 
    
    func = None #velger hvilken funksjon som skal plottes. 
    if (nr == 0):
        func = eta
    elif (nr == 1):
        func = dEta
    elif (nr == 2):
        func = ddEta
    elif (nr == 3):
        func = dddEta
    
    for k in range(N): #N =number og solution intervals 
        if(k==N-1): #legger kun til labelnavn på siste krok.
            lines=plt.plot(ksi_1 + k, func(k, xArray, alpha),label=r'$\eta$ - numerical')
            plt.setp(lines,color='b',linewidth=2.3)
        else:
            lines=plt.plot(ksi_1 + k, func(k, xArray, alpha))
            plt.setp(lines,color='b',linewidth=2.3)


    
def plotSubEta(nr,N,xArray,alpha): #plotter eta numerisk.
    
    fig_solution = plt.figure(figsize=(15,10))   
    
    #eta
    ax_y = fig_solution.add_subplot(411) #lager fire subplot.
    plt.setp(ax_y.get_xticklabels(), visible=False)
    plotEta(0, N,xArray, alpha) #kjører funksjonen for å plotte eta.
    plt.title("$\eta(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta$)",fontsize=20)
    plt.grid()
    
    #1.-deriverte
    ax_dy = fig_solution.add_subplot(412, sharex=ax_y)
    plt.setp(ax_dy.get_xticklabels(), visible=False)
    plotEta(1, N, xArray, alpha)
    plt.title("$\eta'(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta'$)",fontsize=20)
    plt.grid() 
    
    #2.-deriverte
    ax_ddy = fig_solution.add_subplot(413, sharex=ax_y)
    plt.setp(ax_ddy.get_xticklabels(), visible=False)
    plotEta(2, N, xArray, alpha)
    plt.title("$\eta''(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta''$)",fontsize=20)
    plt.grid()
    
    #3.-deriverte
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


def plotEtaAnalytic(N,alpha,beta,xArray,col,label1,bool_const): #plotter eta analytisk.
    for i in range(N):
        if i==(N-1): #legger til labelnavn kun på sist krok
            x=np.linspace(0+i,1+i,200)
            etaAnalytic=-(alpha / 24.)*(x-i)**4 + (alpha/12.)*(x-i)**3 + -(alpha/24.)*(x-i)**2 -(alpha/beta)
            lines=plt.plot(x,etaAnalytic,label=label1)
            plt.setp(lines,color=col,linewidth=2.1)
        else:
            x=np.linspace(0+i,1+i,200)
            etaAnalytic=-(alpha / 24.)*(x-i)**4 + (alpha/12.)*(x-i)**3 + -(alpha/24.)*(x-i)**2 -(alpha/beta)
            lines=plt.plot(x,etaAnalytic)
            plt.setp(lines,color=col,linewidth=2.1)
    
    plt.title("$\eta(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.xlabel("$k$ (antall kroker), ($\\xi$)",fontsize=20)
    plt.ylabel("Utslag, ($\eta$)",fontsize=20)
    if (bool_const): 
        lines2=plotEta(0,4,xArray,alpha)
    plt.legend()
    plt.tight_layout()
    plt.savefig("etaAnalytic_vitber2_3.pdf")

#Lager figur 2
def plotCompareEta(alpha,xArray):
    plt.figure()
    plotEtaAnalytic(4,alpha,53.05,xArray,'r',r'$\eta, \alpha=1,\beta=53.05$',False) 
    plotEtaAnalytic(4,alpha,10000,xArray,'b',r'$\eta, \alpha=1,\beta=10 000$',False)
    plotEtaAnalytic(4,2.5,53.05,xArray,'g',r'$\eta, \alpha=2.5,\beta=53.05$',False)
    plt.legend(loc=7)

def main():
    N = 8
    beta=53.05*np.ones(N)
    alpha = 1.061
    
    A = LS.makeAMatrix(N, beta)
    U = LS.makeUVector(N, alpha)

    xArray = LS.calculateXVector(A, U)
    
    plotSubEta(0, N, xArray, alpha) #figur 3,Subplots med de deriverte. 
    plt.figure()
    plotEtaAnalytic(4,alpha,53.05,xArray,'r',r'$\eta$-analytical',True)  #plotter figur 1
    plotCompareEta(alpha,xArray) #plotter figur 2
