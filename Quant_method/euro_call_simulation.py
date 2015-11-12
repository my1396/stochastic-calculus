'''
Created on Nov 12, 2015

@author: ds-ga-1007
'''
import numpy as np

class Monte_Carlo():
    def __init__(self,s0,r,sigma,T,K):
        self.s0=s0
        self.r=r
        self.sigma=sigma
        self.T=T
        self.K=K
        
    def underlying_simu(self):
        rand_num=np.random.randn()
        self.S_T=self.s0*np.exp((self.r-0.5*self.sigma*self.sigma)*self.T+self.sigma*(self.T**1.0/2)*rand_num)
        return self.S_T