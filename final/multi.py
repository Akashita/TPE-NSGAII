from random import Random
from time import time

import inspyred
from inspyred import ec
from inspyred.benchmarks import Benchmark

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math


def resolve_multi(problem, parameters):
    prng = Random()
    prng.seed(time())

    #      In parameters from 0 -> 4
    #           pop_size | nmb_gen | p_crossover | p_mutation

    ea = inspyred.ec.emo.NSGA2(prng)
    ea.variator = [inspyred.ec.variators.blend_crossover,
                   inspyred.ec.variators.gaussian_mutation]
    ea.terminator = inspyred.ec.terminators.generation_termination

    final_pop = ea.evolve(generator=problem.generator,
                          evaluator=problem.evaluator,
                          pop_size=parameters[0],
                          maximize=problem.maximize,
                          bounder=problem.bounder,
                          crossover_rate=parameters[2],
                          mutation_rate=parameters[3],
                          max_generations=parameters[1])
    final_arc = ea.archive

    return final_arc




def plot_multi(coords, objective):
    if objective == 2:
        plt.xlabel('Function 1')
        plt.ylabel('Function 2')
        plt.scatter(coords[0], coords[1], color='r')
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




#SCH PROBLEM
class SCH(Benchmark):
    def __init__(self):
        self.dimensions = 1
        self.nmb_functions = 2
        Benchmark.__init__(self, self.dimensions, self.nmb_functions)
        self.bounder = ec.Bounder([-10.0], [10.0])
        self.maximize = False

    def generator(self, random, args):
        return [random.uniform(-10.0, 10.0) for _ in range(self.dimensions)]

    def evaluator(self, candidates, args):
        fitness = []
        for c in candidates:
            f1 = c[0]**2
            f2 = (c[0] - 2)**2
            fitness.append(ec.emo.Pareto([f1, f2]))
        return fitness


class FON(Benchmark):
    def __init__(self, dimensions=2):
        self.dimensions = dimensions
        self.nmb_functions = 2
        Benchmark.__init__(self, self.dimensions, self.nmb_functions)
        self.bound5er = ec.Bounder([-4]*self.dimensions,
                                  [4]*self.dimensions)
        self.maximize = False

    def generator(self, random, args):
        return [random.uniform(-4, 4) for _ in range(self.dimensions)]

    def evaluator(self, candidates, args):
        fitness = []
        for c in candidates:
            c = np.array(c)
            f1 = 1 - np.exp(-np.sum((c - 1/(len(c)**.5))**2))
            f2 = 1 - np.exp(-np.sum((c + 1/(len(c)**.5))**2))
            fitness.append(ec.emo.Pareto([f1, f2]))
        return fitness
