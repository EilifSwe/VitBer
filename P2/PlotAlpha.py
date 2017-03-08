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

def make_t_list(N, limit):
    t_list=np.zeros(N)
    for i in range(len(t_list)):
        t_list[i]=r.random()*limit
    return t_list


def make_alpha_list(N, M, beta):
    betaList = np.zeros(N)
    A = LS.makeAMatrix(N, betaList)
    U = LS.makeUVector(N, 1)
    
    #betaIndexList = np.zeros(N)
    betaIndexMatrix=np.zeros([M,N]) #lager en matrise for å få til fargeplottet
    alpha = np.zeros(N)
    
    for i in range(M):
        betaList = beta*np.ones(N) #ok
        LS.updateAMatrix(betaList, A, N) #ok
        tList = make_t_list(N, SC.maxThreshold) #ok
        for k in range(0, N): #ok
            xRef = LS.calculateXVector(A, U) #ok
            betaIndex, rValue = findNextBreak(tList, betaList, xRef) 
            #betaIndexList[k] = betaIndex
            betaIndexMatrix[i,k]=betaIndex
            alpha[k] += betaList[betaIndex] / rValue
            betaList[betaIndex] = 0
            LS.updateAMatrix(betaList, A, N) #hvorfor er det forskjell her og i make_alpha_sparse?
    alpha = alpha/M
    return alpha, betaIndexMatrix #betaIndexList
##----
def make_alpha_list_sparse(N, M, beta):
    betaList = np.zeros(N)
    A = LS.makeSparseAMatrix(N, betaList)
    U = LS.makeUVector(N, 1)
    
    #betaIndexList = np.zeros(N)
    betaIndexMatrix=np.zeros([M,N]) #matrise for å få til fargeplott
    alpha = np.zeros(N)
    
    
    for i in range(M):
        betaList = beta*np.ones(N)
        LS.updateAMatrix(betaList, A, N)
        tList = make_t_list(N, SC.maxThreshold)
        for k in range(0, N):
            xRef = LS.calculateSparseXVector(A, U)
            betaIndex, rValue = findNextBreak(tList, betaList, xRef)
            #betaIndexList[k] = betaIndex
            betaIndexMatrix[i,k]=betaIndex #legger beta-indeksene i matrisa for hver iterasjon
            alpha[k] += betaList[betaIndex] / rValue
            betaList[betaIndex] = 0
            A[4*betaIndex, 4*betaIndex+3]=-betaList[betaIndex] #hvorfor forskjell her og i vanlig?
    alpha = alpha/M
    return alpha, betaIndexMatrix #betaIndexList

def main(numberOfIterations, numberOfSprings,beta,sparse):
   ##----------------------
    M = numberOfIterations
    N = numberOfSprings
    iteration = np.linspace(0,1,N)
    if sparse:
        alphaList, betaIndexMatrix = make_alpha_list_sparse(N, M, beta) #byttet ut list med matrix
    else:
        alphaList, betaIndexMatrix = make_alpha_list(N, M, beta) #byttet ut list med Matrix
    
    plt.figure()
    plt.matshow(betaIndexMatrix) #måte å plotte fargeplottet
    plt.xlabel("n",fontsize=15)
    plt.ylabel("Antall simuleringer",fontsize=15)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.savefig("simuleringer_vitber2.pdf")
    
    plt.figure()
    plt.plot(iteration, alphaList)
    plt.xlabel("n/N Antall iterasjoner",fontsize=15)
    plt.ylabel("Midlere $\\alpha$",fontsize=15)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.savefig("vitber_alpha_prosj2.pdf")
    plt.show()    
