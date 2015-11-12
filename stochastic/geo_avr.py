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
n=10000
def generateC_X():
    m=12
    interval=1.0/m
    r=0.01
    sigma=0.2
    T=1
    K=100
    s=np.ones((n,m))
    s[:,0]=110
    c=[0]*n
    T_bar=sum(np.array(range(m+1))*interval)/m
    sigma_bar_square=0
    j=1
    
    Ari_s=np.ones((n,m))
    Ari_s[:,0]=110
    Ari_c=[0]*n
    #S_T=s0*math.exp(sigma*np.random.randn()+r-0.5*)
    while j<=m:    
        sigma_bar_square+=(2*j-1)*(m+1-j)*interval
        #print j,sigma_bar_square
        j+=1
    #print 'attention', sigma_bar_square
    sigma_bar_square_GBM=sigma_bar_square*sigma*sigma/(n*n*T_bar)
    delta=0.5*sigma*sigma-0.5*sigma_bar_square_GBM
    d=(np.log(s[0,0]/K)+(r-delta+0.5*sigma_bar_square_GBM)*T_bar)/np.sqrt(sigma_bar_square_GBM*T_bar)
    S_T=np.exp(-delta*T_bar)*s[0,0]*norm.cdf(d)-np.exp(-r*T_bar)*K*norm.cdf(d-np.sqrt(sigma_bar_square_GBM*T_bar))                                                            
    print "S_T",S_T
    for i in range(n):
        rand_list=[]
        for j in range(m-1):
            rand_num=np.random.randn()
            rand_list.append(rand_num)
            Ari_s[i,j+1]=Ari_s[i,j]*math.exp((r-sigma*sigma*0.5)*interval+sigma*interval**(1.0/2)*rand_num)
            #print rand_list
            s[i,j+1]=s[i,j]*math.exp((r-sigma*sigma*0.5)*interval+sigma*(interval)**(1.0/2)*rand_num)   
        AriAvrS=np.sum(Ari_s[i,:])/m
        GeoAvrS=np.prod(s[i,:])**(1.0/m)
        '''
        print i
        print s[i,:],GeoAvrS
        print Ari_s[i,:],AriAvrS
        '''
        #GeoAvrS=s[0,0]*math.exp((r-sigma*sigma*0.5)*T_bar+sigma/m*math.sqrt(sigma_bar_square)*np.random.randn())
        #print i,GeoAvrS
        if GeoAvrS>=K:
            c[i]=(math.exp(-r*T)*(GeoAvrS-K))
        if AriAvrS>=K:
            Ari_c[i]=(math.exp(-r*T)*(AriAvrS-K))
    #print c
            
    return c,S_T,Ari_c
 
C_X,S_T,C_Y=generateC_X() 
print "C_X: ",C_X
print "C_Y: ",C_Y
print "S_T: ",S_T
Avr_X=sum(C_X)/n
Var_X=np.square(np.std(C_X))
Avr_Y=sum(C_Y)/n
Var_Y=np.square(np.std(C_Y))
Cov_XY=np.sum((np.array(C_X)-Avr_X)*(np.array(C_Y)-Avr_Y))/n
print "geometric average payoff:", Avr_X
print "variance of geometric average payoff: ", Var_X
print "arithmetic average payoff:", Avr_Y
print "variance of arithmetic average payoff: ", Var_Y
print "cov[x,y]: ",Cov_XY
b_star=Cov_XY/Var_X
print "optimal value of b: ", b_star
rho=Cov_XY/math.sqrt(Var_X*Var_Y) # rho is correlation coefficient
print "correlation coefficient: ",rho
speed_up=1/(1-np.square(rho))
print "variance reduction factor(speed-up): ", speed_up
Y_b_star_bar=Avr_Y-b_star*(Avr_X-S_T)
print "The price of the Asian Option on the arithmetic average is: ",Y_b_star_bar
Var_Y_b_star_bar=1.0/n*(Var_Y-2*b_star*Cov_XY+np.square(b_star)*Var_X)
print "variance of the variance reduction technique: ",Var_Y_b_star_bar
#print C_X
print Avr_X,Var_X,S_T



    

