import numpy as np
import matplotlib.pyplot as plt

def jpdf(x,y):
    if (0<y<x and 0<x<1):
        return 6*(1-x)
    else:
        return 0
x = np.arange(0,2,0.1)
y = np.arange(0,2,0.1)
result = []
for i in np.nditer(x):
    for j in np.nditer(y):
        result.append(jpdf(i,j))

plt.plot(result)
plt.show()


    