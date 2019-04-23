import matplotlib.pyplot as plt


file = 'p_crossover_232313.csv'


f = open(file,'r')
lignes = f.readlines()
f.close()

if lignes[0][:4] == 'Head':
    print(lignes[0][4:])
    lignes = lignes[1:]

pas = 1

for i in range(0,len(lignes),pas):

    ligne = lignes[i][:-1]
    ligne = ligne.split(',')
    ligne = [ float(x) for x in ligne ]

    liste = []
    for j in range(0,len(ligne),1):
        liste.append(ligne[j])
    plt.plot(liste)

plt.show()
