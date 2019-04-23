from multi import *
import matplotlib.pyplot as plt
import numpy as np
import time

import inspyred
from inspyred import ec
from inspyred.benchmarks import Benchmark

def transform_coord(final_arc, nb_objective):
    #------------------------------------------------------------
    #     WARNING: The next function return the coordinates of
    #        the points of the pareto, but also a fitness tab which
    #        is the principal argument of the hypervolume function
    #------------------------------------------------------------
    fit = []
    x = []
    y = []
    z = []
    for i in final_arc:
        fit.append(i.fitness)
        x.append(i.fitness[0])
        y.append(i.fitness[1])
        if nb_objective == 3:
            z.append(i.fitness[2])
    return x,y,z,fit

def plot_multi(coords, objective):
    if objective == 2:
        plt.scatter(coords[0], coords[1], color='b')
        plt.show()

    elif objective == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x = coords[0]
        y = coords[1]
        z = coords[2]
        ax.scatter(x, y, z, c='r', marker='o')


        ax.set_xlabel('Function 1')
        ax.set_ylabel('Function 2')
        ax.set_zlabel('Function 3')

        plt.show()

#------------------------------------------------------------
#     Main program beginning
#------------------------------------------------------------

pas = 1
gen_range = 50

problem = inspyred.benchmarks.DTLZ1(objectives=3, dimensions=3)
objective = 3
#pop, gen, cross, mut
parameters = [20, 0, 0.1, 0.1]

problem_return = []

for turn in range(1,gen_range+1,pas):
    parameters[1] = turn


    final_arc = resolve_multi(problem, parameters)
    coords = transform_coord(final_arc, objective)
    hypervolume = inspyred.ec.analysis.hypervolume(coords[3], reference_point=None)

    problem_return.append([hypervolume, coords])


plt.plot([Z[0] for Z in problem_return])
plt.show()
