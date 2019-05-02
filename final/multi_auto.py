from multi import *
import time
import inspyred
import matplotlib.pyplot as plt

from os import chdir

import inspyred
from inspyred import ec
from inspyred.benchmarks import Benchmark

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
        affiche('nmb_gen = '+ str(n_gen) + ' / ' + str(max_g),(0,60))
        final_pop = resolve_multi(problem, parameters)
        coords = transform_coord(final_pop, objective)
        hypervolume = inspyred.ec.analysis.hypervolume(coords[3], reference_point=(10,10,10))
        minimum.append( round( hypervolume , 4))
        affiche('temps total : ' + str(int((time.time() - first_start) // 60)) + ' minutes',(0,140))
    return minimum[:]

chdir('data') # Pour sauvegarder les fichiers au bon endroit

#On choisit le probleme pour lequel on va faire les tests :
problem = inspyred.benchmarks.DTLZ7(objectives=3, dimensions=3)
name_problem = 'DTLZ7' #(seulement pour le nom des fichiers)
objective = 3

interface = True

#On défini les paramètres par défaut :
# pop_size, nmb_gen, p_crossover, p_mutation
default_parameters = [100, 40, 0.5, 0.5]

#On définie les caractéristiques des paramètres que l'on va faire varier :
#indice : l'indice dans la liste parameters qu'il faut passer dans resolve_problem()
#proba : si le parametre est une probabilitée ou pas (on la rentre alors en %)
parametres = [{'name' : 'pop_size' , 'indice' : 0 , 'min' : 10 , 'max' : 2000 , 'pas' : 100 , 'proba' : False},
{'name' : 'p_crossover' , 'indice' : 2 , 'min' : 0 , 'max' : 100 , 'pas' : 10 , 'proba' : True},
{'name' : 'p_mutation' , 'indice' : 3 , 'min' : 0 , 'max' : 100 , 'pas' : 10 , 'proba' : True}
]

#La façon dont le nombre de génération évolue :
min_gen = 0
max_gen = 100
pas_gen = 10

if interface:
    try:
        import pygame
        #from pygame.locals import *
        pygame.init()
        police = pygame.font.Font(pygame.font.get_default_font(),17)
        couleur = (255,255,255)
        back = (0,0,0)
        fenetre = pygame.display.set_mode((450,450))
    except:
        print('Interface not supported, try install the pygame module')
        interface = False

def affiche(ch,pos):
    if interface:
        ch = '  '+ ch + '   '
        message = police.render(ch, True, couleur, back)
        fenetre.blit(message, pos)
        pygame.display.flip()
    else:
        print(ch)


#On stocke dans exec times les temps d'exécution des différents problemes
exec_times = []
nmb_files = 0
first_start = time.time()
affiche(name_problem,(0,0))

while True:

    #On fait varier chaque parametre les un à la suite des autres :
    for p in parametres:
        affiche('Variation de '+p['name'],(0,20))
        #On stocke la date (pour les fichiers)
        date = time.localtime()

        #On réinitialise les paramètres :
        parameters = default_parameters[:]
        #On initialise la liste contenant les diverses solutions :
        liste_soluces = []

        #On commence le chronomètre :
        start_time = time.time()

        for var_param in range(p['min'] , p['max'] + 1, p['pas']):

            if p['proba']:
                value = var_param / 100
                str_max = str(p['max'] / 100)
            else:
                value = var_param
                str_max = str(p['max'])

            #On fait évoluer le paramètre :
            parameters[p['indice']] = value

            affiche(p['name']+' = '+ str(value) + ' / '+ str_max,(0,40))

            #On récupère la liste des solutions optimales de chaque résolution en faisant varier
            #le nombre de génération à chaque fois :
            time_begin = time.time()
            liste_soluces.append(var_nmb_gen(parameters, min_gen, max_gen, pas_gen))
            t = time.time() - time_begin

            affiche('Temps intermédiaire : '+str(round(t,3))+' secondes',(0,80))

        #On arrete le chronomètre :
        time_exec = time.time() - start_time
        exec_times.append(time_exec)
        affiche(p['name']+ ' done in '+str(round(time_exec,3))+' secondes.',(0,100))


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
        affiche(name + ' saved',(0,120))
        nmb_files += 1
        affiche('csv files saved : '+ str(nmb_files) ,(0,160))
        print('---------------- CSV file saved ----------------\n\n')


    print("--- Done in",int(sum(exec_times)),'secondes ---')
