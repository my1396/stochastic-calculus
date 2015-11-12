'''
Created on Nov 12, 2015

@author: ds-ga-1007
'''
def getreplicationnumber():
    tmp=raw_input("please enter an interger as replication time for MC simu:\nn= ")
    return int(tmp)

def getparameterfor_Euro_call():
    print "please enter parameters for European Call Option:"
    s0=raw_input("current stock price: s0= ")
    r=raw_input("risk free rate: r= ")
    sigma=raw_input("diffusion coefficicent: sigma= ")
    T=raw_input("maturity: T= ")
    K=raw_input("strike price: K= ")
    #float(s0),float(r),float(sigma),float(T),float(K)
    return float(s0),float(r),float(sigma),float(T),float(K)
    
