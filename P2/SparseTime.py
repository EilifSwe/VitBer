import PlotAlpha as PA
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

def main(): #Lager plot for å ta tid på tett og glissen matrise
    N = 25
    
    normalTime = np.zeros(N)
    sparseTime = np.zeros(N)
    
    numberOfSprings = [10*(i+1) for i in range(N)]
    numberOfIterations = 1
    startTime = 0
    endTime = 0
    for i in range(N):
        startTime = timer()
        PA.make_alpha_list(numberOfSprings[i], numberOfIterations, 53)
        endTime = timer()
        normalTime[i] = endTime - startTime
        startTime = timer()
        PA.make_alpha_list_sparse(numberOfSprings[i], numberOfIterations, 53)
        endTime = timer()
        sparseTime[i] = endTime - startTime
    
    
    
    plt.plot(numberOfSprings, sparseTime, label="Sparse")
    plt.plot(numberOfSprings, normalTime, label="Normal")
    plt.legend(loc=2)
    plt.title("Tidsutvikling for sparse-og normalmatrise.")
    plt.xlabel("Antall kroker",fontsize=15)
    plt.ylabel("Tid(s)",fontsize=15)
    plt.savefig("SparseTime.pdf")
    plt.show()
    
