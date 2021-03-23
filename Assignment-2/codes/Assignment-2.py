# Simulation to verify GATE prob 27 using numpy

import numpy as np
import matplotlib.pyplot
from scipy.stats import binom

# binom.pmf function returns the binomial distribution of the variable
# after accepting the variable,probabilities and sample_size
def binomial(k):
    return binom.pmf(k, 10, 0.5)


# Initialising 2 lists to store the theoretical and simulated probabilities
prob_theo = [0 for i in range(11)]
prob_sim = [0 for j in range(11)]
for i in range(11):
    prob_theo[i] = binomial(i)

# denoting head as 0 and tail as 1
dice = [0, 1]
# choosing our sample of 10 tosses as the size of result of each outcome
num_tosses = 10
# assigning 'head' and 'tail' probabilities
probabilities = [0.5, 0.5]

print("Let us run the simulation 1000000 times and check the number of cases in which ONLY the first two tosses are heads")
# declaring our simulation size
sim = 1000000
# initialising two_heads to 0
first_two_heads = 0
for i in range(sim):
    num_head = 0
    # outcome returns a random sample set of 10 tosses considering the probabilities
    outcome = np.random.choice(dice, size=num_tosses, p=probabilities)
    for j in outcome:
        if j == 0:
            num_head += 1
    # the above code calculates the number of heads in the
    # generated random sample and increments num_head if the condition is satisfied
    # checking number of heads for plotting the graph
    if num_head == 0:
        prob_sim[0] += 1
    elif num_head == 1:
        prob_sim[1] += 1
    elif num_head == 2:
        prob_sim[2] += 1
    elif num_head == 3:
        prob_sim[3] += 1
    elif num_head == 4:
        prob_sim[4] += 1
    elif num_head == 5:
        prob_sim[5] += 1
    elif num_head == 6:
        prob_sim[6] += 1
    elif num_head == 7:
        prob_sim[7] += 1
    elif num_head == 8:
        prob_sim[8] += 1
    elif num_head == 9:
        prob_sim[9] += 1
    elif num_head == 10:
        prob_sim[10] += 1
        # The above code updates the corresponding elements of prob_sim
        # after checking the number of heads in the random sample
    # if the number of heads is two in the sample then we check if the first and second tosses give 'head'
    if num_head == 2 and outcome[0] == 0 and outcome[1] == 0:
        first_two_heads += 1
print("Result of Simulation:")
print("The number of cases out of 1000000 in which ONLY first 2 tosses were heads", first_two_heads)
print("Thus the probability that ONLY the first two tosses out of a random sample of 10 will be 'heads' is",
      first_two_heads / sim)
print("And the simulated probability", first_two_heads / sim, "is close to", 0.0009765625,
      "which we received using binomial distribution")
# now prob_sim list contains the number of times each of 0,1,2..10 heads in random sample
# To get probabilities(simulated), we divide all the elements of prob_sim by sim.
for i in range(11):
    prob_sim[i] = prob_sim[i] / sim

cases = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# np.arrange returns len(cases) = 11 evenly spaced points to plot the graph
x = np.arange(len(cases))
# we are then setting the positions of the two plots,the lists prob_theo,prob_sim whose values are plotted in the
# respective graphs and their respective colors and their widths.
# matplotlib.pyplot.bar function draws a bar graph
matplotlib.pyplot.bar(x + 0.00, prob_theo, color='black', width=0.25, label='Calculated')
matplotlib.pyplot.bar(x + 0.25, prob_sim, color='cyan', width=0.25, label='Simulated')
# xlabel and ylabel displays the x and y tags of the graph
matplotlib.pyplot.xlabel('No of heads in 10 tosses')
matplotlib.pyplot.ylabel('Probabilities')
matplotlib.pyplot.xticks(x + 0.25 / 2, cases)
# show function wraps the entire graph and displays it
matplotlib.pyplot.legend()
# show function wraps the entire graph and displays it
matplotlib.pyplot.show()
