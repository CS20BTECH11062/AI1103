#importing the numpy,random and scipy modules which we use later
import numpy as np
import random
from scipy.stats import hypergeom

#initialising values of red and black balls,num_trials and the number of black balls to be chosen for success(2)
red_balls = 4
black_balls = 6
num_trials = 3
num_black_success = 2
print("A  box  contains  4  red  balls  and  6  black  balls.Three  balls  are  selected  randomly  from  the  box one after another, without replacement. What is the probability that the selected set contains one red ball and two black balls?")

#initialising a list which simulates the given bag of balls with 4 red and 6 black balls
bag_orig = ['red','red','red','red','black','black','black','black','black','black']

#calculating theoretical probability by feeding in initialised values to built-in hypergeometric 
#distribution's pmf calculator
theo_prob = hypergeom.pmf(num_black_success,red_balls+black_balls,num_trials,black_balls)
print("The calculated Probability that the selection contains one red and 2 black balls is",theo_prob)

#initialising number of success in simulations to 0
num_success = 0
#bag_calc is a sample during each iteration initialising it to bag_orig after every 3 iterations
bag_calc = ['red','red','red','red','black','black','black','black','black','black']
#choices store the 3 random choices during each 3-choices. 
choices = ["Choice-1","Choice-2","Choice-3"]
#sim contains the number of times the event is run 
sim = 1000000
for j in range(sim):
    for i in range(3):
        #we are choosing a random element from bag_calc
        #and removing the element after selecting it
        var = random.choice(bag_calc)
        choices[i] = var
        bag_calc.remove(var)
    #reinitialising bag_calc with bag_orig
    bag_calc = bag_orig.copy()
    #if the selection contains 2 black balls , we increment success by 1
    if choices.count('black') == 2:
        num_success += 1
#calculating sim_prob by dividing number of successes by total number of simulations
sim_prob = num_success/sim
print("The simulated probability after taking into account",sim,"cases  that the selection contains one red and 2 black balls is",sim_prob)
print("Thus we notice that the simulated probability",sim_prob,"is close to the calculated probability",theo_prob)
print("And both of them are approximately equal to 0.5")

