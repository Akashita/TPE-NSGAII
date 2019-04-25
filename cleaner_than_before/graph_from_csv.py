import matplotlib.pyplot as plt

def graph_from_csv(file):
    f = open(file,'r')
    lignes = f.readlines()
    f.close()

    if lignes[0][:4] == 'Head':
        print(lignes[0][4:])
        lignes = lignes[1:]

        pas_courbes = 1
        pas_values = 1
        min_courbes = 0

    for i in range(min_courbes,len(lignes) - 1,pas_courbes):

        ligne = lignes[i][:-1]
        ligne = ligne.split(',')
        ligne = [ float(x) for x in ligne ]

        liste = []
        for j in range(0,len(ligne),pas_values):
            liste.append(ligne[j])
        plt.plot(liste)

    plt.legend(range(min_courbes,len(lignes),pas_courbes))
    plt.show()

graph_from_csv('Ackley_p_crossover_251532.csv')
