import numpy as np

#Double derivative of the i-th lagrange polynomial in x_k
def ddLagrange(x, i, k):
    ans = 0
    if i == k:
        sum1 = 0
        sum2 = 0
        for j in range(0, len(x)):
            if j != i:
                l = (x[k]-x[j])
                sum1 += 1.0/l
                sum2 += 1.0/(l*l)
        ans = sum1 * sum1 - sum2
        
    else:
        koff = 1
        for j in range(0, len(x)):
            if(j != i):
                koff *= 1/(x[i]-x[j])
        
        sum = 0
        for j in range(0, len(x)):
            if j != i and j != k:
                product = 1
                for l in range(0,len(x)):
                    if l!= i and l != k and l != j:
                        product *= x[k]-x[l]
                sum += product
        ans = 2 * koff * sum
    
    return ans

# set up the LHS (left hand side) for the spectral method for Laplace eqn
def spectral_laplace_lhs(x):
    N = len(x)
    a,b = x[0],x[N-1]
    A = np.zeros((N,N))
    
    #Calculate A
    A[0][0] = 1
    A[N-1][N-1] = 1
    for row in range(1, N-1):
        for col in range(0, N):
            A[row][col] = -ddLagrange(x, col, row)
    print(A)
    
    return A

# set up the RHS (right hand side) for the spectral method for Laplace eqn
def spectral_laplace_rhs(x,f,ua,ub):
    N = len(x)
    a,b = x[0],x[N-1]
    B = np.zeros(N)
    
    B[0] = ua
    B[N-1] = ub
    for i in range(1, N-1):
        B[i] = f(x[i])
    print (B)
    return B

# set up the spectral method for Laplace eqn and solve the resulting system
def spectral_laplace(x,f,ua,ub):
    A = spectral_laplace_lhs(x)
    B = spectral_laplace_rhs(x,f,ua,ub)
    # solve the system
    return np.linalg.solve(A,B)

def printPoints(x, y):
    for i in range(0, len(x)):
        print("(", x[i], ",", y[i], "),", end="")
    print()    
    

def run():
    N = 20
    a = 0
    b = 5
    ua = 0
    ub = 0
    my = 2.0
    sigma = 1.0
    
    x_uniform = np.linspace(a,b,N)
    x_cheby = (b+a)/2. + (a-b)/2. * np.cos(np.arange(N)*np.pi/(N-1))

    print(x_uniform)
    y = spectral_laplace(x_uniform, lambda x : np.exp(-((x-my)**2)/sigma), ua, ub)
    printPoints(x_uniform, y)

run()