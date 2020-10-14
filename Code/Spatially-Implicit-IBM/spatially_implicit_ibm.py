##################################
##################################
### This script is for a spatially-implicit individual-based model comprising
### part of an overall project addressing prey switching as a function of both
### traits and climate
##################################
##################################
### Author: Cole B. Brookson
### Date Created: 2020-10-05
##################################
##################################

import numpy as np
import matplotlib.pyplot as plt

## ------------- Test Section

###### write birth function
def birth(inds: np.array, lamda: float, reproduction_column: int):
    """ Function will take in an array of prey individuals and perform a birth
    function on all the individuals in the array. In this function, the number
    of birth events for an individual B_i is sampled from a Poisson distribution
    with 0.5 expected offspring per time step.

    Parameters:
                individuals(array): an array of size (x,y), where y = 4 is the
                                    column to put the reproductive value in
                lambda(float):      defines the mean and variance of the poisson
                                    distribution
                reproduction_column(int): the column that the reproduction value
                                    should be input into
    Return:
                inds(array):        a new array of individuals with the data
                                    from the old iteration plus that from the new one
    """
    num_individuals = len(inds[0])
    num_columns = inds.shape[0]
    inds[3] = np.random.poisson(0.5, num_individuals)
    total_offspring = int(sum(inds[3]))

    #add all new offspring to inds array
    new_inds = np.zeros((4, total_offspring))
    new_inds[0] = range(len(inds[0]), (len(inds[0]) + total_offspring)) #individual number
    new_inds[1] = np.random.normal(100, 5.0, total_offspring) #random body size
    new_inds[2] = np.random.binomial(1, 0.5, total_offspring) #availability (1 o 0)

    #bind the old and new together
    inds_0 = np.append(inds[0], new_inds[0])
    inds_1 = np.append(inds[1], new_inds[1])
    inds_2 = np.append(inds[2], new_inds[2])

    #re-create the inds array with the new values
    inds = np.zeros((4, len(inds_0)))
    inds[0] = inds_0
    inds[1] = inds_1
    inds[2] = inds_2

    return inds

###### prey
inds = np.zeros((4, 100))
inds[0] = range(1,101) #individual number
inds[1] = np.random.normal(100, 5.0, 100) #random body size
inds[2] = np.random.binomial(1,0.5,100) #availability (1 o 0)
 # last one will be reproduction

time = 5
for i in range(1,time):
    inds = birth(inds, 0.5, 3)
