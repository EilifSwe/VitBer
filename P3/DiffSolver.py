import numpy as np
import matplotlib.pyplot as plt

def forwardEulerStep(t, dt, X, f):
    return X + dt*f(X,t)

def forwardEuler(dt, T, t0, X0, f):
    N=T/dt
    N_int=int(N)
    if N!=N_int:        #Hvis N er et desimaltall runder int(N) tallet ned, 
        N_int=N_int+1   #og det vil trengs et ekstra steg.
    X = np.asarray([np.zeros(2) for i in range(N_int+1)])        
    X[0] = X0
    for i in range(0, N_int):
        if i==N_int-1:          #Ved det siste steget velges det korteste av
            dt=min(dt,T-i*dt)   #tidssteget dt og differansen mellom totaltid og brukt tid.
        X[i+1] = forwardEulerStep(i*dt, dt, X[i], f)
    return X
    
def trapezoidStep(t, dt, X, f):
    k0 = f(X,t)
    k1 = f(X + dt*k0, t +dt,)
    return X + 0.5*dt*(k0+k1)
    
def trapezoid(dt, T, t0, X0, f):
    N=T/dt
    N_int=int(N)
    if N!=N_int:        #Hvis N er et desimaltall runder int(N) tallet ned, 
        N_int=N_int+1   #og det vil trengs et ekstra steg.
    X = np.asarray([np.zeros(2) for i in range(N_int+1)]) 
    X[0] = X0
    for i in range(0, N_int):
        if i==N_int-1:          #Ved det siste steget velges det korteste av
            dt=min(dt,T-i*dt)   #tidssteget dt og differansen mellom totaltid og brukt tid.
        X[i+1] = trapezoidStep(i*dt, dt, X[i], f)
    return X

#Oppgave 1d)
def varTimeTrapezoidStep(t, X, f, TOL, dt, e, endt):
    if(e < 0.5*TOL):    
        dt = 0.8*np.sqrt(TOL/e)*dt
    
    k0 = f(X,t)
    k1 = f(X+dt*k0, t + dt)
    
    while(True):
        e = np.linalg.norm(k1-k0)*dt/2  #linalg.norm sjekker XXXXX
        
        if(e < TOL):
            break
        
        if(np.isfinite(e)):
            dt = 0.8*np.sqrt(TOL/e)*dt
        else:
            dt /= 2
            
        if(t + dt > endt):
            dt = endt - t
        
        k1 = f(X+dt*k0, t + dt)
    
    newX = X + 0.5*dt*(k0+k1)
    newt = t + dt
    
    return newX, newt, dt, e

    
