import os.path
import pandas as pd

COLONNE_TITRE = "Titre"
COLONNE_PRIX = "Prix"
COLONNE_QUANTITE = "Quantité"
FILE_ENCODING = "latin1"

nom_fichier = "produit.csv"
data_types = {COLONNE_TITRE: "str",
              COLONNE_PRIX: "float", COLONNE_QUANTITE: "int"}


def ajouter_produit(titre, prix, stock):
    """Ajout d'un produit dans le fichier CSV"""
    fichier_existe = os.path.exists(nom_fichier)
    df = None
    new_data_row = {COLONNE_TITRE: [titre],
                    COLONNE_PRIX: [prix], COLONNE_QUANTITE: [stock]}

    if fichier_existe:
        df = pd.read_csv(nom_fichier, dtype=data_types, encoding=FILE_ENCODING)
        df = pd.concat([df, pd.DataFrame(new_data_row)], ignore_index=True)
    else:
        df = pd.DataFrame(data=new_data_row).astype(dtype=data_types)

    if df is not None:
        df.to_csv(nom_fichier, index=False, encoding=FILE_ENCODING)


titre = input("Entrez le nom du produit: ")
prix = float(input("Entrez le prix du produit: "))
stock = int(input("Entrer le nombre de produits: "))

ajouter_produit(titre, prix, stock)
