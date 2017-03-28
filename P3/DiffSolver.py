import numpy as np
import matplotlib.pyplot as plt

def forwardEulerStep(x, dx, y, f):
    return y + dx*f(x,y)

def forwardEuler(N, L, x0, y0, f):
    dx = L/N
    y = np.zeros(N)
    y[0] = y0
    for i in range(0, N-1):
        y[i+1] = forwardEulerStep(i*dx, dx, y[i], f)
    return y
    
def trapezoidStep(x, dx, y, f):
    k0 = f(x,y)
    k1 = f(x +dx, y + dx*k0)
    return y + 0.5*dx*(k0+k1)
    
def trapezoid(N, L, x0, y0, f):
    dx = L/N
    y = np.zeros(N)
    y[0] = y0
    for i in range(0, N-1):
        y[i+1] = trapezoidStep(i*dx, dx, y[i], f)
    return y
    
def varTimeTrapezoidStep(x, L, y, f, TOL):
    k0 = f(x,y)
    
    delX = L/100
    fk1 = f(x+delX, y + delX*k0)
    dx = np.sqrt((2*TOL)*delX/np.abs(fk1-k0))
    
    if(x+dx >L):
        dx = L - x
    
    k1 = f(x +dx, y + dx*k0)
    print(0.5*dx*abs(k1-k0)/TOL)
    return x + dx, y + 0.5*dx*(k0+k1)
    
def varTimeTrapezoid(L, x0, y0, f, TOL):
    maxN = 100
    x = np.zeros(maxN)
    y = np.zeros(maxN)
    y[0] = y0
    x[0] = x0
    for i in range(0, maxN-1):
        x[i+1], y[i+1] = varTimeTrapezoidStep(x[i], L, y[i], f, TOL)
        if(x[i+1] >= L):
            break
    return x, y
    
def func(x,y):
    return np.cos(x)

def main():
    N = 100
    L = 8*np.pi
    
    
    xAn = np.linspace(0,L,200)
    yAn = np.sin(xAn)
    
    xFE = np.linspace(0,L,N)
    yFE = forwardEuler(N, L, 0, 0, func)
    
    xTr = np.linspace(0,L,N)
    yTr = trapezoid(N, L, 0, 0, func)
    
    xVTr, yVTr = varTimeTrapezoid(L, 0, 0, func, 0.02)
    
    p1, = plt.plot(xAn, yAn, label="Analytic")
    p2, = plt.plot(xFE, yFE, label="Forward Euler")
    p3, = plt.plot(xTr, yTr, label="Trapezoid")
    p4, = plt.plot(xVTr, yVTr,'ro', label="Variable Trapezoid")
    plt.legend(loc = 0,handles=[p1, p2, p3, p4])
    plt.show()
    plt.show()

main()
    