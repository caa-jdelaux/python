import pandas as pd

# Lecture du fichier CSV
data_csv = pd.read_csv('Jupiter_Notebooks/input.csv')
# Affichage des données
print(data_csv.head())

# Affichage de l'entête
data_csv.head(0)


# Affichage d'une valeure spécifique
data_csv['Color Code'][2]


