import numpy as np
import matplotlib.pyplot as plt

def forwardEulerStep(t, dt, X, f):
    return X + dt*f(X,t)

def forwardEuler(N, T, t0, X0, f):
    dt = T/(N-1)
    X = np.asarray([np.zeros(2) for i in range(N)])
    X[0] = X0
    for i in range(0, N-1):
        X[i+1] = forwardEulerStep(i*dt, dt, X[i], f)
    return X
    
def trapezoidStep(t, dt, X, f):
    k0 = f(X,t)
    k1 = f(X + dt*k0, t +dt,)
    return X + 0.5*dt*(k0+k1)
    
def trapezoid(N, T, t0, X0, f):
    dt = T/(N-1)
    X = np.asarray([np.zeros(2) for i in range(N+1)])
    X[0] = X0
    for i in range(0, N-1):
        X[i+1] = trapezoidStep(i*dt, dt, X[i], f)
    return X
    
def varTimeTrapezoidStep(t, X, f, TOL, lastdt, endt):
    k0 = f(X,t) #stigning  i startpunkt
    
    testk1 = f(X+lastdt*k0, t + lastdt) 
    dist = np.sqrt((testk1[1][0]-k0[1][0])**2 + (testk1[1][1]-k0[1][1])**2)
    dt = 0.8*np.sqrt((2*TOL)*lastdt/dist)
    print(t, dt, endt)
    if(t + dt > endt):
        dt = endt -t
    
    
    k1 = f(X +dt*k0, t+ dt)
    while(0.5*dt*np.sqrt((k1[1][0]-k0[1][0])**2 + (k1[1][1]-k0[1][1])**2)>TOL):
        dt /= 2
        k1 = f(X +dt * k0, t + dt)
    
    newX = X + 0.5*dt*(k0+k1)
    newt = t + dt
    if (0.5*dt*np.sqrt((k1[1][0]-k0[1][0])**2 + (k1[1][1]-k0[1][1])**2)<0.1*TOL):
        dt *= 2
        
    return newX, newt, dt
    
def varTimeTrapezoid(L, x0, y0, f, TOL):
    maxN = 100
    x = np.zeros(maxN)
    y = np.zeros(maxN)
    y[0] = y0
    x[0] = x0
    delX=L/100
    for i in range(0, maxN-1):
        (x[i+1], y[i+1]),delX= varTimeTrapezoidStep(x[i], L, y[i], f, TOL,delX)
        if(x[i+1] >= L):
            break
    return x, y
    
def func(x,y): #den deriverte
    return np.cos(x)

def main():
    N = 100
    L = 4*np.pi
    TOL=0.02
    
    xAn = np.linspace(0,L,200)
    yAn = np.sin(xAn)
    #yAn=np.tan(xAn)
    
    xVTr, yVTr = varTimeTrapezoid(L, 0, 0, func, TOL)
    plt.figure(figsize=(15,8))
    p1, = plt.plot(xAn, yAn, label="Analytic")
   # p2, = plt.plot(xFE, yFE, label="Forward Euler")
    #p3, = plt.plot(xTr, yTr, label="Trapezoid")
    p4, = plt.plot(xVTr, yVTr,'ro', label="Variable Trapezoid")
    plt.legend(loc = 0,handles=[p1,p4])
    plt.show()
    
#main()
    