
#Projet : Data Analysis & Visualization - Étudiants en Médecine


# Importation des bibliothèques principales
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score



#Chargement des données
df_meddata = pd.read_excel('medical_students_dataset.xlsx')

# Aperçu des premières lignes
print("Aperçu des données :")
print(df_meddata.head())

#Exploration du dataset

print("\n--- Informations générales ---")
print(f"Nombre de lignes et de colonnes : {df_meddata.shape}")
print("\nTypes de variables et non-null :")
print(df_meddata.info())

print("\n--- Valeurs manquantes par colonne ---")
print(df_meddata.isnull().sum())

print("\n--- Statistiques descriptives ---")
print(df_meddata.describe(include="all"))

#Visualisations exploratoires


sns.set(style="whitegrid")

# Distribution de l'âge
plt.figure(figsize=(8,5))
sns.histplot(df_meddata['Age'], bins=30, kde=True, color='skyblue')
plt.title("Distribution des âges")
plt.show()

# Répartition par genre
plt.figure(figsize=(6,4))
sns.countplot(x="Gender", data=df_meddata, palette="Set2")
plt.title("Répartition par genre")
plt.show()

# Boxplot BMI selon le diabète
plt.figure(figsize=(8,5))
sns.boxplot(x="Diabetes", y="BMI", data=df_meddata, palette="Set3")
plt.title("BMI selon la présence de diabète")
plt.show()

# Répartition des groupes sanguins
plt.figure(figsize=(8,5))
df_meddata['Blood Type'].value_counts().plot(kind='bar', color='lightcoral')
plt.title("Répartition des groupes sanguins")
plt.xlabel("Groupe sanguin")
plt.ylabel("Nombre d'étudiants")
plt.show()

#Nettoyage des données


# Supprimer la colonne Student ID (car il est non utile à l’analyse de plus on ne peut pas le remplacer par la médiane ou la mode)
if 'Student ID' in df_meddata.columns:
    df_meddata.drop(columns=['Student ID'], inplace=True)
    print("\nColonne 'Student ID' supprimée (identifiant inutile à la modélisation).")

# Remplacer les valeurs manquantes numériques par la médiane
num_cols = df_meddata.select_dtypes(include=["float64", "int64"]).columns
df_meddata[num_cols] = df_meddata[num_cols].fillna(df_meddata[num_cols].median())

# Remplacer les valeurs manquantes catégorielles par la modalité la plus fréquente
cat_cols = df_meddata.select_dtypes(include=["object"]).columns
for col in cat_cols:
    df_meddata[col].fillna(df_meddata[col].mode()[0], inplace=True)

# Vérification des valeurs manquantes après nettoyage
print("\nValeurs manquantes après nettoyage :")
print(df_meddata.isnull().sum())

# Suppression des doublons
duplicates = df_meddata.duplicated().sum()
print(f"\nNombre de doublons : {duplicates}")
if duplicates > 0:
    df_meddata.drop_duplicates(inplace=True)
    print("Doublons supprimés.")
print(f"Nouvelle taille du dataset : {df_meddata.shape}")


#Modélisation - Régression Linéaire
# Objectif : prédire le BMI à partir des autres variables numériques

# Définir la variable cible
y = df_meddata['BMI']

# Sélectionner uniquement les variables explicatives numériques (hors cible)
X = df_meddata.drop(columns=['BMI']).select_dtypes(include=["float64", "int64"])

# Séparation train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Création et entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Prédictions
y_pred = model.predict(X_test)

# Évaluation du modèle
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- Évaluation du modèle de régression linéaire ---")
print(f"Mean Squared Error (MSE) : {mse:.2f}")
print(f"Root Mean Squared Error (RMSE) : {np.sqrt(mse):.2f}")
print(f"Coefficient de détermination R² : {r2:.2f}")

# Visualisation : valeurs réelles vs valeurs prédites
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, color='skyblue', edgecolor='k')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', linewidth=2)
plt.xlabel("Valeurs réelles de BMI")
plt.ylabel("Valeurs prédites de BMI")
plt.title("Régression Linéaire : Valeurs réelles vs Prédictions")
plt.show()
