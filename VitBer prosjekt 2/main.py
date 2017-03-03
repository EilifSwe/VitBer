import numpy as np
import random as r
import matplotlib.pyplot as plt

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

def makeUVector(N,a): #N antall kroker, a = alfa
    return np.array([a,0.5*a,a/6,a/24]*N)
    
def calculateXVector(A, U):
    return np.linalg.solve(A, U)
        
def printMatrix(A):
    for i in range(len(A)):
        print (A[i])
        
def updateAMatrix(beta,A, N):
    for i in range(N):
        A[4*i][4*i+3]=-beta[i]
    
    
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
    ksi = np.linspace(0, N - 0.00001, 1000)
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

def plotSubEta(nr,N,xArray,alpha):
    
    fig_solution = plt.figure(figsize=(15,10))
    
    ax_y = fig_solution.add_subplot(411)
    plt.setp(ax_y.get_xticklabels(), visible=False)
    plotEta(0, N,xArray, alpha)
    plt.title("$\eta(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta$)",fontsize=20)

    
    ax_dy = fig_solution.add_subplot(412, sharex=ax_y)
    plt.setp(ax_dy.get_xticklabels(), visible=False)
    plotEta(1, N, xArray, alpha)
    plt.title("$\eta'(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta'$)",fontsize=20)
                
    ax_ddy = fig_solution.add_subplot(413, sharex=ax_y)
    plt.setp(ax_ddy.get_xticklabels(), visible=False)
    plotEta(2, N, xArray, alpha)
    plt.title("$\eta''(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.ylabel("Utslag, ($\eta''$)",fontsize=20)
    
    ax_dddy = fig_solution.add_subplot(414, sharex=ax_y)
    plotEta(3, N, xArray, alpha)
    plt.title("$\eta'''(\\xi)$",fontsize=20)
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15
    plt.xlabel("$k$ (antall kroker), ($\\xi$)",fontsize=20)
    plt.ylabel("Utslag, ($\eta'''$)",fontsize=20)
    
    plt.tight_layout()
    plt.savefig("eta_ksi_vitber2.pdf")
    
def findNextBreak(t_list, beta, x_vector):
    nextBreak=0
    max_r=0
    for i in range(len(t_list)):
        #Iterates through all the hooks and finds the biggest r-value
        r=-x_vector[4*i+3]*beta[i]/t_list[i]
        if (r)>max_r:
            max_r=r 
            nextBreak=i
        #print(-r, i)
    return nextBreak, max_r
    #Returns the index of the next hook that breaks and corresponding max_r

def make_t_list(N, limit):
    t_list=np.zeros(N)
    for i in range(len(t_list)):
        t_list[i]=r.random()*limit
    return t_list
    

#Main
def main():
    N = 10
    beta=53.05*np.ones(N)
    beta[2] = 0
    
    print(beta)
    alpha = 10
    
    A = makeAMatrix(N, beta)
    #beta[2] = 0
    #updateAMatrix(beta, A, N)
    printMatrix(A)
    U = makeUVector(N, alpha)

    X = calculateXVector(A, U)
    print(X)
    plotEta(0, N, X, alpha)
    
    
def plotAlpha():
    N = 100
    M = 100
    beta = 53.05*np.ones(N)
    tList = make_t_list(N, 0.04)
    A = makeAMatrix(N, beta)
    U = makeUVector(N, 1)
    
    alpha = np.zeros(N)
    iteration = range(N)
    
    for i in range(M):
        beta = 53.05*np.ones(N)
        updateAMatrix(beta, A, N)
        tList = make_t_list(N, 0.04)
        for k in range(0, N):
            xRef = calculateXVector(A, U)
            # plotEta(0,N,xRef, 1)
            betaIndex, rValue = findNextBreak(tList, beta, xRef)
            # print(betaIndex, rValue)
            alpha[k] += beta[betaIndex] / rValue
            #print(betaIndex, alpha[k])
            beta[betaIndex] = 0
            updateAMatrix(beta, A, N)
    
    plt.plot(iteration, alpha/M)
    plt.show()
    
    
#main()
plotAlpha()
