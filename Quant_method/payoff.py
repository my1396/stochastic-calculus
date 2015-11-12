'''
Created on Nov 12, 2015

@author: ds-ga-1007
'''
import numpy as np
from Quant_method.Monte_Carlo import *

def euro_call_simu(s0,r,sigma,T,K):
    underlying_initial=Monte_Carlo(s0,r,sigma,T,K)
    underlying_end_price=underlying_initial.underlying_simu()
    C_T=0
    if underlying_end_price >K:
        C_T=np.exp(-underlying_initial.r*underlying_initial.T)*(underlying_end_price-K)
    return C_T

def cash_or_nothing_binary_call_option(s0,r,sigma,T,K,Q):
    underlying_initial=Monte_Carlo(s0,r,sigma,T,K)
    underlying_end_price=underlying_initial.underlying_simu()
    C_T=0
    if underlying_end_price >= K:
        C_T=Q
    return C_T
    

def result(list):
    return np.mean(list)