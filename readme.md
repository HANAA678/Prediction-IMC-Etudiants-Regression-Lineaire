# Analyse et visualisation de données : étudiants en médecine

Projet de Data Analysis en Python : exploration, nettoyage et visualisation d'un jeu de données d'étudiants en médecine, suivis d'un modèle de **régression linéaire** pour prédire l'**IMC (BMI)**.

## Objectifs

- Explorer et comprendre la structure du jeu de données
- Nettoyer les données (valeurs manquantes, doublons, colonnes inutiles)
- Visualiser les principales variables (âge, genre, groupe sanguin, IMC selon le diabète)
- Construire et évaluer un modèle de régression linéaire pour prédire l'IMC

## Démarche

1. **Chargement** du fichier Excel `medical_students_dataset.xlsx`
2. **Exploration** : dimensions, types de variables, valeurs manquantes, statistiques descriptives
3. **Visualisations exploratoires** :
   - distribution des âges
   - répartition par genre
   - boxplot de l'IMC selon la présence de diabète
   - répartition des groupes sanguins
4. **Nettoyage** :
   - suppression de la colonne `Student ID` (identifiant sans intérêt pour la modélisation)
   - valeurs manquantes numériques remplacées par la **médiane**
   - valeurs manquantes catégorielles remplacées par la **modalité la plus fréquente**
   - suppression des doublons
5. **Modélisation** :
   - variable cible : `BMI`
   - variables explicatives : variables numériques du jeu de données
   - séparation train/test (80 % / 20 %, `random_state=42`)
   - modèle : `LinearRegression` (Scikit-learn)
6. **Évaluation** : MSE, RMSE, R², et graphique valeurs réelles vs valeurs prédites

## Résultats

| Métrique | Valeur |
|----------|--------|
| RMSE     | à compléter |
| R²       | à compléter |

> Les valeurs s'affichent à la fin de l'exécution du script.

## Technologies

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

## Installation et exécution

```bash

# 1. Installer les dépendances
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl

# 2. Lancer l'analyse
python analyse_etudiants_medecine.py
```

Le fichier `medical_students_dataset.xlsx` doit se trouver dans le même dossier que le script.

## Structure du projet

```
.
├── analyse_etudiants_medecine.py   # script d'analyse et de modélisation
├── medical_students_dataset.xlsx   # jeu de données
└── README.md
```


## Auteure

**Hanaa Kachoub**, élève ingénieure en Data Science et Informatique (FST Mohammedia)
[LinkedIn](https://www.linkedin.com/in/hanaa-kachoub-51758a248) · [GitHub](https://github.com/HANAA678)