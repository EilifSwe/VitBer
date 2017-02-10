import numpy as np
import Parametere as par

#Dobelt deriverte av det i-te lagrange polynomet evaluert i x_k
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


#Funksjon for a kalkulere A matrisen
def calculate_A_Matrix(x):
    N = len(x)
    a,b = x[0],x[N-1]
    A = np.zeros((N,N))
    
    #Calculate A
    A[0][0] = 1
    A[N-1][N-1] = 1
    for row in range(1, N-1):
        for col in range(0, N):
            A[row][col] = ddLagrange(x, col, row)

    return A

#Funksjon for a kalkulere B vektoren
def calculate_B_Vector(x, ua, ub, sigma, f):
    N = len(x)
    a,b = x[0],x[N-1]
    B = np.zeros(N)    

    B[0] = ua
    B[N-1] = ub
    for i in range(1, N-1):
        B[i] = -f(sigma, x[i])

    return B

#Funksjon for a kalkulere U vektoren
def calculate_U_Vector(A, B):
    return np.linalg.solve(A,B) #Loeser likningsystemet AU=B