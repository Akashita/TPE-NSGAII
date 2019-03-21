from single import *
import time
import inspyred

problem = inspyred.benchmarks.Ackley()



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


parameters = [200, 40, 0.5, 0.5]
final_pop = resolve_single(problem, parameters)
liste = [Z.fitness for Z in final_pop]


#print(final_pop)
print(min(liste),max(liste),sep='   ')
