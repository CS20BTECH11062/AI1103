import numpy as np
from scipy.integrate import quad
import random

def prob_density(t):
    return 1/(np.pi * (1+t**2))

def f_1(x):
    return 3 * prob_density(3*x)

def f_2(y):
    return 3 * prob_density(3*y)

def integrand(y,z):
    return f_1(z-y)*f_2(y)

def convolution(z):
    return quad(integrand,-np.inf,np.inf,args=(z))[0]

def ans(z):
    return 6/(np.pi * (4+9*(z**2)))


for i in range(10):
    x = random.randint(1,100)
    print("[",x,":",convolution(x),":",ans(x),"]")

print("Thus we've verified that our solution is correct")

import matplotlib.pyplot as plt
x_axis = np.arange(-20,20)
y_axis_conv = []
y_axis_init = []
for i in x_axis:
    y_axis_conv.append(convolution(i))
    y_axis_init.append(prob_density(i))
    
plt.plot(x_axis,y_axis_conv,color = 'r',label = 'X and Y')
plt.plot(x_axis,y_axis_init,color = 'b',label = "X+Y/3")
plt.xlabel("t")
plt.ylabel("Probability (variable = t)")
plt.legend()
plt.show()

