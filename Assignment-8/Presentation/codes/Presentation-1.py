#importing the required packages for plotting, pi symbol and integration
import numpy as np
from scipy.integrate import quad
import random
import matplotlib.pyplot as plt
import math

#the following defines the given probability density
def prob_density(t):
    return 1/(np.pi * (1+t**2))

#f_1 and f_2 functions give the probability density of X/3 and Y/3
def f_1(x):
    return 3 * prob_density(3*x)

def f_2(y):
    return 3 * prob_density(3*y)

#the following function calculates the integrand for convolution function
def integrand(y,z):
    return f_1(z-y)*f_2(y)    

#the quad function performs the integral and gives the convolution function 
def convolution(z):
    return quad(integrand,-np.inf,np.inf,args=(z))[0]



#the answer function calculates the answer from calculations to check whether it matches with concolution's output
def ans(z):
    return 6/(np.pi * (4+9*(z**2)))


#We now plot both convolution and ans functions to check it they're the same.
x_axis = np.arange(-20,20)
y_axis_conv = []
y_axis_init = []
y_axis_ans = []
for i in x_axis:
    y_axis_conv.append(convolution(i))
    y_axis_init.append(prob_density(i))
    y_axis_ans.append(ans(i))


plt.plot(x_axis,y_axis_init,color = 'r',label = 'X and Y')
plt.plot(x_axis,y_axis_conv,color = 'b',label = "X+Y/3")
plt.xlabel("t")
plt.ylabel("Probability (variable = t)")
plt.legend()
plt.show()
