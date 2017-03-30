import numpy as np
import matplotlib.pyplot as plt
import DiffSolver as DS
from timeit import default_timer as timer

def f(X, t):
    return 2*np.pi/(24*3600) * np.asarray([-X[1], X[0]])

def f2(Y, t):
    alpha = (5e-5)
    m = 0.01
    return np.asarray([alpha/m*(f(Y[1], t) - Y[0]), Y[0]])

def plotPath():
    N = 20
    L = 100
    totalTime = 2*24*3600
    X0 = np.asarray([L, 0.])
    t0 = 0
    
    XEuler = DS.forwardEuler(N, totalTime, t0, X0, f)
    XTrapezoid = DS.trapezoid(N, totalTime, t0, X0, f)
    
    plt.figure()
    plt.plot(XEuler[:,0],XEuler[:,1])
    plt.plot(XTrapezoid[:,0],XTrapezoid[:,1])
    
    plt.show()

def plotError():
    L = 100
    totalTime = 2*24*3600
    X0 = np.asarray([L, 0.])
    t0 = 0
    
    steps = 100
    errorEuler = np.zeros(steps)
    errorTrapezoid = np.zeros(steps)
    Nlist = [10*i for i in range(1, steps+1)]
    for i in range(steps):
        Xeuler = DS.forwardEuler(Nlist[i], totalTime, t0, X0, f)
        Xtrapez = DS.trapezoid(Nlist[i], totalTime, t0, X0, f)
        
        errorEuler[i] = np.sqrt((Xeuler[Nlist[i]-1,0] - L)**2 + Xeuler[Nlist[i]-1,1]**2)
        errorTrapezoid[i] = np.sqrt((Xtrapez[Nlist[i]-1,0] - L)**2 + Xtrapez[Nlist[i]-1,1]**2)
  
    print("Forward Euler")
    for i in range(1, steps):
        if (errorEuler[i-1]> 10 and errorEuler[i]< 10):
            print(Nlist[i-1], "iterasjoner ga", errorEuler[i-1], "error")
            print(Nlist[i], "iterasjoner ga", errorEuler[i], "error")
    
    print("Trapezoid")
    for i in range(1, steps):
        if (errorTrapezoid[i-1]> 10 and errorTrapezoid[i]< 10):
            print(Nlist[i-1], "iterasjoner ga", errorTrapezoid[i-1], "error")
            print(Nlist[i], "iterasjoner ga", errorTrapezoid[i], "error")
    
    hlist = [totalTime/(i-1) for i in Nlist]
    
    plt.figure()
    plt.xlabel("h")
    plt.ylabel("error")
    plt.semilogx()
    plt.semilogy()
    plt.plot(hlist, errorEuler)
    plt.plot(hlist, errorTrapezoid)
    plt.show()

def evaluateTime():
    NEuler = 830
    NTrapez = 60
    
    L = 100
    totalTime = 2*24*3600
    X0 = np.asarray([L, 0.])
    t0 = 0
    
    eulerT1 = timer()
    Xeuler = DS.forwardEuler(NEuler, totalTime, t0, X0, f)
    eulerT2 = timer()
    
    trapezT1 = timer()
    Xtrapez = DS.trapezoid(NTrapez, totalTime, t0, X0, f)
    trapezT2 = timer()
    
    print("Euler time:", eulerT2 - eulerT1)
    print("Trapez time:", trapezT2 - trapezT1)

def massAn():
    L = 1.0E+02
    alpha = 5.0E-05
    m = 1.0E-02
    k = alpha/m
    w = 2*np.pi/(24*60*60)*k
    A = np.array([
            [ 0, 0, 1, 0],
            [ 0, 0, 0, 1],
            [ 0,-w,-k, 0],
            [ w, 0, 0,-k]
        ])
    lams , V = np.linalg.eig(A)
    X0 = np.array([L,0.,0.,0.])
    C = np.linalg.solve(V,X0)
    t = 2*24*3600
    X = V.dot(C*np.exp(lams*t)) # pun
    return [X[0].real, X[1].real]
    #print(’Position after 48 hours = ’, X[0].real, X[1].real)

def mass(N, T, L):
    dt = T/(N-1)
    Y = np.asarray([np.asarray([np.zeros(2),np.zeros(2)]) for i in range(N)])
    Y[0] = np.asarray([np.asarray([0,0]),np.asarray([L,0])])
    for i in range(0, N-1):
        Y[i+1] = DS.forwardEulerStep(i*dt, dt, Y[i], f2)
    return Y[:,1,:]
    

def plotWithMass():
    N = 500
    T = 2*24*3600
    L = 100
    
    XNum = mass(N, T, L)
    XAn = massAn()
    
    plt.figure()
    plt.plot(XNum[:,0],XNum[:,1])
    #plt.plot(XAn[0], XAn[1], 'ro', color = 'g')
    plt.show()

def plotErrorWithMass():
    L = 100
    totalTime = 2*24*3600
    t0 = 0
    
    steps = 100
    error = np.zeros(steps)
    endpoint = massAn()
    Nlist = [230+10*i for i in range(1, steps+1)]
    for i in range(steps):
        X = mass(Nlist[i], totalTime, L)
        error[i] = np.sqrt((X[Nlist[i]-1,0] - endpoint[0])**2 + (X[Nlist[i]-1,1]-endpoint[1])**2)
    
    hlist = [totalTime/(i-1) for i in Nlist]
    
    plt.figure()
    plt.xlabel("h")
    plt.ylabel("error")
    plt.semilogx()
    plt.semilogy()
    plt.plot(hlist, error)
    plt.show()
    
def varTimeStepMass(TOL, t0, totalTime, L):
    Y = []
    t = []
    dt = []
    
    
    steps = 0
    
    currentY = np.asarray([np.asarray([0,0]),np.asarray([L,0])])
    currentt = t0
    currentdt = 400
    while (currentt < totalTime):
        currentY, currentt, currentdt = DS.varTimeTrapezoidStep(currentt, currentY, f2, TOL, currentdt, totalTime)
        
        Y.append(currentY)
        t.append(currentt)
        dt.append(currentdt)
        steps += 1
    Y = np.asarray(Y)
    print(steps)
    return Y[:,1,:], t, dt
    
def plotVarTimeStepMass():
    L = 100
    totalTime = 2*24*3600
    t0 = 0
    TOL = 1
    
    XNum, tNum, dtNum = varTimeStepMass(TOL, t0, totalTime, L)
    XAn = massAn()
    
    plt.figure()
    plt.plot(tNum, dtNum, 'ro')
    plt.show()
    
    plt.figure()
    plt.plot(XNum[:,0], XNum[:,1])
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    