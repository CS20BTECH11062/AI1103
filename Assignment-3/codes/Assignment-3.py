import numpy as np
import matplotlib.pyplot as plt


plantA = np.random.exponential(6,250000)
plantB = np.random.exponential(2,1000000)

works_in_a = 0
works_in_b = 0
for i in plantA:
    if i>12:
        works_in_a += 1
for i in plantB:
    if i>12:
        works_in_b += 1
total_works = works_in_b + works_in_a
prob = works_in_a/total_works
print(prob)

