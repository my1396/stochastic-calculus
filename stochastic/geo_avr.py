'''
Created on Nov 8, 2015

@author: ds-ga-1007
'''
'''
Created on Nov 8, 2015

@author: ds-ga-1007
'''
import numpy as np
import math
from scipy.stats import norm
n=50
def generateC_X():
    m=12
    r=0.01
    sigma=0.2
    T=1
    K=100
    s0=110
    c=[0]*n
    T_bar=sum(range(m+1))/m
    sigma_bar_square=0
    j=1
    #S_T=s0*math.exp(sigma*np.random.randn()+r-0.5*)
    while j<=m:    
        sigma_bar_square+=(2*j-1)*(m+1-j)
        #print j,sigma_bar_square
        j+=1
    #print 'attention', sigma_bar_square
    sigma_bar_square_GBM=sigma_bar_square*sigma*sigma/(n*n*T_bar)
    delta=0.5*sigma*sigma-0.5*sigma_bar_square_GBM
    d=(np.log(s0/K)+(r-delta+0.5*sigma_bar_square_GBM)*T_bar)/np.sqrt(sigma_bar_square_GBM*T_bar)
    S_T=np.exp(-delta*T_bar)*s0*norm.cdf(d)-np.exp(-r*T_bar)*K*norm.cdf(d-np.sqrt(sigma_bar_square_GBM*T_bar))                                                            
    print "S_T",S_T
    for i in range(n):
        GeoAvrS=s0*math.exp((r-sigma*sigma*0.5)*T_bar+sigma/m*math.sqrt(sigma_bar_square)*sigma*np.random.randn())
        #print i,GeoAvrS
        if GeoAvrS>=K:
            c[i]=(math.exp(-r*T)*(GeoAvrS-K))
    return c,S_T
 
C_X,S_T=generateC_X()          
Avr_X=sum(C_X)/n
Var_X=np.square(np.std(C_X))
print Avr_X,Var_X,S_T



    

