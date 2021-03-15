# Simulation to verify prob 1.4 using numpy
import random as rn
import numpy as np

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
print("Result of Simulation:")
print("The number of cases out of 1000000 in which at most 6 were right handed is",at_most_six_cases)
print("Thus the probability that at most 6 out of a random sample of 10 will be 'right' handed is",at_most_six_cases/sim)
print("And the simulated probability",at_most_six_cases/sim,"is close to",0.012795198,"which we received using binomial distribution")