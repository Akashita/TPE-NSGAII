
# Influence du paramétrage sur l'optimisation de fonction par algorithmes génétiques

**Gabriel Vaubaillon  
Swan Launay**

## But du programme :  
Lors du projet nous souhaitions observer l'influence des paramètres des algorithmes génétiques sur la résolution de problèmes. Nous avons alors créé ce programme qui trace l'évolution de la solution *(ou de l'hypervolume du front de pareto en multi objectif)* en fonction du nombre de génération. Le but est aussi de générer ces courbes avec des paramètres différents pour pouvoir ensuite comprendre leur influence.

## Divers :
- Nous utilisons la bibliothèque python [Inspyred](aarongarrett.github.io/inspyred/)
- La fonction **liste_fichiers** dans le fichier **moyennes.py** ne fonctionne à priori que sur linux.  
- Pour suivre l'algorithme nous utilisons une interface **pygame**, il est cependant possible de supprimer l'affichage en mettant la variable **interface** à **False** dans les fichiers **auto.py**. *(l'interface semble ne pas fonctionner sous windows)*

## Utilisation :
*Le fonctionnement est similaire que l'on soit en single objectif ou en multi objectif*

- Choisir un problème et choisir le bon programme : mono objectif -> **single_auto.py** ou  multi objectif -> **multi_auto.py**
- Choisir les valeurs par défaut des paramètres en fonction du problème choisit
- Choisir les paramètres que l'on souhaite faire varier, leurs intervalles de variation et le pas de variation. Attention les paramètres peuvent beaucoup influer sur les temps de calculs.
- Une fois les fichiers csv générés on peut observer les résultats avec les fonctions fournies dans **moyennes.py**.  
On peut afficher un seul fichier, une moyenne des fichiers, une courbe lissée, etc...
- On peut aussi résoudre les problèmes et faire varier un peu les paramètres "à la main" avec le programme **user.py**
