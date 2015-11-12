'''
Created on Nov 12, 2015

@author: ds-ga-1007
'''
from payoff import *
from getinput import *

def main():
    print "Do you want to use the default number? Y/N"
    print "default setting: [n,s0,r,sigma,T,K]=[1000,120,0.01,0.2,1,100]"
    set_initial=raw_input()
    if set_initial=="Y":
        n=1000
        s0=120
        r=0.01
        sigma=0.2
        T=1
        K=100
    else:
        n=getreplicationnumber()
        s0,r,sigma,T,K=getparameterfor_Euro_call()
    C_T=[0]*n
    for i in range(n):
        C_T[i]=euro_call_simu(s0,r,sigma,T,K)
    estimateofC=result(C_T)
    print "list of C_T: (length:%d)" % (len(C_T))
    print ['%.2f' % elem for elem in C_T]
    print "The time of C[i]=0 in the simulation: %d" % (C_T.count(0))
    print "MC simulation for price of European Call Option is: ",estimateofC
    
if __name__=="__main__":
    main()
    
