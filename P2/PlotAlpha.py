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
        #print(-r, i)
    return nextBreak, max_r
    #Returns the index of the next hook that breaks and corresponding max_r

def make_t_list(N, limit):
    t_list=np.zeros(N)
    for i in range(len(t_list)):
        t_list[i]=r.random()*limit
    return t_list
    
def make_alpha_list(N, M, beta):
    betaList = beta*np.ones(N)
    tList = make_t_list(N, SC.maxThreshold)
    A = LS.makeAMatrix(N, betaList)
    U = LS.makeUVector(N, 1)
    
    betaIndexList = np.zeros(N)
    alpha = np.zeros(N)
    
    
    for i in range(M):
        betaList = beta*np.ones(N)
        LS.updateAMatrix(betaList, A, N)
        tList = make_t_list(N, SC.maxThreshold)
        for k in range(0, N):
            xRef = LS.calculateXVector(A, U)
            betaIndex, rValue = findNextBreak(tList, betaList, xRef)
            betaIndexList[k] = betaIndex
            alpha[k] += betaList[betaIndex] / rValue
            betaList[betaIndex] = 0
            LS.updateAMatrix(betaList, A, N)
    alpha = alpha/M
    return alpha, betaIndexList
    
def main(numberOfIterations, numberOfSprings, beta):
    M = numberOfIterations
    N = numberOfSprings
    iteration = np.linspace(0,1,N)
    
    alphaList, betaIndexList = make_alpha_list(N, M, beta)
    
    plt.plot(iteration, betaIndexList, 'o')
    plt.figure()
    
    plt.plot(iteration, alphaList)
    plt.show()