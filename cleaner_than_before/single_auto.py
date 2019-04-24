from single import *
import time
import inspyred
import matplotlib.pyplot as plt


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

def moyenne(L):
    somme = 0
    for i in L:
        somme += i
    return somme / len(L)

def var_nmb_gen(parameters,min_g,max_g,pas_g):
    minimum = []
    for n_gen in range(min_g , max_g , pas_g):
        parameters[1] = n_gen
        print('nmb_gen = ',n_gen)
        final_pop = resolve_single(problem, parameters)
        liste = [Z.fitness for Z in final_pop]
        minimum.append( round( min(liste) , 4))
    return minimum[:]


#On choisit le probleme pour lequel on va faire les tests :
problem = inspyred.benchmarks.Ackley()
name_problem = 'Ackley' #(seulement pour le nom des fichiers)

#On défini les paramètres par défaut :
# pop_size, nmb_gen, p_crossover, p_mutation
default_parameters = [1000, 40, 0.5, 0.5]

#On définie les caractéristiques des paramètres que l'on va faire varier :
#indice : l'indice dans la liste parameters qu'il faut passer dans resolve_problem()
#proba : si le parametre est une probabilitée ou pas (on la rentre alors en %)
parametres = [{'name' : 'pop_size' , 'indice' : 0 , 'min' : 10 , 'max' : 10000 , 'pas' : 100 , 'proba' : False},
{'name' : 'p_crossover' , 'indice' : 2 , 'min' : 0 , 'max' : 100 , 'pas' : 10 , 'proba' : True},
{'name' : 'p_mutation' , 'indice' : 3 , 'min' : 0 , 'max' : 100 , 'pas' : 10 , 'proba' : True}
]

#La façon dont le nombre de génération évolue :
min_gen = 0
max_gen = 10000
pas_gen = 10

#On stocke dans exec times les temps d'exécution des différents problemes
exec_times = []

#On fait varier chaque parametre les un à la suite des autres :
for p in parametres:
    print('-- Variation de ',p['name'],"--")
    #On stocke la date (pour les fichiers)
    date = time.localtime()

    #On réinitialise les paramètres :
    parameters = default_parameters[:]
    #On initialise la liste contenant les diverses solutions :
    liste_soluces = []

    #On commence le chronomètre :
    start_time = time.time()

    for var_param in range(p['min'] , p['max'] , p['pas']):

        if p['proba']:
            value = var_param / 100
        else:
            value = var_param

        #On fait évoluer le paramètre :
        parameters[p['indice']] = value

        print(p['name'],' : ', value , sep='', end='\n')

        #On récupère la liste des solutions optimales de chaque résolution en faisant varier
        #le nombre de génération à chaque fois :
        time_begin = time.time()
        liste_soluces.append(var_nmb_gen(parameters, min_gen, max_gen, pas_gen))
        t = time.time() - time_begin

        print('\nTemps intermédiaire :',round(t,3),'secondes \n')

    #On arrete le chronomètre :
    time_exec = time.time() - start_time
    exec_times.append(time_exec)
    print(p['name'],' done in ',round(time_exec,3),' secondes.\n',sep='')


    # Enregistrement du fichier csv :

    #On choisit le nom du fichier :
    name = name_problem + '_'+ p['name'] + '_' + str_nb(date[2]) + str_nb(date[3]) + str_nb(date[4]) + '.csv'

    #On écrit l'entête du fichier (date, temps d'exécutions, paramètres) :
    str_date = str(date[0]) +'/'+ str_nb(date[1]) +'/'+ str_nb(date[2]) +' '+ str_nb(date[3]) +':'+ str_nb(date[4]) +':'+ str_nb(date[5])
    entete = 'Head Début : ' + str_date
    entete += " , Temps d'exécution : " + str(int(time_exec)) + " secondes"
    entete += ' , Variation de ' + p['name'] + ' entre ' + str(p['min']) + ' et ' + str(p['max'])
    if p['proba']:
        entete += ' (en %)'
    entete += ' avec un pas de ' + str(p['pas'])
    entete += ', Variation de nmb_gens de '+ str(min_gen) + ' à ' + str(max_gen)

    #On écrit les données en elles mêmes :
    ch = entete + '\n'
    for i in liste_soluces[:]:
        for j in i:
            ch += str(j) + ','
        ch = ch[:-1] + '\n'

    #On enregistre le fichier :
    f = open(name, 'w')
    f.write(ch)
    f.close()
    print('---------------- CSV file saved ----------------\n\n')


print("--- Done in",int(sum(exec_times)),'secondes ---')
