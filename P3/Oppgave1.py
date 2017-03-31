import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import DiffSolver as DS
from timeit import default_timer as timer
import TSM_Classes as TSM_C

def f(X, t):
    return 2*np.pi/(24*3600) * np.asarray([-X[1], X[0]])

def f2(Y, t):
    alpha = (5e-5)
    m = 0.01
    return np.asarray([alpha/m*(f(Y[1], t) - Y[0]), Y[0]])

def plotPath():
    N = 200
    L = 100
    totalTime = 2*24*3600
    X0 = np.asarray([L, 0.])
    t0 = 0
    #h=totalTime/N
    h=2*10**2
    XEuler = DS.forwardEuler(h, totalTime, t0, X0, f)
    XTrapezoid = DS.trapezoid(h, totalTime, t0, X0, f)
    
    #plott startpunkt
    plt.figure()
    plt.plot(XEuler[:,0],XEuler[:,1],label='Euler')
    plt.plot(XTrapezoid[:,0],XTrapezoid[:,1],label='Trapezoid')
    plt.plot(XEuler[0,0],XEuler[0,1],'x')
    plt.plot(XTrapezoid[0,0],XTrapezoid[0,1],'x')
    plt.title("Banen til x(t)",fontsize=15)
    plt.xlabel("Posisjon, $x$ (m)",fontsize=15)
    plt.ylabel("Posisjon, $y$ (m)",fontsize=15)
    plt.legend()
    plt.savefig("path_oppg1.pdf")
    plt.show()

def plotError():
    L = 100
    totalTime = 2*24*3600
    X0 = np.asarray([L, 0.])
    t0 = 0
    
    steps = 15# 100
    errorEuler = np.zeros(steps)
    errorTrapezoid = np.zeros(steps)
    h=np.logspace(1,5,steps)
    #Nlist=np.logspace(2,5,steps)
    #Nlist=np.linspace(200,50000,steps)
    #Nlist = [10*i for i in range(1, steps+1)]
    for i in range(steps):
        Xeuler = DS.forwardEuler(h[i], totalTime, t0, X0, f)
        Xtrapez = DS.trapezoid(h[i], totalTime, t0, X0, f)
        
        errorEuler[i] = np.sqrt((Xeuler[-1,0] - L)**2 + Xeuler[-1,1]**2)
        errorTrapezoid[i] = np.sqrt((Xtrapez[-1,0] - L)**2 + Xtrapez[-1,1]**2)
  
    print("Forward Euler")
    for i in range(1, steps):
        if (errorEuler[i-1]> 10 and errorEuler[i]< 10):
            print(h[i-1], "iterasjoner ga", errorEuler[i-1], "error")
            print(h[i], "iterasjoner ga", errorEuler[i], "error")
    
    print("Trapezoid")
    for i in range(1, steps):
        if (errorTrapezoid[i-1]> 10 and errorTrapezoid[i]< 10):
            print(h[i-1], "iterasjoner ga", errorTrapezoid[i-1], "error")
            print(h[i], "iterasjoner ga", errorTrapezoid[i], "error")
    
    
    plt.figure() 
    
    plt.plot(h, errorEuler,label='Error - Euler')
    plt.plot(h, errorTrapezoid,label='Error - Trapezoid')
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Feil for Euler og Trapezoid",fontsize=15)
    plt.xlabel("Tidssteg, $h$ (s)",fontsize=15)
    plt.ylabel("Error, (m)",fontsize=15)
    plt.legend(loc=4)
    plt.savefig("Error_oppg1a.pdf")
    plt.show()

def evaluateTime():
    hEuler = 208
    hTrapez = 3004
    
    L = 100
    totalTime = 2*24*3600
    X0 = np.asarray([L, 0.])
    t0 = 0
    
    eulerT1 = timer()
    Xeuler = DS.forwardEuler(hEuler, totalTime, t0, X0, f)
    eulerT2 = timer()
    
    trapezT1 = timer()
    Xtrapez = DS.trapezoid(hTrapez, totalTime, t0, X0, f)
    trapezT2 = timer()
    
    print("Euler time:", eulerT2 - eulerT1, "Error:", np.sqrt((Xeuler[-1,0] - L)**2 + Xeuler[-1,1]**2))
    print("Trapez time:", trapezT2 - trapezT1, "Error:",np.sqrt((Xtrapez[-1,0] - L)**2 + Xtrapez[-1,1]**2))

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
    plt.plot(XNum[0,0],XNum[0,1],'x')
    
    
    plt.plot(XNum[:,0],XNum[:,1],label="Trapezoid")
    plt.title("Banen til $x(t)$",fontsize=15)
    plt.xlabel("Posisjon, $x$ (m)",fontsize=15)
    plt.ylabel("Posisjon, $y$ (m)",fontsize=15)
    plt.legend(loc=4)
    plt.savefig("Bane_oppg1c.pdf")
    
    #plt.plot(XAn[0], XAn[1], 'ro', color = 'g')
    plt.show()

#Fikse riktig log-scale på denne
def plotErrorWithMass():
    L = 100
    totalTime = 2*24*3600
    t0 = 0
    
    steps = 100
    error = np.zeros(steps)
    endpoint = massAn()
    hlist = [50+10*i for i in range(1, steps+1)]
    Nlist = [totalTime//(i-1) for i in hlist]
    for i in range(steps):
        X = mass(Nlist[i], totalTime, L)
        error[i] = np.sqrt((X[-1,0] - endpoint[0])**2 + (X[-1,1]-endpoint[1])**2)
    
    
    #plott log-log
    figure=plt.figure()
    ax = figure.add_subplot(111)
    ax.loglog(hlist, error,label="Global Error - Trapezoid")
    ax.set_title("Global Error ",fontsize=15)
    ax.set_xlabel("Tidssteg, $h$ (s)",fontsize=15)
    ax.set_ylabel("Error, (m)",fontsize=15)
    
    ax.set_xscale('symlog', linthreshx=1)
    
    xAxis = plt.gca().xaxis
    xAxis.set_minor_locator(TSM_C.MinorSymLogLocator(1))
    xAxis.set_minor_formatter(FormatStrFormatter("%.0f"))
    ax.legend(loc=2)
    plt.savefig("Globalerror_oppg1c.pdf")
    plt.show()
    '''
    #Nytt plott
    hlist=np.linspace(100,390,steps)
    Nlist = [int(totalTime//(i-1)) for i in hlist]
    print(Nlist)
    for i in range(steps):
        X = mass(Nlist[i], totalTime, L)
        error[i] = np.sqrt((X[-1,0] - endpoint[0])**2 + (X[-1,1]-endpoint[1])**2)
    
    figure=plt.figure()
    ax=figure.add_subplot(111)
    ax.loglog(hlist, error,label="Global Error - Trapezoid")
    ax.set_title("Global Error ",fontsize=15)
    ax.set_xlabel("Tidssteg, $h$",fontsize=15)
    ax.set_ylabel("Error",fontsize=15) 
    ax.set_xlim([100,400])
    xAxis = plt.gca().xaxis
    xAxis.set_minor_locator(TSM_C.MinorSymLogLocator(0))
    xAxis.set_minor_formatter(FormatStrFormatter("%.0f"))
    yAxis = plt.gca().yaxis
    yAxis.set_minor_locator(TSM_C.MinorSymLogLocator(0))
    yAxis.set_minor_formatter(FormatStrFormatter("%.0f"))
    ax.legend()
    plt.grid(b=True, which='both', color='0.3', linestyle=':')
    plt.savefig("Globalerror_oppg1c_test.pdf")
    plt.show()
    '''
        
        
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
    #print(steps)
    return Y[:,1,:], t, dt
    
def plotVarTimeStepMass():
    L = 100
    totalTime = 2*24*3600
    t0 = 0
    TOL = 1
    
    XNum, tNum, dtNum = varTimeStepMass(TOL, t0, totalTime, L)
    XAn = massAn()
    
    plt.figure()
    plt.plot(tNum, dtNum, 'o',label='Tidssteg')
    plt.title("Banen til $x(t)$ med variabelt tidssteg",fontsize=15)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.xlim()
    plt.xlabel("Tidsutvikling, $t$",fontsize=15)
    plt.ylabel("Endring i tid, $dt$",fontsize=15)
    
    plt.ylim([0,500])
    
    plt.legend()
    plt.savefig("Tid_oppg1d.pdf")
    plt.show()
    
    
    plt.figure()
    plt.plot(XNum[:,0], XNum[:,1],label="Varierende tidsstegmetode")
    plt.plot(XNum[0,0], XNum[0,1],'x')
    plt.title("Banen til $x(t)$ med variabelt tidssteg",fontsize=15)
    plt.xlabel("Posisjon, $x$",fontsize=15)
    plt.ylabel("Posisjon, $y$",fontsize=15)
    plt.legend(loc=4)
    plt.savefig("Bane_oppg1d.pdf")
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    