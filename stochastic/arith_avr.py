'''
Created on Nov 8, 2015

@author: ds-ga-1007
'''
import numpy as np
import math
n=10000
def generateC_Y():
    m=12
    r=0.01
    sigma=0.2
    T=1
    K=100
    Ari_s=np.ones((n,m))
    Ari_s[:,0]=110
    Ari_c=[0]*n
    for i in range(n):
        for j in range(m-1):
            Ari_s[i,j+1]=Ari_s[i,j]*math.exp((r-sigma*sigma*0.5)+sigma*np.random.randn())
        AriAvrS=np.sum(Ari_s[i,:])/m
        #print i,s[i],AriAvrS
        if AriAvrS>=K:
            Ari_c[i]=(math.exp(-r*T)*(AriAvrS-K))
    #print c,len(c)
    return Ari_c   

C_Y=generateC_Y()
Avr_Y=np.mean(C_Y)
Var_Y=np.sum(np.square((np.array(C_Y)-Avr_Y)))/n
#Var_Y=np.square(np.std(C_Y))
#print Avr_Y,Var_Y,np.std(C_Y)
print C_Y
print Avr_Y,Var_Y
#print C_Y-Avr_Y,sum(C_Y-Avr_Y)





    

