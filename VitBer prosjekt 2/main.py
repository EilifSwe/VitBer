import numpy as np
import matplotlib.pyplot as plt

def makeAMatrix(N, beta): #beta er liste med betaverdier og N er antall kroker
    k=4*N
    A=np.zeros((k,k))
    Left_square = np.array([[6.0,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,1]])
    Right_square = np.array([[-6.0,0,0,0],[-6,-2,0,0],[-3,-2,-1,0],[-1,-1,-1,-1]])
    
    for i in range(N):
        j = (i + 1) % N
        #Venstre blokk
        A[4*i][4*i]=6
        A[4*i+1][4*i]=6
        A[4*i+1][4*i+1]=2
        A[4*i+2][4*i]=3
        A[4*i+2][4*i+1]=2
        A[4*i+2][4*i+2]=1
        A[4*i+3][4*i]=1
        A[4*i+3][4*i+1]=1
        A[4*i+3][4*i+2]=1
        A[4*i+3][4*i+3]=1
        
        #Høyre blokk
        A[4*i][4*j]=-6
        A[4*i][4*j+3]=-beta[j]
        A[4*i+1][4*j+1]=-2
        A[4*i+2][4*j+2]=-1
        A[4*i+3][4*j+3]=-1
    return A

def makeUVector(N,a): #N antall kroker, a = alfa
    return np.array([a,0.5*a,a/6,a/24]*N)
    
def calculateXVector(A, U):
    return np.linalg.solve(A, U)
        
def printMatrix(A):
    for i in range(len(A)):
        print (A[i])
        
def updateAMatrix(beta,A):
    for i in range(N):
        A[4*i][4*i+3]=beta[i]
    return A
    
def eta(ksi, xArray, alpha):
    k = int(np.floor(ksi))
    x = ksi - k
    
    return (((-(alpha / 24.) *x + xArray[4*k])*x + xArray[4*k+1])*x + xArray[4*k+2])*x + xArray[4*k+3]

def dEta(ksi, xArray, alpha):
    k = int(np.floor(ksi))
    x = ksi - k
    return ((-(alpha / 6.) *x + 3*xArray[4*k])*x + 2*xArray[4*k+1])*x + xArray[4*k+2]
    
def ddEta(ksi, xArray, alpha):
    k = int(np.floor(ksi))
    x = ksi - k
    return (-(alpha / 2.) *x + 6*xArray[4*k])*x + 2*xArray[4*k+1]
    
def dddEta(ksi, xArray, alpha):
    k = int(np.floor(ksi))
    x = ksi - k
    
    return -alpha*x + 6*xArray[4*k]
    
def plotEta(nr, N, xArray, alpha):
    ksi = np.linspace(0, N - 0.001, 1000)
    etaArray = []
    
    func = None
    
    if (nr == 0):
        func = eta
    elif (nr == 1):
        func = dEta
    elif (nr == 2):
        func = ddEta
    elif (nr == 3):
        func = dddEta
    
    for i in ksi:
        etaArray.append(func(i, xArray, alpha))
    
    plt.plot(ksi, etaArray)
    plt.show()
    

#Main
def main():
    N = 10
    beta=53.05*np.ones(N)
    beta[4] = 30
    print(beta)
    alpha = 10
    
    A = makeAMatrix(N, beta)
    printMatrix(A)
    U = makeUVector(N, alpha)

    X = calculateXVector(A, U)
    print(X)
    plotEta(0, N, X, alpha)
    
main()
