import matplotlib.pyplot as plt

file = 'big_test.csv'

f = open(file,'r')
lignes = f.readlines()
f.close()

pas = 1

total = []
for i in range(0,len(lignes),pas):
    ligne = lignes[i][:-1]
    ligne = ligne.split(',')
    ligne = [ float(x) for x in ligne ]
    liste = []
    for j in range(0,len(ligne),1):
        liste.append(ligne[j])
    plt.plot(liste)
plt.show()
    #total.append(liste)
