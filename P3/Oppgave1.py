import numpy as np
import matplotlib.pyplot as plt
import DiffSolver as DS

def f(X, t):
    return 2*np.pi/(24*3600) * np.asarray([-X[1], X[0]])

def f2(Y, t):
    alpha = (5e-5)
    m = 0.01
    return np.asarray([alpha/m*(f(Y[1], t) - Y[0]), Y[0]])

def main():
    N = 50
    L = 100
    X0 = np.asarray([0, 100])
    t0 = 0
    
    X = DS.forwardEuler(N, 48, t0, X0, f)
    
    plt.figure()
    plt.plot(X[:,0],X[:,1], 'ro')
    plt.plot(XAnalytic[:,0],XAnalytic[:,1], 'ro', color = 'g')
    
    plt.show()

def met2An():
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

    

def met2():
    N = 500
    T = 2*24*3600
    L = 100
    
    dt = T/N
    Y = np.asarray([np.asarray([np.zeros(2),np.zeros(2)]) for i in range(N)])
    Y[0] = np.asarray([np.asarray([0,0]),np.asarray([0,L])])
    for i in range(0, N-1):
        Y[i+1] = DS.trapezoidStep(i*dt, dt, Y[i], f2)
        
    plt.figure()
    
    plt.plot(Y[:,1,0],Y[:,1,1], 'ro')
    XAn = met2An()
    plt.plot(XAn[0], XAn[1], 'ro', color = 'g')
    #plt.plot(XAnalytic[:,0],XAnalytic[:,1], 'ro', color = 'g')
    plt.show()

def plotError(trapezoid):
    L = 100
    X0 = np.asarray([0, 100])
    t0 = 0
    
    steps = 100
    error = []
    Nlist = [10*i for i in range(1, steps+1)]
    for N in Nlist:
        if(trapezoid):
            X = DS.trapezoid(N, 48, t0, X0, f)
        else:
            X = DS.forwardEuler(N, 48, t0, X0, f)
        error.append(np.sqrt(X[N-1,0]**2 + (X[N-1,1] - L)**2))
    
    
    if(trapezoid):
        print("Trapezoid")
    else:
        print("Forward Euler")
    for i in range(1, steps):
        if (error[i-1]> 10 and error[i]< 10):
            print(Nlist[i-1], "iterasjoner ga", error[i-1], "error")
            print(Nlist[i], "iterasjoner ga", error[i], "error")
        
    
    plt.figure()
    plt.semilogx()
    plt.semilogy()
    plt.plot(Nlist, error)
    plt.show()
   
met2()
#plotError(False)
#plotError(True)
#main()