import csv

# Exo 12
# Date: 2021/07/22
# Author: JDE
# Description:
# Ecrire un script qui demande les informations d'un produit (libelle, prix, stock) à l'utilisateur
# et les enregistre dans un fichier CSV

# Définition du chemin du fichier CSV
path = 'Python.Bureautique-main/JDE/data/produit.csv'

# Demander les informations du produit à l'utilisateur
libelle = input("Entrez le libellé du produit : ")
prix = float(input("Entrez le prix du produit : "))
stock = int(input("Entrez le stock du produit : "))

# Créer une liste avec les informations du produit
produit = [libelle, prix, stock]

# Ouvrir le fichier CSV en mode écriture
with open(path, 'a', newline='') as file:
    writer = csv.writer(file)
    
    # Écrire les informations du produit dans le fichier CSV
    writer.writerow(produit)
    
print("Les informations du produit ont été enregistrées dans le fichier CSV.")
