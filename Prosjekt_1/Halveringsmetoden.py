import Parametere as par

def halvering(sLow,sHigh,f, x, A, fLow,fHigh): 
#sLow og sHigh er gjetninger på sigma, fLow og fHigh er funksjonsverdien for gjetningene.
    
    sMid=(sLow+sHigh)/2 #midtpunktet
    fMid=f(x, sMid, A) #funksjonsverdi i midtpunktet
    if fMid==0:
        return sMid, sMid, fLow, fHigh
    
    elif(fMid*fLow < 0): #Nullpunktet finnes i det venstre intervallet
        sHigh = sMid 
        fHigh=fMid
        
    elif(fMid*fHigh<0): #Nullpunktet finnes i det høyre intervallet
        sLow = sMid
        fLow=fMid
    
    return sLow, sHigh, fLow, fHigh #Returnerer funksjonsverdier for gjenbruk til neste iterasjon

def finn_sigma(sLow, sHigh, temp, x, A):
    fLow=temp(x, sLow, A) #Funksjonsverdier til initielle gjetninger
    fHigh=temp(x,sHigh,A)
    
    while (abs(sHigh-sLow)>par.TOL): #Her kjøres halveringsmetoden helt til akseptabel sigma er funnet
        sLow, sHigh,fLow,fHigh=halvering(sLow,sHigh,temp, x, A,fLow,fHigh)
    return (sLow+sHigh)/2
