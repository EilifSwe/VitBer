import numpy as np
import random as r
import matplotlib.pyplot as plt

import LinearSystem as LS
import SystemConstants as SC

def findNextBreak(t_list, beta, x_vector):
    nextBreak=0
    max_r=0
    for i in range(len(t_list)):
        #Iterates through all the hooks and finds the biggest r-value
        r=-x_vector[4*i+3]*beta[i]/t_list[i]
        if r > max_r:
            max_r=r 
            nextBreak=i
    return nextBreak, max_r
    #Returns the index of the next hook that breaks and corresponding max_r

#Lager en liste med N tilfeldige verdier mellom 0 og limit
def make_t_list(N, limit):
    t_list=np.zeros(N)
    for i in range(len(t_list)):
        t_list[i]=r.random()*limit
    return t_list

#Lager en liste med alphaverdiene som kreves for å løsrive den neste kroken
#betaIndexMatrix er en tabell med indeksen til kroken som løsrives
def make_alpha_list(N, M, beta):        #N kroker simuleres M ganger
    betaList = np.zeros(N)
    A = LS.makeAMatrix(N, betaList)     #Lager A-matrisen (dette trengs bare en gang)
    U = LS.makeUVector(N, 1)            #Lager U-vektorsen med alpha lik 1
    
    betaIndexMatrix=np.zeros([M,N])     
    alpha = np.zeros(N)                 #Oppretter listen som skal inneholde gjennomsnittet av alpha-verdiene
    
    for i in range(M):
        betaList = beta*np.ones(N)                  #Lager en betaliste med ingen røkede kroker
        LS.updateAMatrix(betaList, A, N)            #Oppdaterer A-matrisen med disse nye betaverdiene
        tList = make_t_list(N, SC.maxThreshold)     #Lager en ny liste med tilfeldige løsrivningsverdier
        for k in range(0, N):
            xRef = LS.calculateXVector(A, U)                            #Kalkulerer xref-vektoren
            betaIndex, rValue = findNextBreak(tList, betaList, xRef)    #Finner den neste kroken som ryker og r-verdien dens
            betaIndexMatrix[i,k]=betaIndex                              #Lagrer indeksen i tabellen
            alpha[k] += betaList[betaIndex] / rValue                    #Regner ut alpha-verdien og legger den til i alpha-listen
            betaList[betaIndex] = 0                                     #Oppdaterer beta-listen med den røkete kroken
            A[4*betaIndex, 4*betaIndex+3] = 0                           #Oppdaterer A-matrisen med den røkete kroken             
    alpha = alpha/M                    #Deler med M for at det skal være gjennomsnitt
    return alpha, betaIndexMatrix

#Samme som make_alpha_list bare med to endringer
def make_alpha_list_sparse(N, M, beta):
    betaList = np.zeros(N)
    A = LS.makeSparseAMatrix(N, betaList)   #Oppretter A som en sparse-matrise
    U = LS.makeUVector(N, 1)
    
    betaIndexMatrix=np.zeros([M,N])
    alpha = np.zeros(N)
    
    for i in range(M):
        betaList = beta*np.ones(N)
        LS.updateAMatrix(betaList, A, N)
        tList = make_t_list(N, SC.maxThreshold)
        for k in range(0, N):
            xRef = LS.calculateSparseXVector(A, U)                      #Regner ut X-vektoren med sparse-solver
            betaIndex, rValue = findNextBreak(tList, betaList, xRef)
            betaIndexMatrix[i,k]=betaIndex
            alpha[k] += betaList[betaIndex] / rValue
            betaList[betaIndex] = 0
            A[4*betaIndex, 4*betaIndex+3]=0
    alpha = alpha/M
    return alpha, betaIndexMatrix
    

    
def main(numberOfIterations, numberOfSprings,beta,sparse):
    M = numberOfIterations
    N = numberOfSprings
    iteration = np.linspace(0,1,N)
    if sparse:
        alphaList, betaIndexMatrix = make_alpha_list_sparse(N, M, beta)
    else:
        alphaList, betaIndexMatrix = make_alpha_list(N, M, beta)
    
    plt.figure()
    plt.matshow(betaIndexMatrix)
    plt.xlabel("$k$, kroker",fontsize=15)
    plt.ylabel("Antall simuleringer",fontsize=15)
    plt.title("Rekkefølge når krokene ryker",fontsize=15,y=1.08)
    plt.savefig("simuleringer_vitber2.pdf")
    
    plt.figure()
    plt.plot(iteration, alphaList)
    plt.legend()
    plt.title("Midlere $\\alpha$",fontsize=15)
    
    plt.text(0.7,350000,r'$\beta=10^8$',fontsize=15) #tekst med betaverdier. Plasseres ulikt avh. av betaverdi.
    #plt.text(0.7,0.2,r'$\beta=53.05$',fontsize=15)
    #plt.text(0.7,0.000007,r'$\beta=10^-3$',fontsize=15)
    #plt.text(0.7,0.00000000010,r'$\beta=10^-8$',fontsize=15)
    
    plt.xlabel("$n/N$ Antall iterasjoner",fontsize=15)
    plt.ylabel("$\\alpha$",fontsize=15)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.tight_layout()
    plt.savefig("vitber_alpha_prosj2.pdf")
    plt.show()
