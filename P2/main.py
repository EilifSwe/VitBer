import numpy as np
import PlotEta as PE
import PlotAlpha as PA
import PlotAlphaMax as PAM
import SparseTime as ST
import SystemConstants as SC
from timeit import default_timer as timer

start = timer()

if __name__ == "__main__":
    Master_Flag = {
                0: 'PlotEta',
                1: 'PlotAlpha',
                2: 'PlotAlphaMax',
                3: 'SparseTime'
        }[3]
    if Master_Flag == 'PlotEta':
        PE.main()
    elif Master_Flag == 'PlotAlpha':
        numberOfIterations = 10
        numberOfSprings = 500
        beta = SC.beta
        sparse = True
        PA.main(numberOfIterations, numberOfSprings, beta, sparse)
    elif Master_Flag == 'PlotAlphaMax':
        numberOfIterations = 10
        numberOfSprings = 10
        numberOfPoints = 500
        betaMin = 1e-8
        betaMax = 1e8
        PAM.main(numberOfIterations, numberOfSprings, numberOfPoints, betaMin, betaMax)
    elif Master_Flag == 'SparseTime':
        ST.main()
        
end = timer()
print("Dette er totaltid: ", end - start, "sekunder.")




