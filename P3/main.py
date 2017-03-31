import Oppgave1 as O1
import Oppgave2 as O2
import Oppgave3 as O3

L = 100
totalTime = 2*24*3600

if __name__ == "__main__":
    Master_Flag = {
                0: 'PlotPath',
                1: 'PlotError',
                2: 'EvaluateTime',
                3: 'PlotWithMass',
                4: 'PlotErrorWithMass',
                5: 'PlotVarTimestep',
                6: 'PlotOceanPath',
                7: 'PlotParticlePos'
        }[7]
    if Master_Flag == 'PlotPath':
        h = 100
        O1.plotPath(h, L, totalTime, 0)
    elif Master_Flag == 'PlotError':
        steps = 50
        O1.plotError(steps, L, totalTime, 0)
    elif Master_Flag == 'EvaluateTime':
        hEuler = 208
        hTrapez = 3004
        O1.evaluateTime(hEuler, hTrapez, L, totalTime, 0)
    elif Master_Flag == 'PlotWithMass':
        h = 100
        O1.plotWithMass(h, L, totalTime, 0)
    elif Master_Flag == 'PlotErrorWithMass':
        steps = 90
        O1.plotErrorWithMass(steps, L, totalTime, 0)
    elif Master_Flag == 'PlotVarTimestep':
        TOL = 1
        O1.plotVarTimeStepMass(TOL, L, totalTime, 0)
    elif Master_Flag == 'PlotOceanPath':
        map = True
        O2.plotPath(map)
    elif Master_Flag == 'PlotParticlePos':
        grid = False
        O3.plotParticlePos(grid)