from multi import *

import numpy as np
import time

import inspyred
from inspyred import ec
from inspyred.benchmarks import Benchmark

from tkinter import *

#------------------------------------------------------------
#     Functions
#------------------------------------------------------------


def question(demande,default):
    entree = 'a'#To do the loop at least once
    while not entree.lower() in ['','y','n']:
        entree = input(demande)
    if entree == '':
        return default
    return entree.lower() == 'y'


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

def euclidian_distance(pointA,pointB):
    #return the euclidian distance between two point
    if len(pointB) != len(pointA):
        print("Erreur : les points ne sont pas dans la même dimension")
    somme = 0
    for i in range(len(pointA)):
        somme += (pointA[i] - pointB[i])**2
    return math.sqrt(somme)



#------------------------------------------------------------
#     Main program beginning
#------------------------------------------------------------

def resolve_problems(parameters, problem, objective):
    time_start = time.time()
    final_arc = resolve_multi(problem, parameters)
    time_end = time.time() - time_start
    print("\n --- Executing time : ", time_end, "--- \n")
    coords = transform_coord(final_arc, objective)
    hypervolume = inspyred.ec.analysis.hypervolume(coords[3], reference_point=None)

    return hypervolume

problem = SCH()

objective = 2

pop_size = 50
nmb_gen = 50
p_crossover = 0.5
p_mutation = 0.5

parameters = [pop_size,  nmb_gen,  p_crossover,  p_mutation]
print("Hypervolume :",resolve_problems(parameters, problem, objective))
