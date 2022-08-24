# -------------------------------------------------------------------------------
# Name:        Birthday Paradox
# Purpose:     Fun/Games
#
# Author:      rnicolescu
#
# Created:     24/08/2022
# Copyright:   (c) rnicolescu 2022
# Licence:     <your license here>
# ------------------------------------------------------------------------------
'''
In probability theory, the birthday problem asks for the probability that, in a set of n randomly chosen people, at least two will share a birthday.
The birthday paradox is that, counterintuitively, the probability of a shared birthday exceeds 50% in a group of only 23 people.
The birthday paradox is a veridical paradox: it appears wrong, but is in fact true.
While it may seem surprising that only 23 individuals are required to reach a 50% probability of a shared birthday,
this result is made more intuitive by considering that the comparisons of birthdays will be made between every possible pair of individuals.
With 23 individuals, there are (23 × 22) / 2 = 253 pairs to consider, much more than half the number of days in a year.
Real-world applications for the birthday problem include a cryptographic attack called the birthday attack,
which uses this probabilistic model to reduce the complexity of finding a collision for a hash function,
as well as calculating the approximate risk of a hash collision existing within the hashes of a given size of population.
The problem is generally attributed to Harold Davenport in about 1927, though he did not publish it at the time.
Davenport did not claim to be its discoverer "because he could not believe that it had not been stated earlier".
The first publication of a version of the birthday problem was by Richard von Mises in 1939.

source: https://en.wikipedia.org/wiki/Birthday_problem
'''


from random import *

class Birthday_Paradox:

    def __init__(self, groups, simulations):

        self.groups = groups
        self.simulations = simulations


    def calculate_probability(self):

        stat = {'Same': 0, 'Not_same': 0}
        for i in range(self.simulations):
            days = []
            for j in range(self.groups):
                day = randint(1, 366)
                days.append(day)

            if len(days) == len(set(days)):
                stat['Not_same'] += 1
            else:
                stat['Same'] += 1
        print (f'Probability for at least 2 with same birthday in a group of {self.groups} and runing  {self.simulations} simulations is:')
        return (f"P(A) = {stat['Same'] / (stat['Same'] + stat['Not_same'])*100:.2f}%")


if __name__ == "__main__":

    groups = int(input("Enter the number of groups for calculating:"))
    simulations = int(input('Enter the number of simulations to run:'))
    paradox_birthday = Birthday_Paradox(groups, simulations)
    print(paradox_birthday.calculate_probability())

