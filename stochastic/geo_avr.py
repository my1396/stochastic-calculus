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
n=50
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
while j<=m:    
    sigma_bar_square+=(2*j-1)*(m+1-j)
    j+=1

for i in range(n):
    GeoAvrS=s0*math.exp((r-sigma*sigma*0.5)*T_bar+sigma/m*math.sqrt(sigma_bar_square)*sigma*np.random.randn())
    print i,GeoAvrS
    if GeoAvrS>=K:
        c[i]=(math.exp(-r*T)*(GeoAvrS-K))

print c        
print sum(c)/n

    

