# -*- coding: utf-8 -*-

from random import Random
from time import time
import inspyred
from inspyred import ec
from inspyred.benchmarks import Benchmark
import matplotlib.pyplot as plt
import numpy as np
import math

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


# FON PROBLEM
class FON(Benchmark):
    def __init__(self, dimensions=2):
        self.dimensions = dimensions
        self.nmb_functions = 2
        Benchmark.__init__(self, self.dimensions, self.nmb_functions)
        self.bounder = ec.Bounder([-4]*self.dimensions,
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


#==============================================================================
# Choose problem and parameters
#==============================================================================

# CHOOSE DEFAULT PARAMETERS
pop_size = 20
nmb_gen = 40
p_crossover = 0.5
p_mutation = 0.5
affichage = False


# CHOOSE THE RANGE AND THE STEP OF THE VARIATION
list_pop_size = [x for x in range(2,1000,10)]
list_nmb_gen = [x for x in range(5,100,5)]
list_p_crossover = [x for x in range(42)]
list_p_mutation = [x for x in range(42)]


# CHOSE A PROBLEM IN THE LIST

problem = SCH()
# problem = FON(2)
# problem = inspyred.benchmarks.Kursawe(3)
# problem = inspyred.benchmarks.DTLZ1(dimensions=2, objectives=2)
# problem = inspyred.benchmarks.DTLZ2()
# problem = inspyred.benchmarks.DTLZ3()
# problem = inspyred.benchmarks.DTLZ4()
# problem = inspyred.benchmarks.DTLZ5()
# problem = inspyred.benchmarks.DTLZ6()
# problem = inspyred.benchmarks.DTLZ7(dimensions=3, objectives=3)

#==============================================================================
# Solve
#==============================================================================
def resolve_problem(param):
    global problem
    global indice
    global affichage

    global pop_size
    global nmb_gen
    global p_crossover
    global p_mutation

    global list_pop_size
    global list_nmb_gen
    global list_p_crossover
    global list_p_mutation


    prng = Random()
    prng.seed(time())
    ea = inspyred.ec.emo.NSGA2(prng)
    ea.variator = [inspyred.ec.variators.blend_crossover,
                   inspyred.ec.variators.gaussian_mutation]
    ea.terminator = inspyred.ec.terminators.generation_termination
    if param == 'pop_size':
        pop_size = list_pop_size[indice]
    elif param == 'nmb_gen':
        nmb_gen = list_nmb_gen[indice]
    elif param == 'p_crossover':
        p_crossover = list_p_crossover[indice]
    elif param == 'p_mutation':
        p_mutation = list_p_mutation[indice]
    final_pop = ea.evolve(generator=problem.generator,
                          evaluator=problem.evaluator,
                          pop_size=pop_size,
                          maximize=problem.maximize,
                          bounder=problem.bounder,
                          crossover_rate=p_crossover,
                          mutation_rate=p_mutation,
                          max_generations=nmb_gen)

    

    if affichage:
        #==============================================================================
        # Plot
        #==============================================================================
        final_arc = ea.archive
        x = []
        y = []
        for f in final_arc:
            x.append(f.fitness[0])
            y.append(f.fitness[1])
        plt.scatter(x, y, color='b')
        xp = np.linspace(0, 4, 100)
        yp = (xp**.5 - 2)**2
        plt.plot(xp, yp, 'r')
        plt.show()
        
    return ea    
    


def pred_pareto_ref(x):
    y = (x**.5 - 2)**2
    return y

def calcr(ea):
    final_arc = ea.archive
    tot=[]
    for i in final_arc:
        tot.append([i.fitness[0],i.fitness[1]])
    x = np.array([i[0] for i in tot])
    y = np.array([i[1] for i in tot])
    r = 1 - (sum((y - pred_pareto_ref(x))**2)/sum((y - np.mean(y))**2))
    print(r)

for indice in range(10):
    print('\n',indice,'\npop_size = ',list_pop_size[indice])
    resolve_problem('pop_size')
    calcr(resolve_problem('pop_size'))

print("Done")
