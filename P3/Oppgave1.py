import numpy as np
import matplotlib.pyplot as plt
import DiffSolver as DS

def f(X, t):
    return 2*np.pi/24 * np.asarray([-X[1], X[0]])

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
   
plotError(False)
plotError(True)
#main()