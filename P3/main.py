import Oppgave1 as O1



if __name__ == "__main__":
    Master_Flag = {
                0: 'PlotPath',
                1: 'PlotError',
                2: 'EvaluateTime',
                3: 'PlotWithMass',
                4: 'PlotErrorWithMass',
                5: 'PlotVarTimestep'
        }[5]
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
        
#end = timer()
#O1.met2()