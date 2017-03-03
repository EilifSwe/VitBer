import numpy as np
import PlotEta as PE
import PlotAlpha as PA

if __name__ == "__main__":
    Master_Flag = {
                0: 'PlotEta',
                1: 'PlotAlpha'
        }[0]
    if Master_Flag == 'PlotEta':
        PE.main()
    elif Master_Flag == 'PlotAlpha':
        numberOfIterations = 50
        numberOfSprings = 70
        PA.main(numberOfIterations, numberOfSprings)



