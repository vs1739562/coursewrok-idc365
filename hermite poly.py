# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:20:50 2021

@author: gamma
"""
#Choose simple units
m=1.
w=1.
hbar=1.

import matplotlib.pyplot as plt
from pylab import rcParams;
rcParams['figure.figsize'] = 10, 10
fig = plt.figure(figsize = (8,8))

import numpy as np
import numpy.polynomial.hermite as Herm
import math
import matplotlib
import matplotlib.pyplot as plt 
def hermite(x,n):
    xi = np.sqrt(m*w/hbar)*x
    herm_coeffs = np.zeros(n+1)
    herm_coeffs[n] = 1
    return Herm.hermval(xi, herm_coeffs)
#Discretized space
dx = 0.05
x_lim = 12
x = np.arange(-x_lim,x_lim,dx)


def stationary_state(x,n):
    xi = np.sqrt(m*w/hbar)*x
    prefactor = 1./math.sqrt(2.**n * math.factorial(n)) * (m*w/(np.pi*hbar))**(0.25)
    psi = prefactor * np.exp(- xi**2 / 2) * hermite(xi,n)
    return psi

#plt.figure()
#plt.plot(x, stationary_state(x,4))
#plt.xlabel(r"x")
#plt.ylabel(r"$\psi_4(x)$")
#plt.title(r"Test Plot of $\psi_4(x)$")
#plt.show()




import scipy.integrate as integrate
Cf_1 = np.zeros((5,5)) #first order transistion coefficient
CF_1 = np.zeros(5)
time = np.zeros(5)
fvi = np.zeros(5)

for f in range(5):
    result = integrate.quad(lambda x: stationary_state(x, f+1)*stationary_state(x, 1),-1 ,1)
    
    fvi[f] = result[0]**2
    #Cf_1[i] = result[0] ## this is just probability <f|V|i> where i took V = 1
    #print(type(Cf_1[i]))
    for t in range(5):
        time[t]=t
        a =( np.exp(complex(0,1)*(f)*w*t)-1)  
        
        
        res1 = a /(f+1) ## this is a/(w-w(fi))
        res = complex( result[1],0) *res1 ### this is  transistion probability for particular vallue of f(final state )
            ## particular value of t 
            
            
        
            #print(abs(res))
        CF_1[t] = res  ## transition coefficient with resoect to t having fixed f

        Cf_1[f,t]= res
        
            
P = np.square(Cf_1)            
colours = ['r','g','b','k']            
for i in range(5):
    
    if i != 0:
        
    #ax1= fig.add_subplot(1,1,1)
       plt.plot(time,P[i,:], label = "Transistion probability over time: P(1 to " + str(i+1)+ ")")
       plt.xlabel("time")
       plt.ylabel("Transistion probability")
       plt.yscale("log")
       plt.legend(loc = "best",fancybox=True, shadow=True, prop={'size':'small'})  
       
fig = plt.figure(figsize = (10,10))       

for i in range(5):
    

    
    if i != 0:
        
    #ax1= fig.add_subplot(1,1,1)
       plt.plot(time,P[:,i], label = " Transistion Probabilty P varying with state  for fixed time at " + str(i)+ " sec")
       plt.xlabel("state")
       plt.ylabel('Transistion probability' )
       plt.yscale("log")
      
       plt.legend(loc = "upper center",fancybox=True, shadow=True, prop={'size':'small'})         
          
    #ax1= fig.add_subplot(1,1,1)
fig = plt.figure(figsize = (8,8))         
plt.plot(time,fvi, label = "|<f|V|i>|^2" )
plt.xlabel("f")
plt.ylabel("|<f|V|i>|^2")
plt.yscale("log")
plt.legend(loc = "best",fancybox=True, shadow=True, prop={'size':'small'})         
             
#print(Cf_1)
   
#plt.figure()
#plt.plot(time, CF_1)
#plt.xlabel(r"x")
#plt.ylabel(r"$\psi_4(x)$")
#plt.title(r"Test Plot of $\psi_4(x)$")
#plt.show() 
   
 


