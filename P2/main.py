import numpy as np
import PlotEta as PE
import PlotAlpha as PA
import PlotAlphaMax as PAM
import SystemConstants as SC
from timeit import default_timer as timer

start = timer()

if __name__ == "__main__":
    Master_Flag = {
                0: 'PlotEta',
                1: 'PlotAlpha',
                2: 'PlotAlphaMax'
        }[1]
    if Master_Flag == 'PlotEta':
        PE.main()
    elif Master_Flag == 'PlotAlpha':
        numberOfIterations = 1
        numberOfSprings = 1000
        beta = SC.beta
        sparse = False
        PA.main(numberOfIterations, numberOfSprings, beta, sparse)
    elif Master_Flag == 'PlotAlphaMax':
        numberOfIterations = 10
        numberOfSprings = 20
        numberOfPoints = 50
        betaMin = 1e-8
        betaMax = 1e8
        PAM.main(numberOfIterations, numberOfSprings, numberOfPoints, betaMin, betaMax)
        
end = timer()
print("Dette er totaltid: ", end - start) 
        



