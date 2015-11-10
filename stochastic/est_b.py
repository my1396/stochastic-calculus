'''
Created on Nov 9, 2015

@author: ds-ga-1007
'''
from arith_avr import *
from geo_avr import *
print n
C_X,S_T=generateC_X()
Avr_X=sum(C_X)/n
Var_X=np.square(np.std(C_X))
print "geometric average payoff:", Avr_X
print "variance of geometric average payoff: ", Var_X
C_Y=generateC_Y()
Avr_Y=np.mean(C_Y)
Var_Y=np.square(np.std(C_Y))
print "arithmetic average payoff:", Avr_Y
print "variance of arithmetic average payoff: ", Var_Y
#print C_X
#print C_Y
#print C_X,Avr_X
Cov_XY=np.sum((np.array(C_X)-Avr_X)*(np.array(C_Y)-Avr_Y))/n
print "cov[x,y]: ",Cov_XY
b_star=Cov_XY/Var_X
print "optimal value of b: ", b_star
rho=Cov_XY/math.sqrt(Var_X*Var_Y) # rho is correlation coefficient
print "correlation coefficient: ",rho
speed_up=1/(1-np.square(rho))
print "variance reduction factor(speed-up): ", speed_up
Y_b_star_bar=Avr_Y-b_star*(Avr_X-S_T)
print "The price of the Asian Option on the arithmetic average is: ",Y_b_star_bar
Var_Y_b_star_bar=1/n*(Var_Y-2*b_star*Cov_XY+np.square(b_star)*Var_X)
print "variance of the variance reduction technique: ",Var_Y_b_star_bar





