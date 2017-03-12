import numpy as np
import matplotlib.pyplot as plt
import LinearSystem as LS
import SystemConstants as SC
import PlotAlpha as PA

def main(numberOfIterations, numberOfSprings, numberOfPoints, betaMin, betaMax):
    betaList = [np.power(10,i) for i in np.linspace(np.log10(betaMin), np.log10(betaMax), numberOfPoints)]
    alphaMaxList = np.zeros(numberOfPoints)
    
    for i in range(0, numberOfPoints):
        var=0
        alphaList,var = PA.make_alpha_list(numberOfSprings, numberOfIterations, betaList[i])
        alphaMaxList[i] = np.max(alphaList)
    plt.figure(figsize=(5,3))
    plt.semilogx(betaList, alphaMaxList)
    plt.semilogy(betaList,alphaMaxList)
    plt.xlabel("$\\beta$",fontsize=15)
    plt.ylabel("$max_n\\alpha_n$",fontsize=15)
    plt.title("E-felt for å løsne polymeren",fontsize=15)
    plt.tight_layout()
    plt.savefig("E_beta_vitber2.pdf")
    plt.show()
