
# Formations :
    - VSCode - utilisation
    - Avancé Python

# Trouver les packages à ajouter :
    https://pypi.org/

# Trouver la syntaxe sur un fichier json
    https://jsonpath.com/
    
# Documentation python :
    https://docs.python.org/3/

# Entrainements
    https://www.codingame.com/


# Voir la liste des packages installé en local
    CMD> pip list
        Package            Version
        ------------------ --------
        certifi            2024.2.2
        charset-normalizer 3.3.2
        idna               3.7
        pip                24.0
        requests           2.32.2
        setuptools         65.5.0
        urllib3            2.2.1


# Astuce CMD
    https://www.malekal.com/astuces-invite-de-commande-a-connaitre/
    Par exemple pour avoir malekal.com comme prompt, saisissez :
    - prompt JDE$G
    Modifier le titre du CMD
    - title MON.
    

# Gestion des fichiers JSON
    import json

    ## On charge le contenu du fichier JSON
    with open('input.json', 'r') as f:
        data = json.load(f)
        f.close()
        
    ## Affichage du contenu
    pretty_data = json.dumps(data, indent=2)
    print(pretty_data)   

    ## Get the value of the key 'name'
    menuitem = data['menu']['popup']['menuitem'][0]['value']
    print("menuitem: ", menuitem)

# Création d'un tableau à partir de 2 listes
    data2 = {'Colonne1': [1, 2, 3, 4, 5], 'Colonne2': [10, 20, 30, 40, 50]}

# Ecriture dans un fichier csv
    with open('output3.csv', 'w') as f:
        writer = csv.writer(f)
        # ériture de l'entête
        writer.writerow(data2.keys())
        # écriture des données
        writer.writerows(zip(*data2.values()))

    ## Explication de zip
    print([*zip(*data2.values())])
    for i in zip(*data2.values()):
        print(i)
    f.close()
# Gestion du ZIP
    #Explication 
    # Exemple : Gestion du zip
    a = [1, 2, 3]
    b = ['a', 'b', 'c']
    print([*zip(a, b)])

# Définir le type des colonnes d'une table
    import pandas as pd

    # File path
    path = "./Data/eleves.csv"

    # Define data types for columns
    dtype = {
        'prenom': 'string',
        'nom': 'string',
        'sexe': 'string',
        'classe': 'int'
    }

    # Read the CSV file with specified data types
    df = pd.read_csv(path, encoding='latin1', dtype=dtype, parse_dates=['date_naissance'])
    df.info()

# Différentes types de jointure
    https://www.ionos.fr/digitalguide/hebergement/aspects-techniques/sql-join/


# Voir pytest pour les tests unitaires
    Exemple sous JDE/student
    https://datascientest.com/pytest-pourquoi-et-comment-lutiliser



# Sur les dataFrame du notebook, utilisation de plugin VSCODE
    Data Wrangler