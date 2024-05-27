#importations
import pandas as pd 
from functools import partial   

#initialisation des variables
chemin_fichier = "eleves_erreurs.csv"

#récupération des dataframes
df = pd.read_csv(chemin_fichier, encoding='latin1',
                     engine='python',
                     dtype={'id': 'int', 'prenom': 'string', 'nom': 'string', 'sexe': 'string', 'classe': 'int'},
                     parse_dates=['date_naissance'],
                     on_bad_lines='warn')

print(df)
