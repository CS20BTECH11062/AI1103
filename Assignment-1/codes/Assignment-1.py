# Simulation to verify prob 1.4 using numpy
import random as rn
import numpy as np
import matplotlib.pyplot
from scipy.stats import binom


# binom.pmf function returns the binomial distribution of the variable
# after accepting the variable,probabilities and sample_size
def binomial(k):
    return binom.pmf(k, 10, 0.9)


# Initialising 2 lists to store the theoretical and simulated probabilities
prob_theo = [0 for i in range(11)]
prob_sim = [0 for j in range(11)]
for i in range(11):
    prob_theo[i] = binomial(i)

# denoting right handed as 0 and left handed as 1
people = [0, 1]
# choosing our sample of 10 people as the size of result of each outcome
num_people = 10
# assigning 'left' and 'right' probabilities
probabilities = [0.9, 0.1]

print("Let us run the simulation 1000000 times and check the number of cases in which at most 6 are right handed")
# declaring our simulation size as 1000000
sim = 1000000
# initialising at most 6 cases to 0
at_most_six_cases = 0
# running the loop 'sim' times to get an unbiased sample
for i in range(sim):
    num_right = 0
    # np.random.choice function takes in the cases(people here) , size of the list(num_people here) and probabilities of success
    # and returns a random list with the entries considering the probabilities
    outcome = np.random.choice(people, size=num_people, p=probabilities)
    for j in outcome:
        if j == 0:
            num_right += 1
    if num_right <= 6:
        at_most_six_cases += 1
        # the above code calculates the number of right handed peoples in the
        # generated random sample and increments at_most_six_cases if the condition is satisfied
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
    # The above code updates the corresponding elements of prob_sim
    # after checking the number of right_handed people in the random sample
print("Result of Simulation:")
print("The number of cases out of 1000000 in which at most 6 were right handed is", at_most_six_cases)
print("Thus the probability that at most 6 out of a random sample of 10 will be 'right' handed is",
      at_most_six_cases / sim)
print("And the simulated probability", at_most_six_cases / sim, "is close to", 0.012795198,
      "which we received using binomial distribution")
# now prob_sim list contains the number of times each of 0,1,2..10 right handed people in the random sample
# To get probabilities(simulated), we divide all the elements of prob_sim by sim.
for i in range(11):
    prob_sim[i] = prob_sim[i] / sim

cases = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# np.arrange returns len(cases) = 11 evenly spaced points to plot the graph
x = np.arange(len(cases))
# matplotlib.pyplot.bar function draws a bar graph of
matplotlib.pyplot.bar(x + 0.00, prob_theo, color='black', width=0.25, label='Calculated')
# we are then setting the positions of the two plots,the lists prob_theo,prob_sim whose values are plotted in the
# respective graphs and their respective colors and their widths.
matplotlib.pyplot.bar(x + 0.25, prob_sim, color='yellow', width=0.25, label='Simulated')
# xlabel and ylabel displays the x and y tags of the graph
matplotlib.pyplot.xlabel('No of person(s) who are right handed')
matplotlib.pyplot.ylabel('Probabilities')
# xticks function accepts the points and the list whose items are displayed in the accepted points.
matplotlib.pyplot.xticks(x + 0.25 / 2, cases)
# legends function displays the color of the plot and its label above the graph
matplotlib.pyplot.legend()
# show function wraps the entire graph and displays it
matplotlib.pyplot.show()
