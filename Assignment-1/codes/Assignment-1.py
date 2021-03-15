# Simulation to verify prob 1.4 using numpy
import random as rn
import numpy as np
import matplotlib.pyplot
from scipy.stats import binom

def binomial(k):
    return binom.pmf(k,10,0.9)

prob_theo = [0 for i in range(11)]
prob_sim = [0 for j in range(11)]
for i in range(11):
    prob_theo[i] = binomial(i)



#denoting right handed as 0 and left handed as 1
people = [0,1]
#choosing our sample of 10 people as the size of result of each outcome
num_people = 10
#assigning 'left' and 'right' probabilities
probabilities = [0.9,0.1]

print("Let us run the simulatation 1000000 times and check the number of cases in which at most 6 are right handed")
#declaring our simulation size
sim = 1000000
#initialising at most 6 cases to 0
at_most_six_cases = 0
for i in range(sim):
    num_right = 0
    outcome = np.random.choice(people,size = num_people,p = probabilities)
    for j in outcome:
        if j == 0:
            num_right += 1
    if num_right <= 6:
        at_most_six_cases += 1
    if num_right == 0:
        prob_sim[0] += 1
    elif num_right == 1:
        prob_sim[1] += 1
    elif num_right == 2:
        prob_sim[2] += 1
    elif num_right == 3:
        prob_sim[3] += 1
    elif num_right == 4:
        prob_sim[4] += 1
    elif num_right == 5:
        prob_sim[5] += 1
    elif num_right == 6:
        prob_sim[6] += 1
    elif num_right == 7:
        prob_sim[7] += 1
    elif num_right == 8:
        prob_sim[8] += 1
    elif num_right == 9:
        prob_sim[9] += 1
    elif num_right == 10:
        prob_sim[10] += 1

print("Result of Simulation:")
print("The number of cases out of 1000000 in which at most 6 were right handed is",at_most_six_cases)
print("Thus the probability that at most 6 out of a random sample of 10 will be 'right' handed is",at_most_six_cases/sim)
print("And the simulated probability",at_most_six_cases/sim,"is close to",0.012795198,"which we received using binomial distribution")

for i in range(11):
    prob_sim[i] = prob_sim[i]/sim

cases = ["0","1","2","3","4","5","6","7","8","9","10"]


x = np.arange(len(cases))
matplotlib.pyplot.bar(x + 0.00, prob_theo, color = 'black', width = 0.25, label = 'Calculated')
matplotlib.pyplot.bar(x + 0.25, prob_sim, color = 'yellow', width = 0.25, label = 'Simulated')
matplotlib.pyplot.xlabel('No of person(s) who are right handed')
matplotlib.pyplot.ylabel('Probabilities')
matplotlib.pyplot.xticks(x  + 0.25/2,cases)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()