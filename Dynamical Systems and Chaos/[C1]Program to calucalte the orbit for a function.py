# -*- coding: utf-8 -*-

"""
Program to calculate the orbit for a function (Defined as = 2.5x(1-x)) 

"""

from matplotlib import pyplot as plt

seed = 0.55         #The seed value
Xt = [seed]      #The orbit list
iterations = 50 #number of obersvations in the orbit

for i in range(0,iterations):
    x = 2.5*seed*(1-seed) #the definiton of the function
    Xt.extend([x])
    seed = x
    
#print "The Orbit for f(x) = 2.5x(1-x) is : ", Xt, "\n The length of the orbit is set to : ", len(Xt);
length = len(Xt)

plt.plot(range(1, length + 1), Xt)
plt.xlabel("Time")
plt.ylabel("Xt")
plt.show()


