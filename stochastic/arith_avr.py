'''
Created on Nov 8, 2015

@author: ds-ga-1007
'''
import numpy as np
import math
n=50
m=12
r=0.01
sigma=0.2
T=1
K=100
s=np.ones((n,m))
s[:,0]=110
c=[0]*n
for i in range(n):
    for j in range(m-1):
        s[i,j+1]=s[i,j]*math.exp((r-sigma*sigma*0.5)+sigma*np.random.randn())
    AriAvrS=np.sum(s[i,:])/m
    print i,s[i],AriAvrS
    if AriAvrS>=K:
        c[i]=(math.exp(-r*T)*(AriAvrS-K))
        
print sum(c)/n
    

