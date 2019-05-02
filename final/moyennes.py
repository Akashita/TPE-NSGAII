
#To show the results :
import matplotlib.pyplot as plt

#We need to choose the files :
from os import system,chdir


def moyenne(L):
    """permet de réaliser la moyenne de la liste L entrée en paramètres"""

    if len(L) == 0:
        print('liste vide dans moyenne')
        return False

    somme = 0
    for i in L:
        somme += i
    return somme / len(L)


def liste_fichiers(schema):
    #On liste les fichiers correspondants au schema dans un fichier temporaire
    cmd = 'ls ' + schema + ' > I_hope_no_important_file_is_named_this_way.tmp'
    system(cmd)

    #On lit ce fichier temporaire :
    f = open('I_hope_no_important_file_is_named_this_way.tmp', 'r')
    fichiers = f.readlines()
    f.close()

    #On supprime le fichier temporaire :
    system('rm I_hope_no_important_file_is_named_this_way.tmp')

    #Lorsque l'on lit les noms des fichiers on récupère aussi un retour à la
    #ligne. On les supprime avec la ligne suivante :
    fichiers = [i[:-1] for i in fichiers]
    return fichiers[:]


def liste_from_csv(fichier):
    """cette fonction permet de générer un tableau de valeurs à partir d'un
    fichier csv"""
    #On récupère les lignes du fichier dans une liste :
    f = open(fichier, 'r')
    lignes = f.readlines()
    f.close()

    #Si la première ligne est un entete, on l'ignore
    if lignes[0][:4] == 'Head':
        lignes = lignes[1:]

    #On initialise le tableau final :
    liste_totale = []

    for i in range(len(lignes)):
        #On supprime le retour à la ligne :
        ligne = lignes[i][:-1]
        #On sépare les valeurs selon les virgules :
        ligne = ligne.split(',')
        #on transforme les chaînes de caractères en réels :
        ligne = [ float(x) for x in ligne ]
        #On ajoute la ligne dans le tableau final :
        liste_totale.append(ligne)
    return liste_totale


def moyenne_fichier(schema):
    """permet d'effectuer la courbe moyenne à partir de plusieurs fichiers
    de valeurs"""
    #On considère que l'utilisateur choisit des sets de fichiers ayant du sens
    #On ne mélange pas pop_size et p_crossover par exemple !!

    #On récupère la liste des fichiers :
    fichiers = liste_fichiers(schema)
    nmb_fichier = len(fichiers)

    #On récupère les données brutes des fichiers:
    donnees_fichiers = []
    for fichier in fichiers:
        donnees_fichiers.append(liste_from_csv(fichier))

    #On choisit le nombre de lignes et de colonnes en fonction du fichier qui
    #en a le moins :
    nmb_lignes = min([len(x) for x in donnees_fichiers])
    nmb_val = min( [ len(donnees_fichiers[i][0]) for i in range(nmb_fichier) ] )

    new_liste = []
    for n_ligne in range(nmb_lignes):
        new_ligne = []
        for val in range(nmb_val):
            #Chaque valeur deviens la moyenne des valeurs correspondantes dans
            #tous les fichiers :
            moy = moyenne([donnees_fichiers[i][n_ligne][val] for i in range(nmb_fichier)])
            new_ligne.append(moy)
        new_liste.append(new_ligne)

    return new_liste[:]


def lissage_liste(L , intervalle = 2):
    """cette fonction réduit les pics et les variations
    d'une liste en ramenant les valeurs d'un intervalle
    sur un seul point (qui prend leur valeur moyenne)"""
    new_liste = []
    for i in range(0, len(L), intervalle):

        #On récupère les valeurs de l'intervalle :
        valeurs = []
        for j in range(intervalle):
            if i+j < len(L):
                valeurs.append(L[i + j])
        #On insère la moyenne des points de l'intervalle :
        new_liste.append(moyenne(valeurs))
    return new_liste


def lissage_tab(tab,step = 2):
    """cette fonction réduit les pics et les variations
    d'un tableau de liste en ramenant les valeurs d'un intervalle
    sur un seul point (qui prend leur valeur moyenne) pour chaque liste"""
    new_tab = []
    for liste in tab:
        new_tab.append(lissage_liste(liste , intervalle=step))
    return new_tab


def graph_tableau(tab, pas_courbes =1, min_courbes=0, pas_values=1, namex='x', namey='y'):
    """cette fonction permet d'obtenir une courbe basique à partir d'un tableau
    input : tab, le tableau
            pas_courbes : permet de sauter 'pas courbes' lors de l'affichage pour être plus lisible
            min_courbes : permet de ne pas afficher les premières courbes
            pas_value : permet de ne pas afficher toutes les valeurs
            namex & namey : les noms des axes"""
    for i in range(min_courbes,len(tab),pas_courbes):
        ligne = [tab[i][j] for j in range(0, len(tab[i]), pas_values)]
        plt.plot(ligne)
    plt.legend(range(min_courbes,len(tab),pas_courbes))
    plt.xlabel(namex)
    plt.ylabel(namey)
    plt.show()

###############################################################################
### Zone de Travail :

chdir('data') # Pour aller chercher les fichiers au bon endroit


#graph_tableau(moyenne_fichier('Ackley_p_mut*.csv'),pas_courbes = 3,min_courbes = 0,pas_values = 10)
#graph_tableau(lissage_tab(liste_from_csv('Ackley_p_crossover_251532.csv'),step=100),pas_values = 1)
#graph_tableau(moyenne_fichier('Ackley*pop*.csv'),pas_values = 1,min_courbes=0)

graph_tableau(lissage_tab(moyenne_fichier('Ackley*cross*.csv'),step=100))



# Fin du fichier
###############################################################################
