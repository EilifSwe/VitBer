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
    
def varTimeTrapezoidStep(x, L, y, f, TOL,delX):
    k0 = f(x,y) #stigning  i startpunkt
    
    fk1 = f(x+delX, y + delX*k0) 
    dx = 0.8*np.sqrt((2*TOL)*delX/np.abs(fk1-k0))
    
    if(x+dx >L):
        dx = L - x
    
    k1 = f(x +dx, y + dx*k0)
    while(0.5*dx*abs(k1-k0)>TOL):
        dx=dx/2
        k1 = f(x +dx, y + dx*k0)
    if (0.5*dx*abs(k1-k0)<0.1*TOL):
        dx=2*dx
    print(0.5*dx*abs(k1-k0)/TOL)
    newpoint=x + dx, y + 0.5*dx*(k0+k1)
    if (0.5*dx*abs(k1-k0)<0.3*TOL):
        dx=2*dx
        #print("hurra :D")
    return newpoint,dx
    
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
    