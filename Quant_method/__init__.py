import numpy as np

def euro_call(s0,r,sigma,T):
    rand_num=np.random.randn()
    S_T=s0*np.exp((r-0.5*sigma*sigma)*T+sigma*(T**1.0/2)*rand_num)
    return S_T
