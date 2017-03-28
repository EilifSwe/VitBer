def f(X, t):
    x = X[0]
    y = X[1]
    R = np.sqrt(x*x + y*y)
    a = 2*np.pi*R/24
    return [-a*y, a*x]
    
    