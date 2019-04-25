import matplotlib.pyplot as plt
from os import system

def moyenne(L):
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


system('ls Ackley_p_cross*.csv > tmp.moy')
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


pas_courbes = 1
pas_values = 1
min_courbes = 0

for i in range(min_courbes,len(new_liste),pas_courbes):
    ligne = [new_liste[i][j] for j in range(0, len(new_liste[i]), pas_values)]
    plt.plot(ligne)
plt.legend(range(min_courbes,len(new_liste),pas_courbes))
plt.show()







# Fin du fichier
