from multi import *
import matplotlib.pyplot as plt
import numpy as np
import time

import inspyred
from inspyred import ec
from inspyred.benchmarks import Benchmark

problem = inspyred.benchmarks.DTLZ1(objectives=3, dimensions=3)

def str_nb(n,taille = 2):
    """écrit les nombres à la bonne taille, avec des 0 devant si ils sont trops courts"""
    ch = str(n)
    while len(ch) < taille:
        ch = '0' + ch
    return ch

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

def affiche(liste):
    for elem in liste:
        print(elem)

#pop_size, nmbgen , crossover , mutation_rate
#parameters = [1000, 40, 0.5, 0.5]
parameters = [100, 20, 0.5, 0.5]
liste_soluces = []
objective = 3

#On fait varier mutation
for mut in range(1,110, 10):
    parameters[3] = mut / 100
    print('mutation_rate : ', parameters[3] ,'\n\n')
    minimum = [] #Liste des meilleures solutions
    pas = 1 #Pas des gen
    max = 15 #Génération max

    for param in range(1 , max , pas):
        parameters[1] = param
        final_arc = resolve_multi(problem, parameters)
        coords = transform_coord(final_arc, objective)
        hypervolume = inspyred.ec.analysis.hypervolume(coords[3], reference_point=None)
        minimum.append(hypervolume)
        print('nmb_gen : ',param)
    print('\n\n')
    liste_soluces.append(minimum[:])
print('Done')

D = time.localtime()
name = 'mut_' + str_nb(D[1]) + str_nb(D[2]) + str_nb(D[3]) + str_nb(D[4]) + ".csv"
f = open(name, "w")
ch = ''
for i in liste_soluces[:]:
    for j in i:
        ch += str(j) + ','
    ch = ch[:-1] + '\n'
f.write(ch)
f.close()
