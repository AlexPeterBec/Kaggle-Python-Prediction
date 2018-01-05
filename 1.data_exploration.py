import pandas as pd
# pd.options.mode.chained_assignment = None

trainSet = pd.read_csv("train.csv")
testSet = pd.read_csv("test.csv")

# Affichage de la premiere ligne
#print(trainSet.head(n=1))
#print(trainSet.describe())
print(trainSet.shape) # Nombre de ligne, variables

print("\nDecompte des survivants dans TrainSet - En nombre et en proportions")
# trainSet["Survived"] Selectionne uniquement la colonne Survived
print(trainSet["Survived"].value_counts())
print(trainSet["Survived"].value_counts(normalize=True))

print("Influence du Sexe passager :")
print("\n Restriction sur les passagers masculins :")
print(trainSet["Survived"][trainSet["Sex"] == "male"].value_counts())
print(trainSet["Survived"][trainSet["Sex"] == "male"].value_counts(normalize=True))
# Pour les hommes : 81% // 19% survecu
print("Restriction sur les passagers feminins :")
print(trainSet["Survived"][trainSet["Sex"] == "female"].value_counts())
print(trainSet["Survived"][trainSet["Sex"] == "female"].value_counts(normalize=True))
# Pour les femmes : 26% // 74% survecu

print("\n Influence de l'age :")
# Creation d'une nouvelle colonne et assignation
trainSet["Child"] = float('NaN')
trainSet["Child"][trainSet["Age"] < 18 ] = 1
trainSet["Child"][trainSet["Age"] >= 18 ] = 0
print(trainSet["Survived"][trainSet["Child"] == 1].value_counts(normalize=True))
# Pour les enfants : 46% // 53% survecu

print("\n Premiere prediction : Uniquement basé sur les passagers feminins")
# Duplication du testSet et ajout du resultat survived
test_one = testSet
test_one["Survived"] = "0"
test_one["Survived"][test_one["Sex"] == 'female'] = 1

print(test_one["Survived"])
