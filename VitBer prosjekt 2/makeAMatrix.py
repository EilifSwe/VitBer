import numpy as np

def makeAMatrix(beta, N): #beta er liste med betaverdier og N er antall kroker
    k=4*N
    A=np.zeros((k,k))
    Left_square = np.array([[6.0,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,1]])
    Right_square = np.array([[-6.0,0,0,0],[-6,-2,0,0],[-3,-2,-1,0],[-1,-1,-1,-1]])
    
    for i in range(N):
        j = (i + 1) % N
        #Venstre blokk
        A[4*i][4*i]=6
        A[4*i][4*i+3]=beta[i]
        A[4*i+1][4*i+1]=2
        A[4*i+2][4*i+2]=1
        A[4*i+3][4*i+3]=1
        #Høyre blokk
        A[4*i][4*j]=-6
        A[4*i+1][4*j]=-6
        A[4*i+1][4*j+1]=-2
        A[4*i+2][4*j]=-3
        A[4*i+2][4*j+1]=-2
        A[4*i+2][4*j+2]=-1
        A[4*i+3][4*j]=-1
        A[4*i+3][4*j+1]=-1
        A[4*i+3][4*j+2]=-1
        A[4*i+3][4*j+3]=-1
    return A
        
        
def printMatrix(A):
    for i in range(len(A)):
        print (A[i])
        
beta=np.ones(4)

def updateAMatrix(beta,A):
    for i in range(N):
        A[4*i][4*i+3]=beta[i]
    return A
    

#Main
A=makeAMatrix(beta,4)
printMatrix(A)

def makeUVector(N,a): #N antall kroker, a = alfa
    print(np.array([-a,-0.5*a,-a/6,-a/24]*N))
    
makeUVector(4,2)


        
        
    
    
