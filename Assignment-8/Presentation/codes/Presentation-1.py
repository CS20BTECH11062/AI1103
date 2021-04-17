from scipy.stats import cauchy
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random as rn
sim_len = 1000000

X = cauchy.rvs(size=sim_len)
Y = cauchy.rvs(size=sim_len)
Z = []
K = []
count = []


def ans(z):
    return 6/(np.pi * (4+9*(z**2)))


for i in range(sim_len):
    k = (X[i] + Y[i])/3
    Z.append(round(k,2))
    #K.append(ans((X[i]+Y[i])/3)
s = rn.randint(0,sim_len)
print(Z.count(Z[s])/sim_len,ans(Z[s]))