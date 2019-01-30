from single import *
from multi import *
import numpy as np

import inspyred
from inspyred import ec
from inspyred.benchmarks import Benchmark

from tkinter import *

#------------------------------------------------------------
#     Functions
#------------------------------------------------------------

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




#------------------------------------------------------------
#     Initialisation variables (Default var)
#------------------------------------------------------------
pop_size = 200
nmb_gen = 40
p_crossover = 0.5
p_mutation = 0.5

affichage = True
dimension = 2

# Choose the range of the variation (By default. Indeed, the variation is specified for each problem (see below))
list_pop_size = [x for x in range(2,100,10)]
list_nmb_gen = [x for x in range(5,100,5)]
list_p_crossover = [x/10 for x in range(1,11)]
list_p_mutation = [x/10 for x in range(1,11)]


#------------------------------------------------------------
#     Interaction with the user to choose it's preferences
#------------------------------------------------------------

problem_type = input("0 -> Multi-objective | 1 -> Single-objective : ")
if problem_type == "0": #Multi-objective
    liste_problemes = ['SCH','FON','kursawe','DTLZ1','DTLZ2','DTLZ3','DTLZ4','DTLZ5','DTLZ6','DTLZ7']
    print("\n\nWhat problem do you want ? :")
    entree = -1
    while entree < 0 or entree > len(liste_problemes):
        for i in range(len(liste_problemes)):
            print(' - ',i,' : ',liste_problemes[i])
        entree = int(input(''))
    if entree == 0:
        problem = SCH()

    elif entree == 1:
        problem = FON(2)

    elif entree == 2:
        problem = inspyred.benchmarks.Kursawe()

    elif entree == 3:
        problem = inspyred.benchmarks.DTLZ1(dimensions=2, objectives=2)

    elif entree == 4:
        problem = inspyred.benchmarks.DTLZ2()

    elif entree == 5:
        problem = inspyred.benchmarks.DTLZ3()

    elif entree == 6:
        problem = inspyred.benchmarks.DTLZ4()

    elif entree == 7:
        problem = inspyred.benchmarks.DTLZ5()

    elif entree == 8:
        problem = inspyred.benchmarks.DTLZ6()

    elif entree == 9:
        problem = inspyred.benchmarks.DTLZ7(dimensions=3, objectives=3)
        dimension = 3


elif problem_type == "1": #Single-objective
    liste_problemes = ['Ackley','Griewank','Rosenbrock','Schwefel','Sphere']
    print("\n\nWhat problem do you want ? :")
    entree = -1

    while entree < 0 or entree > len(liste_problemes):
        for i in range(len(liste_problemes)):
            print(' - ',i,' : ',liste_problemes[i])
        entree = int(input(''))
    if entree == 0:
        problem = inspyred.benchmarks.Ackley()
        X,Y = np.mgrid[-5:5:0.25, -5:5:0.25]
        Z = (-20) * np.exp((-0.2) * np.sqrt(0.5*((X**2)+(Y**2)))) - np.exp(0.5*(np.cos(2*np.pi*X) + np.cos(2*np.pi*Y))) + np.exp(1) + 20
        list_pop_size = [x for x in range(2,100,10)]
        list_nmb_gen = [x for x in range(1,10000,500)]
        list_p_crossover = [x/10 for x in range(1,11)]
        list_p_mutation = [x/10 for x in range(1,11)]

    elif entree == 1:
        problem = inspyred.benchmarks.Griewank()
        X,Y = None
        Z = None
        list_pop_size = [x for x in range(2,100,10)]
        list_nmb_gen = [x for x in range(1,10000,500)]
        list_p_crossover = [x/10 for x in range(1,11)]
        list_p_mutation = [x/10 for x in range(1,11)]

    elif entree == 2:
        problem = inspyred.benchmarks.Rosenbrock()
        X,Y = None
        Z = None
        list_pop_size = [x for x in range(2,100,10)]
        list_nmb_gen = [x for x in range(1,10000,500)]
        list_p_crossover = [x/10 for x in range(1,11)]
        list_p_mutation = [x/10 for x in range(1,11)]

    elif entree == 3:
        problem = inspyred.benchmarks.Schwefel()
        X,Y = None
        Z = None
        list_pop_size = [x for x in range(2,100,10)]
        list_nmb_gen = [x for x in range(1,10000,500)]
        list_p_crossover = [x/10 for x in range(1,11)]
        list_p_mutation = [x/10 for x in range(1,11)]

    elif entree == 4:
        problem = inspyred.benchmarks.Sphere()
        X,Y = None
        Z = None
        list_pop_size = [x for x in range(2,100,10)]
        list_nmb_gen = [x for x in range(1,10000,500)]
        list_p_crossover = [x/10 for x in range(1,11)]
        list_p_mutation = [x/10 for x in range(1,11)]

#------------------------------------------------------------
#     Keep display on ?
#------------------------------------------------------------

if affichage:
    print("\n\nDisplay is active, that could be annoying...")
    affichage = 'o' == input("Keep display on ? : O/n\n").lower()


#------------------------------------------------------------
#     Variation of parameters
#------------------------------------------------------------

list_param = ['pop_size','nmb_gen','p_crossover','p_mutation']
no_name = [list_pop_size , list_nmb_gen , list_p_crossover , list_p_mutation]

print("\n\nQuel parametre voulez vous faire varier :")
for i in range(len(list_param)):
    print(' - ',i,' : ',list_param[i])
entree = int(input(''))

param = list_param[entree]
list_var = no_name[entree][:]


for indice in range(len(list_var)):

    if param == 'pop_size':
        pop_size = list_var[indice]
    elif param == 'nmb_gen':
        nmb_gen = list_var[indice]
    elif param == 'p_crossover':
        p_crossover = list_var[indice]
    elif param == 'p_mutation':
        p_mutation = list_var[indice]

    parameters =[pop_size,  nmb_gen,  p_crossover,  p_mutation]

    print('\nRound ',indice,'\n',param,' = ',list_var[indice])
    if problem_type == "0":
        final_arc = resolve_multi(problem, parameters)
        coords = transform_coord(final_arc, dimension)
        hypervolume = inspyred.ec.analysis.hypervolume(coords[3], reference_point=None)
        if affichage:
            plot_multi(coords, dimension)

    elif problem_type == "1":
        final_pop = resolve_single(problem, parameters)
        if affichage:
            plot_single(final_pop, X ,Y, Z)

print("\n\n\t -- Done --\n\n")
