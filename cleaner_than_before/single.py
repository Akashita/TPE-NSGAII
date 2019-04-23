from time import time
from random import Random
import inspyred
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def resolve_single(problem, parameters):

    #      In parameters from 0 -> 4
    #           pop_size | nmb_gen | p_crossover | p_mutation

    prng = Random()
    prng.seed(time())

    ea = inspyred.ec.GA(prng)
    ea.terminator = inspyred.ec.terminators.evaluation_termination
    final_pop = ea.evolve(generator=problem.generator,
                          evaluator=problem.evaluator,
                          pop_size=parameters[0],
                          maximize=problem.maximize,
                          bounder=problem.bounder,
                          crossover_rate=parameters[2],
                          mutation_rate=parameters[3],
                          max_evaluations=parameters[1],
                          num_elites=1)
    return final_pop

def plot_single(final_pop, X, Y, Z):
    #     Constrution of range :
    #       [min, max, step]

    #------------------------------------------------------------
    #     The representation of the last generation
    #-----------------------------------------------------------
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    yolo = max(final_pop)
    #ax.scatter([X.candidate[0] for X in final_pop], [Y.candidate[1] for Y in final_pop], [Z.fitness for Z in final_pop], c="r", marker="o")
    ax.scatter(yolo.candidate[0], yolo.candidate[1], yolo.fitness, c="r", marker="o")
    #------------------------------------------------------------
    #     The representation of the function
    #------------------------------------------------------------
    ax.plot_wireframe(X, Y, Z, alpha=0.2)
    #ax.plot_surface(X, Y, Z, alpha=0.5, cmap="hot")

    #------------------------------------------------------------
    #     Set labels
    #------------------------------------------------------------
    ax.set_xlabel('Variable X1')
    ax.set_ylabel('Variable X2')
    ax.set_zlabel('F(X1,X2)')

    plt.show()
