from single import *
from multi import *

import numpy as np
import time

import inspyred
from inspyred import ec
from inspyred.benchmarks import Benchmark

#------------------------------------------------------------
#     Functions
#------------------------------------------------------------
def input_int(ch , intervalle=[]):
    intervalle_exist = ( len(intervalle) != 0 )
    valide = False
    while not valide:
        entree = input(ch)
        if entree == '':
            print("You choose the default value")
            return 'default'

        try:
            entree = int(entree)
            if intervalle_exist:
                if entree >= intervalle[0] and entree <= intervalle[1]:
                    valide = True
                else:
                    print("We only take integers between ",intervalle[0]," and ",intervalle[1],", sorry")
            else:
                valide = True
        except:
            print("We only take integers",end = '')
            if intervalle_exist:
                print(" between ",intervalle[0]," and ",intervalle[1],", sorry",end ='')
            print('')
    return entree

def input_float(ch , intervalle=[]):
    intervalle_exist = (len(intervalle) != 0)
    valide = False
    while not valide:
        entree = input(ch)
        if entree == '':
            print("You choose the default value")
            return 'default'

        try:
            entree = float(entree)
            if intervalle_exist:
                if entree >= intervalle[0] and entree <= intervalle[1]:
                    valide = True
                else:
                    print("We only take floats between ",intervalle[0]," and ",intervalle[1],", sorry")
            else:
                valide = True
        except:
            print("We only take floats",end = '')
            if intervalle_exist:
                print(" between ",intervalle[0]," and ",intervalle[1],", sorry",end ='')
            print('')
    return entree

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

def resolve_problems(problem_type):
    time_start = time.time()
    if problem_type == "0":
        final_arc = resolve_multi(problem, parameters)
        time_end = time.time() - time_start
        print("\n --- Executing time : ", time_end, "--- \n")
        coords = transform_coord(final_arc, objective)
        hypervolume = inspyred.ec.analysis.hypervolume(coords[3], reference_point=None)
        if keep_display:
            plot_multi(coords, objective)

        return hypervolume

    elif problem_type == "1":
        final_pop = resolve_single(problem, parameters)
        time_end = time.time() - time_start
        print("\n --- Executing time : ", time_end, "--- \n")
        if keep_display:
            plot_single(final_pop, X ,Y, Z)



#------------------------------------------------------------
#     Initialisation variables (Default var)
#------------------------------------------------------------

# Choose the range of the variation (By default. Indeed, the variation is specified for each problem (see below))
list_pop_size = [x for x in range(2,100,10)]
list_nmb_gen = [x for x in range(5,100,5)]
list_p_crossover = [x/10 for x in range(1,11)]
list_p_mutation = [x/10 for x in range(1,11)]

objective = 2
go_one = True



#------------------------------------------------------------
#     Global loop
#------------------------------------------------------------
while  go_one:

    #------------------------------------------------------------
    #     Interaction with the user to choose it's preferences
    #------------------------------------------------------------
    print("Step 1 : What type of problem do you want to solve ?")
    print(" - 0 : Multi-objective")
    print(" - 1 : Single-objective")

    problem_type = ''
    while not problem_type in ['0','1']:
        problem_type = input("Choice : ")

    if problem_type == "0": #Multi-objective
        liste_problemes = ['SCH','FON','kursawe','DTLZ1','DTLZ2','DTLZ3','DTLZ4','DTLZ5','DTLZ6','DTLZ7']
        print("\n\nStep 2 : Which problem do you want ? :")

        for i in range(len(liste_problemes)):
            print(' - ',i,' : ',liste_problemes[i])
        entree = input_int('Choice : ', [0, len(liste_problemes)-1] )

        if entree == 0:
            problem = SCH()

        elif entree == 1:
            problem = FON(2)

        elif entree == 2:
            problem = inspyred.benchmarks.Kursawe(objectives=2)  #Il marche pas très bien

    #------------------------------------------------------------
    #     For DTLZx problems, the number of dimensiosn must be greater than the number of objectives


        elif entree == 3:
            problem = inspyred.benchmarks.DTLZ1(objectives=3, dimensions=3)
            objective = 3

        elif entree == 4:
            problem = inspyred.benchmarks.DTLZ2(objectives=3, dimensions=3)
            objective = 3

        elif entree == 5:
            problem = inspyred.benchmarks.DTLZ3(objectives=3, dimensions=3)
            objective = 3

        elif entree == 6:
            problem = inspyred.benchmarks.DTLZ4(objectives=3, dimensions=3)
            objective = 3

        elif entree == 7:
            problem = inspyred.benchmarks.DTLZ5(objectives=3, dimensions=3)
            objective = 3

        elif entree == 8:
            problem = inspyred.benchmarks.DTLZ6(objectives=3, dimensions=3)
            objective = 3

        elif entree == 9:
            problem = inspyred.benchmarks.DTLZ7(objectives=3, dimensions=3)
            objective = 3

    #------------------------------------------------------------

    elif problem_type == "1": #Single-objective
        liste_problemes = ['Ackley','Griewank','Rosenbrock','Schwefel','Sphere']
        print("\n\nStep 2 : Which problem do you want ? :")

        for i in range(len(liste_problemes)):
            print(' - ',i,' : ',liste_problemes[i])
        entree = input_int('Choice : ', intervalle = [0, len(liste_problemes)-1])

        if entree == 0:
            problem = inspyred.benchmarks.Ackley()
            X,Y = np.mgrid[-5:5:0.25, -5:5:0.25] #Definitions's range Ackley function
            Z = (-20) * np.exp((-0.2) * np.sqrt(0.5*((X**2)+(Y**2)))) - np.exp(0.5*(np.cos(2*np.pi*X) + np.cos(2*np.pi*Y))) + np.exp(1) + 20

            #------------------------------------------------------------
            #     Apparement le single-obj est sensible aux paramètres ce serait bien de définir des range adaptés aux problèmes et de ne plus les bouger
            #------------------------------------------------------------

            list_pop_size = [x for x in range(2,100,10)]
            list_nmb_gen = [x for x in range(1,10000,500)]
            list_p_crossover = [x/10 for x in range(1,11)]
            list_p_mutation = [x/10 for x in range(1,11)]

            # TODO: En mettre un dans chaque probleme,
            #pop_size , nmb_gen , p_crossover , p_mutation
            default_parameters = [200, 10, 0.5, 0.5]

        elif entree == 1:
            problem = inspyred.benchmarks.Griewank()
            X,Y = np.mgrid[-600:600:10, -600:600:10]
            Z = 1 + (1/4000)*((X**2)+(Y**2))-(np.cos(X/np.sqrt(1)))*(np.cos(Y/np.sqrt(2)))
            list_pop_size = [x for x in range(2,100,10)]
            list_nmb_gen = [x for x in range(1,10000,500)]
            list_p_crossover = [x/10 for x in range(1,11)]
            list_p_mutation = [x/10 for x in range(1,11)]

        elif entree == 2:
            problem = inspyred.benchmarks.Rosenbrock()
            X,Y = np.mgrid[-10:10:0.1, -10:10:0.1]
            Z = 100*(Y - X**2)**2 + (1 - X)**2
            list_pop_size = [x for x in range(2,100,10)]
            list_nmb_gen = [x for x in range(1,10000,500)]
            list_p_crossover = [x/10 for x in range(1,11)]
            list_p_mutation = [x/10 for x in range(1,11)]

        elif entree == 3:
            problem = inspyred.benchmarks.Schwefel()
            X,Y = np.mgrid[-512:512:1, -512:512:1]
            Z = 418.982887*2 + (-X*np.sin(np.sqrt(np.abs(X)))) + (-Y*np.sin(np.sqrt(np.abs(Y))))
            list_pop_size = [x for x in range(2,100,10)]
            list_nmb_gen = [x for x in range(1,10000,500)]
            list_p_crossover = [x/10 for x in range(1,11)]
            list_p_mutation = [x/10 for x in range(1,11)]

        elif entree == 4:
            problem = inspyred.benchmarks.Sphere()
            X,Y = np.mgrid[-10:10:0.1, -10:10:0.1]
            Z = X**2 + Y**2
            list_pop_size = [x for x in range(2,100,10)]
            list_nmb_gen = [x for x in range(1,10000,500)]
            list_p_crossover = [x/10 for x in range(1,11)]
            list_p_mutation = [x/10 for x in range(1,11)]

    #------------------------------------------------------------
    #     Keep display on ?
    print("\n\nStep 3 : Display is active, that could be annoying...")
    keep_display = question("Keep display on ? : (Y/n) ",True)

    #------------------------------------------------------------


    #------------------------------------------------------------
    #     Keep variation engine ?
    variation_choix = question("\n\nStep 4 : Do you want to vary a parameter ? (y/N) ",False)
    #------------------------------------------------------------


    if variation_choix:
        #------------------------------------------------------------
        #     Variation of parameters
        #------------------------------------------------------------

        list_param = ['pop_size','nmb_gen','p_crossover','p_mutation']
        no_name = [list_pop_size , list_nmb_gen , list_p_crossover , list_p_mutation]

        print("\n\nStep 5 : Which parameter do you want to vary :")
        for i in range(len(list_param)):
            print(' - ',i,' : ',list_param[i])
        entree = input_int('Choice : ',[0,len(list_param)-1])

        param_variation = list_param[entree]
        list_var = no_name[entree][:]

        print('\n\nStep 6 : Enter values for remaining parameters')
        if param_variation != 'pop_size':
            pop_size = input_int(" - Population size : ")
        if param_variation != 'nmb_gen':
            nmb_gen = input_int(" - Generation : ")
        if param_variation != 'p_crossover':
            p_crossover = input_float(" - Crossover probabilty : ")
        if param_variation != 'p_mutation':
            p_mutation = input_float(" - Mutation probabilty : ")

        for indice in range(len(list_var)):
            if param_variation == 'pop_size':
                pop_size = list_var[indice]
            elif param_variation == 'nmb_gen':
                nmb_gen = list_var[indice]
            elif param_variation == 'p_crossover':
                p_crossover = list_var[indice]
            elif param_variation == 'p_mutation':
                p_mutation = list_var[indice]

            print('\nRound ',indice,'\n',param_variation,' = ',list_var[indice])

            parameters = []
            for i, param in enumerate([pop_size, nmb_gen, p_crossover, p_mutation]):
                if param == "default":
                    parameters.append(default_parameters[i])
                else:
                    parameters.append(param)

            print("Hypervolume :",resolve_problems(problem_type))



    else:
        #------------------------------------------------------------
        #     Define some values for problem parameters
        #------------------------------------------------------------

        print('\n\nStep 5 : Enter values for all parameters :')
        pop_size = input_int(" - Population size : ")
        nmb_gen = input_int(" - Generation : ")
        p_crossover = input_float(" - Crossover probabilty : ")
        p_mutation =input_float(" - Mutation probabilty : ")

        parameters = []
        for i, param in enumerate([pop_size, nmb_gen, p_crossover, p_mutation]):
            if param == "default":
                parameters.append(default_parameters[i])
            else:
                parameters.append(param)

        print("Hypervolume :",resolve_problems(problem_type))

    go_one = question("\n\nThe program ended properly, do you want to start it again ? (Y/n) : ",True)
    print("\n"*10)

print("\n\n\t -- Done --\n\n")
