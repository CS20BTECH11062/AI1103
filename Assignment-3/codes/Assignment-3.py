#importing numpy which contains functions for calculating exponential probabilities
#and math which helps calculate exp()
import numpy as np
import math
#initialising the values of A's and B's bulb probabilities to
#calculate prob_theo
pr_A = 0.2
pr_B = 0.8
#l_A and l_B are the inverse of means of A and B plants
l_A = 1/6
l_B = 1/2

#the following function calculates the cumulative probability distribution of exponential variables
#which we then use to assign values for pr_works_given_A and pr_works_given_B

def exp_cumulative(x,l):
    if x >= 0:
        return 1 - math.exp(-l*x)
    else:
        return 0
pr_works_given_A = 1 - exp_cumulative(12,l_A)
pr_works_given_B = 1 - exp_cumulative(12,l_B)

#theo_prob calculates the theoretical probability using bayes theorem and the probability values
#we assigned and calculated
theo_prob = pr_A*pr_works_given_A/(pr_A*pr_works_given_A+ pr_B*pr_works_given_B)

#creating 2 exponential probability samples of sizes such that it matches their probabilities
plantA = np.random.exponential(6,2500000)
plantB = np.random.exponential(2,10000000)
#B produces 4* as many bulbs as A
#the following 2 variables monitors the number of bulbs in the samples that 
#work after 12 months from A and B
works_after_12_months_a = 0
works_after_12_months_b = 0
#we now loop through the 2 samples and update the number of bulbs
#that works after 12 months
for i in plantA:
    if i>12:
        works_after_12_months_a += 1
for i in plantB:
    if i>12:
        works_after_12_months_b += 1
#total_works gives the total number of bulbs that worked after 12 months
total_works = works_after_12_months_a + works_after_12_months_b
#prob gives the probability that the bulb is from plant A given that
#it works after 12 months
sim_prob = works_after_12_months_a/total_works
print(sim_prob)
print("The simulated probability",sim_prob,'is close to the calculated probability',theo_prob)
