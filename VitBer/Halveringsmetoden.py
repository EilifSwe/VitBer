
#halveringsmetoden
def halvering(x1,x2,f, x, my, ua, ub, A, U_AVG): 
    #skal kun returnere a og b
    m=(x1+x2)/2
    print(f(x, x1, my, ua, ub, A,U_AVG))
    print(f(x, m, my, ua, ub, A,U_AVG))
    print(f(x, x2, my, ua, ub, A,U_AVG))
    if f(x, m, my, ua, ub, A,U_AVG)==0:
        return x1,x2
    elif (f(x, m, my, ua, ub, A, U_AVG)*f(x, x1, my, ua, ub, A, U_AVG)<0):
        x1=x1
        x2=m
    elif(f(x, m, my, ua, ub, A, U_AVG)*f(x, x2, my, ua, ub, A, U_AVG)<0):
        x1=m
        x2=x2
    return x1,x2
    
def finn_sigma(x1,x2, TOL, temp, x, my, ua, ub, A, U_AVG):
    while (abs(x2-x1)>TOL):
        #print(x1, x2)
        x1,x2=halvering(x1,x2,temp, x, my, ua, ub, A, U_AVG)
    
    return (x1+x2)/2