from sklearn import tree
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None

print("Importation des données :")
trainSet = pd.read_csv("train.csv")
testSet = pd.read_csv("test.csv")

print("Formattage des données :")
# Remplissage des champs manquants
trainSet["Age"] = trainSet["Age"].fillna(trainSet["Age"].median())
trainSet["Embarked"] = trainSet["Embarked"].fillna("S")
# Transformation des non numeriques
trainSet["Sex"][trainSet["Sex"] == "male"] = 0
trainSet["Sex"][trainSet["Sex"] == "female"] = 1
trainSet["Embarked"][trainSet["Embarked"] == "S"] = 0
trainSet["Embarked"][trainSet["Embarked"] == "C"] = 1
trainSet["Embarked"][trainSet["Embarked"] == "Q"] = 2
