# Titanic : Machine Learning from disaster

Exploration du dataset Titanic et utilisation de techniques machine learning pour prédire les survivants

# Données

### Training set 
Set d'entrainement pour les modèles.
Contient les données utilisées par l'algo, mais aussi la réponse qu'on attend

### Test set
Utilisé pour évaluer la performance du code.
Contient les mêmes champs que le set d'entrainement, mais pas les réponses (ici, survivant ou non).

# Librairies

### Pandas
Utilisé pour la manipulation de tableaux de données et fichiers CSV.
Sert à explorer les datasets, observer les variables et les volumes de données.

### SciKit Learn
Librairie la plus populaire pour mettre en oeuvre du machine learning.

J'utilise ici "tree" pour construire un arbre de décision. Un arbre de décision parcours les données et choisit une combinaison de critère successifs pour séparer les données en groupes cohérents, c'est une suite de décisions/tests (exemple : pour classer des fruits, se baser d'abord sur le poids, puis sur l'aspect). 

Dans Python, on crée un DecisionTreeClassifier, puis on l'entraine avec des Features et un Resultat (numpy array). L'arbre va donc associer les groupes de features spécifiques qui amènent le plus souvent à un résultat précis. On peut alors connaitre l'importance de chaque features dans la classification finale.

