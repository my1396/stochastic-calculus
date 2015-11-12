'''
Created on Nov 12, 2015

@author: ds-ga-1007
'''
def getreplicationnumber():
    tmp=raw_input("please enter an integer as replication times for MC simulation:\nn= ")
    return int(tmp)

def getparametersfor_underlying():
    print "please enter parameters for the underlying:"
    s0=raw_input("current stock price: s0= ")
    r=raw_input("risk free rate: r= ")
    sigma=raw_input("diffusion coefficicent: sigma= ")
    T=raw_input("maturity: T= ")
    return float(s0),float(r),float(sigma),float(T)

def getparameterfor_Euro_call():
    print "please enter parameter(strike price) for European Call Option:"
    K=raw_input("strike price: K= ")
    return float(K)

def getQfor_Binary_call():
    K=raw_input("strike price: K= ")
    print "fixed amount payoff Q, if S_T > K: "
    Q=raw_input("Q= ")
    return float(K),float(Q)
    
