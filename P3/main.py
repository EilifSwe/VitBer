import Oppgave1 as O1
import Oppgave2 as O2


if __name__ == "__main__":
    Master_Flag = {
                0: 'PlotPath',
                1: 'PlotError',
                2: 'EvaluateTime',
                3: 'PlotWithMass',
                4: 'PlotErrorWithMass',
                5: 'PlotVarTimestep',
                6: 'PlotOceanPath'
        }[6]
    if Master_Flag == 'PlotPath':
        O1.plotPath()
    elif Master_Flag == 'PlotError':
        O1.plotError()
    elif Master_Flag == 'EvaluateTime':
        O1.evaluateTime()
    elif Master_Flag == 'PlotWithMass':
        O1.plotWithMass()
    elif Master_Flag == 'PlotErrorWithMass':
        O1.plotErrorWithMass()
    elif Master_Flag == 'PlotVarTimestep':
        O1.plotVarTimeStepMass()
    elif Master_Flag == 'PlotOceanPath':
        O2.plotPath(False)
        
#end = timer()
#O1.met2()