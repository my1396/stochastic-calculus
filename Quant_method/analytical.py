'''
Created on Nov 17, 2015

@author: ds-ga-1007
'''
import math
from scipy.stats import norm

s0=120
r=0.01
sigma=0.2
T=1
K=100
Q=10
d_=1.0/(sigma*math.sqrt(T))*(math.log(float(s0)/K)+(r-0.5*sigma*sigma)*T)
d2=1.0/(sigma*math.sqrt(T))*(math.log(float(s0)/K)+(r+0.5*sigma*sigma)*T)
v=s0*norm.cdf(d2)-math.exp(-r*T)*K*norm.cdf(d_)
v_binary=math.exp(-r*T)*Q*norm.cdf(d_)
print "analytical result for Euro Call: ", v
print "analytical result for Binary Call: ",v_binary