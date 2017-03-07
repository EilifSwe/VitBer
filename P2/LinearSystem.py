import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve

def makeAMatrix(N, beta): #beta er liste med betaverdier og N er antall kroker
    k=4*N
    A=np.zeros((k,k))
    Left_square = np.array([[6.0,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,1]])
    Right_square = np.array([[-6.0,0,0,0],[-6,-2,0,0],[-3,-2,-1,0],[-1,-1,-1,-1]])
    
    for i in range(0, N):
        j = (i + N - 1) % N
        #Venstre blokk
        A[4*i][4*j]=6
        A[4*i+1][4*j]=6
        A[4*i+1][4*j+1]=2
        A[4*i+2][4*j]=3
        A[4*i+2][4*j+1]=2
        A[4*i+2][4*j+2]=1
        A[4*i+3][4*j]=1
        A[4*i+3][4*j+1]=1
        A[4*i+3][4*j+2]=1
        A[4*i+3][4*j+3]=1
        
        #Høyre blokk
        A[4*i][4*i]=-6
        A[4*i][4*i+3]=-beta[i]
        A[4*i+1][4*i+1]=-2
        A[4*i+2][4*i+2]=-1
        A[4*i+3][4*i+3]=-1
    return A
    
def makeUVector(N,alpha): #N antall kroker, a = alfa
    return np.array([alpha,0.5*alpha,alpha/6,alpha/24]*N)
    
def calculateXVector(A, U):
    return np.linalg.solve(A, U)
    

def printMatrix(A):
    for i in range(len(A)):
        print (A[i])
        
def updateAMatrix(betaList,A, N):
    for i in range(N):
        A[4*i, 4*i+3]=-betaList[i]

        
        
        
#I det følgende løses oppgave 4        
def calculateSparseXVector(A,U):
    return spsolve(A.tocsc(), U)
    
def makeSparseAMatrix(N, beta):
    A = sparse.dok_matrix((4*N, 4*N))
    for i in range(0, N):
        j = (i + N - 1) % N
        #Venstre blokk
        A[4*i, 4*j]=6
        A[4*i+1, 4*j]=6
        A[4*i+1, 4*j+1]=2
        A[4*i+2, 4*j]=3
        A[4*i+2, 4*j+1]=2
        A[4*i+2, 4*j+2]=1
        A[4*i+3, 4*j]=1
        A[4*i+3, 4*j+1]=1
        A[4*i+3, 4*j+2]=1
        A[4*i+3, 4*j+3]=1
        
        #Høyre blokk
        A[4*i, 4*i]=-6
        A[4*i, 4*i+3]=-beta[i]
        A[4*i+1, 4*i+1]=-2
        A[4*i+2, 4*i+2]=-1
        A[4*i+3, 4*i+3]=-1


    return A

    

    
    
        
    