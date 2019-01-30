from single import *
from multi import *
import numpy as np

import inspyred
from inspyred import ec
from inspyred.benchmarks import Benchmark

pop_size = 200
nmb_gen = 40
p_crossover = 0.5
p_mutation = 0.5

parameters =[pop_size,  nmb_gen,  p_crossover,  p_mutation]

"""
problem = inspyred.benchmarks.Ackley(dimensions = 2)
X,Y = np.mgrid[-5:5:0.25, -5:5:0.25]
Z = (-20) * np.exp((-0.2) * np.sqrt(0.5*((X**2)+(Y**2)))) - np.exp(0.5*(np.cos(2*np.pi*X) + np.cos(2*np.pi*Y))) + np.exp(1) + 20

final_pop = resolve_single(True,problem,parameters)
plot_single(final_pop, X, Y, Z)
"""

problem = problem = inspyred.benchmarks.DTLZ2()
resolve_multi(True, problem,parameters)
