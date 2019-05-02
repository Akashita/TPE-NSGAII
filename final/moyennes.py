import matplotlib.pyplot as plt
from os import system,chdir

def moyenne(L):
    if len(L) == 0:
        print('liste vide dans moyenne')
        return False

    somme = 0
    for i in L:
        somme += i
    return somme / len(L)

def liste_from_csv(fichier):
    f = open(fichier, 'r')
    lignes = f.readlines()
    f.close()

    if lignes[0][:4] == 'Head':
        lignes = lignes[1:]

    liste_totale = []
    for i in range(len(lignes)):

        ligne = lignes[i][:-1]#on supprime le retour à la ligne
        ligne = ligne.split(',')
        ligne = [ float(x) for x in ligne ]

        liste = []
        for j in range(len(ligne)):
            liste.append(ligne[j])
        liste_totale.append(liste)
    return liste_totale

def moyenne_fichier(schema):
    cmd = 'ls ' + schema + ' > tmp.moy'
    system(cmd)
    f = open('tmp.moy', 'r')
    fichiers = f.readlines()
    f.close()
    system('rm tmp.moy')
    fichiers = [i[:-1] for i in fichiers]
    nmb_fichier = len(fichiers)

    donnees_fichiers = []
    for fichier in fichiers:
        donnees_fichiers.append(liste_from_csv(fichier))

    nmb_lignes = min([len(x) for x in donnees_fichiers])
    nmb_val = min( [ len(donnees_fichiers[i][0]) for i in range(nmb_fichier) ] )


    new_liste = []
    for n_ligne in range(nmb_lignes):
        new_ligne = []
        for val in range(nmb_val):
            new_ligne.append(moyenne([donnees_fichiers[i][n_ligne][val] for i in range(nmb_fichier)]))
        new_liste.append(new_ligne)

    return new_liste


def lissage_liste(L , pas = 2):
    new_liste = []
    for i in range(0, len(L), pas):
        tmp = []
        for j in range(pas):
            if i+j < len(L):
                tmp.append(L[i + j])
        new_liste.append(moyenne(tmp))
    return new_liste

def lissage_tab(tab,step = 2):
    new_tab = []
    for i in tab:
        new_tab.append(lissage_liste(i,pas=step))
    return new_tab

def graph_tableau(tab,pas_courbes =1, min_courbes=0,pas_values=1):

    for i in range(min_courbes,len(tab),pas_courbes):
        ligne = [tab[i][j] for j in range(0, len(tab[i]), pas_values)]
        plt.plot(ligne)
    plt.legend(range(min_courbes,len(tab),pas_courbes))
    plt.xlabel('Générations')
    plt.ylabel('Solutions')
    plt.show()

chdir('data')

#graph_tableau(moyenne_fichier('Ackley_p_mut*.csv'),pas_courbes = 3,min_courbes = 0,pas_values = 10)

#graph_tableau(lissage_tab(liste_from_csv('Ackley_p_crossover_251532.csv'),step=100),pas_values = 1)

graph_tableau(moyenne_fichier('DTLZ*pop*27*.csv'),pas_values = 1,min_courbes=0)
graph_tableau(lissage_tab(moyenne_fichier('DTLZ*pop*27*.csv'),step=2),pas_values = 1)



# Fin du fichier
