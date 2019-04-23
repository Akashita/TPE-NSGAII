from single import *
import time
import inspyred
import matplotlib.pyplot as plt

problem = inspyred.benchmarks.Ackley()

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
parameters = [1000, 40, 0.5, 0.5]
liste_soluces = []

#On fait varier crossover
for cross in range(0, 100, 10):
    parameters[2] = cross / 100
    print('crossover : ', cross,'\n\n')
    minimum = [] #Liste des meilleures solutions
    pas = 10
    max = 1000

    for param in range(0 , max , pas):
        parameters[1] = param
        final_pop = resolve_single(problem, parameters)
        liste = [Z.fitness for Z in final_pop]
        minimum.append( round( min(liste) , 3))
        print('nmb_gen : ',param)

    print('\n\n')
    liste_soluces.append(minimum)
print('Done')

D = time.localtime()
name = str(D[0]) + str_nb(D[1]) + str_nb(D[2]) + str_nb(D[3]) + str_nb(D[4]) + ".csv"
f = open(name, "w")
ch = ''
for i in liste_soluces:
    for j in i:
        ch += str(j) + ','
    ch = ch[:-1] + '\n'
f.write(ch)
f.close()

#print(liste)

#print(final_pop)
#print(min(liste),max(liste),sep='   ')
