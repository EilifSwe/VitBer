import numpy as np
import matplotlib.pyplot as plt

import LinearSystem as LS
import SystemConstants as SC
import PlotAlpha as PA

def main(numberOfIterations, numberOfSprings, numberOfPoints, betaMin, betaMax):
    betaList = np.linspace(betaMin, betaMax, numberOfPoints)
    alphaMaxList = np.zeros(numberOfPoints)
    
    for i in range(0, numberOfPoints):
        var=0
        alphaList,var = PA.make_alpha_list(numberOfIterations, numberOfSprings, betaList[i])
        alphaMaxList[i] = np.max(alphaList)
    plt.figure(figsize=(5,3))
    plt.plot(betaList, alphaMaxList)
    plt.xlabel("$\\beta$",fontsize=15)
    plt.ylabel("$max_n\\alpha_n$",fontsize=15)
    #plt.rcParams['xtick.labelsize'] = 12
    #plt.rcParams['ytick.labelsize'] = 12
    plt.title("E-felt for å løsne polymeren",fontsize=15)
    plt.tight_layout()
    plt.savefig("E_beta_vitber2.pdf")
    plt.show()