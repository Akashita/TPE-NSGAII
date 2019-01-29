from random import Random
from time import time
import inspyred
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np


pop_size = 2000
nmb_gen = 10000
p_crossover = 0.5
p_mutation = 0.5


def main(prng=None, display=True):

    global pop_size
    global nmb_gen
    global p_crossover
    global p_mutation

    if prng is None: #Pseudo Random Number Generator (PRNG)
        prng = Random()
        prng.seed(time())

    problem = inspyred.benchmarks.Ackley(2)
    ea = inspyred.ec.GA(prng)
    ea.terminator = inspyred.ec.terminators.evaluation_termination
    final_pop = ea.evolve(generator=problem.generator,
                          evaluator=problem.evaluator,
                          pop_size=pop_size,
                          maximize=problem.maximize,
                          bounder=problem.bounder,
                          crossover_rate=p_crossover,
                          mutation_rate=p_mutation,
                          max_evaluations=nmb_gen, #I'm not sure about this one
                          num_elites=1)

    best = max(final_pop)
    print('Best Solution: \n{0}'.format(str(best)))

    if display:
        graph(best)


def graph(best):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    print(best.candidate[0])
    ax.scatter(best.candidate[0],best.candidate[1], best.fitness, c="r", marker="o"
    )

    X, Y = np.mgrid[-5:5:0.25, -5:5:0.25]
    Z = (-20)*np.exp((-0.2)*np.sqrt(0.5*((X**2)+(Y**2))))-np.exp(0.5*(np.cos(2*np.pi*X)+np.cos(2*np.pi*Y)))+np.exp(1)+20

    ax.plot_wireframe(X, Y, Z, alpha=0.2, cmap="hot")
    #ax.plot_surface(X, Y, Z, alpha=0.5, cmap="hot")

    ax.set_xlabel('Variable X1')
    ax.set_ylabel('Variable X2')
    ax.set_zlabel('F(X1,X2)')

    plt.show()


main()
