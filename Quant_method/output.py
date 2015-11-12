'''
Created on Nov 12, 2015

@author: ds-ga-1007
'''
from payoff import *
from getinput import *

def main():
    choose_option=raw_input("which option you want to simulate?\n1. European Call Option   2.cash-or-nothing Binary call option\n1 or 2: ")
    n=getreplicationnumber()
    print "Do you want to use the default setting parameter? Y/N"
    print "default parameters are:\n[s0,r,sigma,T]=[120,0.01,0.2,1]\nK=100\nQ=10"
    set_initial=raw_input().upper()
    if set_initial=="Y":
        s0=120
        r=0.01
        sigma=0.2
        T=1
        K=100
        Q=10
    else:
        s0,r,sigma,T=getparametersfor_underlying()
        if choose_option=="1":
            K=getparameterfor_Euro_call()
        else:
            K,Q=getQfor_Binary_call()
    C_T=[0]*n
    for i in range(n):
        if choose_option=="1":
            C_T[i]=euro_call_simu(s0,r,sigma,T,K)
        else:
            C_T[i]=cash_or_nothing_binary_call_option(s0,r,sigma,T,K,Q)
    estimateofC=result(C_T)
    print "list of C_T: (Times of replication: %d)" % (len(C_T))
    print ['%.2f' % elem for elem in C_T]
    print "The times of C[i]=0 shown in the simulation: %d" % (C_T.count(0))
    if choose_option=="1":
        option="European Call Option"
    else:
        option="cash-or-nothing Binary call option"
    print "The option simulated is: %s" % (option) 
    print "MC simulation for price of %s is: %.2f" % (option,estimateofC)
    
if __name__=="__main__":
    main()
    
