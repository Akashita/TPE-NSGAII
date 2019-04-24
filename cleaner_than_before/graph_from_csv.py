import matplotlib.pyplot as plt


file = 'Ackley_pop_size_240022.csv'


f = open(file,'r')
lignes = f.readlines()
f.close()

if lignes[0][:4] == 'Head':
    print(lignes[0][4:])
    lignes = lignes[1:]

pas_courbes = 3
pas_values = 10

for i in range(0,len(lignes),pas_courbes):

    ligne = lignes[i][:-1]
    ligne = ligne.split(',')
    ligne = [ float(x) for x in ligne ]

    liste = []
    for j in range(0,len(ligne),pas_values):
        liste.append(ligne[j])
    plt.plot(liste)

plt.show()
