#importing the numpy,random and scipy modules which we use later
import numpy as np
import random
from scipy.stats import hypergeom

#initialising values of defective and non-defective items,num_trials and the number of defective items to be chosen for success(2)
defective_items = 20
non_defective_items = 80
num_trials = 2
num_defective_success = 2

print("A  box  contains  20  defective  items  and  80  non-defective items. If two items are selected at random without  replacement,  what  will  be  the  probability that both items are defective?")

#initialising a list which simulates the given set of items with 20 defective and 80 non-defective items
defective = ['defective' for i in range(20)]
non_defective = ['non-defective' for i in range(80)]
item_orig = defective + non_defective

#calculating theoretical probability by feeding in initialised values to built-in hypergeometric 
#distribution's pmf calculator
theo_prob = hypergeom.pmf(num_defective_success,non_defective_items+defective_items,num_trials,defective_items)
print("The calculated Probability that the selection contains one red and 2 black balls is",theo_prob)

#initialising number of success in simulations to 0
num_success = 0
#item_calc is a sample during each iteration initialising it to bag_orig after every 3 iterations
item_calc = item_orig.copy()
#choices store the 2 random choices during each 2-choices. 
choices = ["Choice-1","Choice-2"]
#sim contains the number of times the event is run 
sim = 1000000
for j in range(sim):
    for i in range(2):
        #we are choosing a random element from item_calc
        #and removing the element after selecting it
        var = random.choice(item_calc)
        choices[i] = var
        item_calc.remove(var)
    #reinitialising item_calc with item_orig
    item_calc = item_orig.copy()
    #if the selection contains 2 defective items , we increment success by 1
    if choices.count('defective') == 2:
        num_success += 1
#calculating sim_prob by dividing number of successes by total number of simulations
sim_prob = num_success/sim
print("The simulated probability after taking into account",sim,"cases  that the selection contains one red and 2 black balls is",sim_prob)
print("Thus we notice that the simulated probability",sim_prob,"is close to the calculated probability",theo_prob)
print("And both of them are approximately equal to 0.038")