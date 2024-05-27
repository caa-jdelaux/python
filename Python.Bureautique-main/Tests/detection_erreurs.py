#importations
import pandas as pd 
from functools import partial   

#initialisation des variables
chemin_fichier = "eleves_erreurs.csv"
bad_lines_fichier = "erreurs.csv"

def write_bad_line(line, fp, sep=','):
    fp.write(sep.join(line) + '\n')
    return None  # return None to skip the line while processing

#récupération des dataframes
with open("bad_lines_fichier.csv", 'a', encoding='latin-1') as bad_lines_fp:
    df = pd.read_csv(chemin_fichier, encoding='latin1',
                     engine='python',
                     dtype={'id': 'int', 'prenom': 'string', 'nom': 'string', 'sexe': 'string', 'classe': 'int'},
                     parse_dates=['date_naissance'],
                     on_bad_lines=partial(write_bad_line, sep=',', fp=bad_lines_fp))
    print(df)
