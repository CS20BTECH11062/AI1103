#importing the numpy module to use uniform distribution
import numpy as np
#defining the simulation size
sim = 1000000
#initialising the sum of random variables 
sum_random_var = 0
#defining the upper and lower bound for the random variables
lower_bound = 0
upper_bound = 1
#defining number of rv's to be created on each trial
num_var = 1
#creating a function to calculate M_n by performing sim number of trials
def calc_M_n(sim):
#performing the action 'sim' times and incrementing sum_random_var by U_i
    global sum_random_var
    for i in range(sim):
        U_i = np.random.uniform(lower_bound,upper_bound,num_var)
        sum_random_var += U_i[0]
    #finally calculating M_n by dividing sum_random_var by sim
    M_n = sum_random_var/sim
    return M_n
print("The simulated M_n",calc_M_n(sim),"is close to the calculated mean",(upper_bound+lower_bound)/2)
