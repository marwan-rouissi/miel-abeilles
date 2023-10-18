# Le miel et les abeilles
![image](https://github.com/marwan-rouissi/miel-abeilles/assets/115158061/9453ca92-7593-4f83-a3c8-884148ff5f60)


Ce projet implémente un algorithme génétique pour résoudre le problème du voyageur de commerce (TSP) en utilisant une métaphore de colonie d'abeilles. L'algorithme génétique est une approche heuristique basée sur l'évolution biologique qui cherche à trouver une solution optimale en combinant et en évoluant des solutions candidates.

Le problème du voyageur de commerce consiste à trouver le chemin le plus court qui permet de visiter un ensemble de villes une seule fois et de revenir à la ville de départ. Il s'agit d'un problème NP-complet, ce qui signifie qu'il n'existe pas d'algorithme polynomial pour résoudre le problème de manière exacte pour des instances de grande taille. L'algorithme génétique offre une approche efficace pour trouver des solutions approximatives de haute qualité.

## Structure du projet

Le projet est composé de deux fichiers principaux :

- `beehive.py` : Ce fichier contient la définition des classes `Hive` et `Bee`. La classe `Hive` représente une colonie d'abeilles et la classe `Bee` représente une abeille individuelle. Ces classes contiennent les méthodes nécessaires pour exécuter l'algorithme génétique.

- `main.py` : Ce fichier est utilisé pour exécuter l'algorithme génétique en utilisant les classes définies dans `beehive.py`. Il lit les positions des fleurs à partir d'un fichier CSV, crée une instance de la classe `Hive` et exécute l'algorithme génétique pour un nombre spécifié de générations.
  
- `app.py` : Ce fichier permet d'éxecuter le programme depuis une interface graphique Tkinter, invitant l'utilisateur à renseigner un fichier CSV contenant les positions des fleurs, ainsi que le nombre de génération à travers lequel on souhaite itérer.

## Instructions

Pour exécuter le programme, suivez ces étapes :

1. Assurez-vous d'avoir Python 3 installé sur votre machine.

2. Installez les modules nécessaires en exécutant la commande suivante :

```
pip install -r requirements.txt
```

3. Placez le fichier CSV contenant les positions des fleurs dans le même répertoire que les fichiers `beehive.py` et `main.py`.

4. Ouvrez le fichier `main.py` dans un éditeur de texte et modifiez les paramètres de l'algorithme génétique si nécessaire. Par exemple, vous pouvez ajuster le nombre de générations, la taille de la population ou la fréquence de mutation.

5. Exécutez le fichier `main.py` avec la commande suivante :

```
python main.py
```

6. Le programme exécutera l'algorithme génétique pour le nombre spécifié de générations et affichera les visualisations des résultats.

## Fonctionnement de l'algorithme génétique

L'algorithme génétique utilisé dans ce projet suit les étapes classiques d'un algorithme génétique :

1. **Initialisation** : Une population initiale d'individus (abeilles) est générée. Chaque abeille représente une solution candidate au problème TSP, c'est-à-dire un chemin qui visite toutes les villes une seule fois.

2. **Évaluation** : Chaque abeille est évaluée en fonction de sa fitness, qui mesure la qualité de sa solution. Dans le cas du TSP, la fitness peut être définie comme l'inverse de la longueur totale du chemin parcouru par l'abeille.

3. **Sélection** : Les abeilles les plus performantes sont sélectionnées pour survivre à la génération suivante, tandis que les moins performantes sont éliminées. La sélection est basée sur la fitness des abeilles.

4. **Croisement** : Les abeilles sélectionnées sont croisées entre elles pour créer une nouvelle génération d'abeilles. Le croisement se fait en échangeant des parties du chemin entre deux abeilles parentes pour créer des descendants avec des caractéristiques mixtes.

5. **Mutation** : Pour introduire de la diversité génétique, certaines abeilles subissent une mutation aléatoire. La mutation consiste à modifier légèrement le chemin d'une abeille en inversant certains segments ou en permutant certaines positions de fleurs.

6. **Répétition** : Les étapes d'évaluation, de sélection, de croisement et de mutation sont répétées pour un certain nombre de générations afin d'améliorer progressivement les solutions candidates.

7. **Terminaison** : L'algorithme s'arrête après un nombre fixe de générations ou lorsque certains critères d'arrêt sont atteints, tels qu'une amélioration négligeable de la fitness ou un temps d'exécution maximal.

## Visualisation des résultats après 1000 générations:
### Parcours de la meilleure abeille:
![image](https://github.com/marwan-rouissi/miel-abeilles/assets/115158061/f6ad478d-67c1-4688-89c7-46a2ff9665e0)
### Représentation de la fitness des meilleures au fil des générations:
![image](https://github.com/marwan-rouissi/miel-abeilles/assets/115158061/846aa8bf-9d0b-4fe1-85c1-274187b5f6d2)
### Représentation de la moyenne de la fitness de chaque génération:
![image](https://github.com/marwan-rouissi/miel-abeilles/assets/115158061/7c9a40ce-1d4f-4f39-8a26-aa82bf93a36f)



## Axes d'amélioration

Voici quelques axes d'amélioration possibles pour le projet :

1. **Optimisation de la performance** : L'algorithme génétique peut être intensif en termes de calculs, surtout lorsque le nombre de générations et la taille de la population sont élevés. L'optimisation des opérations critiques et l'utilisation de bibliothèques de calcul parallèle peuvent améliorer les performances.

2. **Paramètres ajustables** : Rendre les paramètres de l'algorithme génétique ajustables permettrait aux utilisateurs d'expérimenter différentes configurations et d'adapter l'algorithme à des problèmes spécifiques.

3. **Méthodes de sélection avancées** : L'utilisation de méthodes plus avancées de sélection, telles que la sélection par tournoi ou la sélection par rang, peut améliorer l'exploration de l'espace des solutions et accélérer la convergence vers des solutions optimales.
Dans notre cas, il s'agit d'une sélection par fitness de manière à mieux simuler et représenter l'idée de séléction naturelle.

4. **Méthodes de croisement et de mutation améliorées** : L'exploration de méthodes plus avancées de croisement et de mutation, telles que le croisement à deux points ou la mutation non uniforme, peut améliorer la diversité génétique et accélérer la convergence vers des solutions optimales.

5. **Validation des résultats** : L'ajout de métriques d'évaluation pour mesurer la qualité des solutions trouvées par l'algorithme génétique permettrait une comparaison avec d'autres approches ou des solutions optimales connues pour le problème du TSP.

6. **Interface utilisateur conviviale** : Développer une interface utilisateur conviviale où les utilisateurs peuvent charger facilement leurs propres fichiers CSV contenant les positions des fleurs, ajuster les paramètres et visualiser les résultats faciliterait l'utilisation du programme. (voir le fichier `app.py`)

7. **Tests unitaires et validation** : Ajouter des tests unitaires pour vérifier le bon fonctionnement des différentes parties du code et valider les résultats produits par l'algorithme génétique.

## Conclusion

Ce projet fournit une implémentation d'un algorithme génétique pour résoudre le problème du voyageur de commerce en utilisant une métaphore de colonie d'abeilles. En suivant les instructions fournies, vous pouvez exécuter l'algorithme sur vos propres instances du problème TSP et obtenir des solutions approximatives de haute qualité. Les axes d'amélioration suggérés vous permettront d'explorer davantage ce domaine passionnant et d'améliorer les performances et les fonctionnalités de l'algorithme génétique.
