import numpy as np
import matplotlib.pyplot as plt

import LinearSystem as LS
import SystemConstants as SC
import PlotAlpha as PA

def main(numberOfIterations, numberOfSprings, numberOfPoints, betaMin, betaMax):
    betaList = np.linspace(betaMin, betaMax, numberOfPoints)
    alphaMaxList = np.zeros(numberOfPoints)
    
    for i in range(0, numberOfPoints):
        variable=0 
        alphaList,variable = PA.make_alpha_list(numberOfIterations, numberOfSprings, betaList[i])
        alphaMaxList[i] = np.max(alphaList)
    plt.plot(betaList, alphaMaxList)
    plt.show()
