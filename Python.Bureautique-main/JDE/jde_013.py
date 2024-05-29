import csv

# Exo 13
# Date: 2021/07/22
# Author: JDE
# Description:
# Programme de gestion des numéros de téléphone
# Sauvegarde des données téléphoniques dans le fichier contact.csv
# au démarrage du programme, le fichier est lu et les données sont stockées dans un dictionnaire
# a la fermeture du programme, le dictionnaire est sauvegardé dans le fichier CSV
# Lors du démarrage, le menu suivant est affiché:
# 1. voir les contacts
# 1. Ajouter un contact
# 2. Modifier un contact
# 3. Supprimer un contact
# 4. Rechercher un contact
# 5. Quitter
# Le choix 1 affiche tous les contacts
# Le Choix 2 demande le nom et le numéro de téléphone du contact à ajouter


# Définition des variables
file_path = 'Python.Bureautique-main/JDE/data/contact.csv'

# Définition des fonctions
def read_contacts():
    contacts = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                if row[0] != "" and row[1] != "":
                    name = row[0]
                    phone = row[1]
                    contacts[name] = phone
        file.close()
    return contacts

def save_contacts(contacts):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, phone in contacts.items():
            if name != "" and phone != "":
                writer.writerow([name, phone])
        file.close()

def check_file_exists(file_path):
    try:
        with open(file_path, 'r') as file:
            return True
    except FileNotFoundError:
        return False

def create_file(file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["", ""])
        file.close()

#-------------------------------------------------------------
# Vérification si le fichier existe
# Vériication si le fichier existe
if check_file_exists(file_path):
    print("File exists")
else:
    print("File does not exist -> On va le créer")
    create_file(file_path)
    
# Load contacts from file
contacts = read_contacts()

while True:
    # Your code here
    # Display menu
    print("Menu:")
    print("1. Voir les contacts")
    print("2. Ajouter un contact")
    print("3. Modifier un contact")
    print("4. Supprimer un contact")
    print("5. Rechercher un contact")
    print("6. Quitter")

    # Get user input for choice
    choice = input("Choisissez une option: ")

    # Process user choice
    if choice == "1":
        # Afficher tous les contacts
        for name, phone in contacts.items():
            print(f"Nom: {name}, Téléphone: {phone}")
            
    elif choice == "2":
        # Demander le nom et le numéro de téléphone du contact à ajouter
        name = input("Entrez le nom du contact: ")
        phone = input("Entrez le numéro de téléphone du contact: ")
        contacts[name] = phone
        
    elif choice == "3":
        # Demander le nom du contact à modifier
        name = input("Entrez le nom du contact à modifier: ")
        
        # Vérifier si le contact existe
        if name in contacts:
            # Demander le nouveau numéro de téléphone
            phone = input("Entrez le nouveau numéro de téléphone: ")
            contacts[name] = phone
        else:
            print("Le contact n'existe pas")

    elif choice == "4":
        # Demander le nom du contact à supprimer
        name = input("Entrez le nom du contact à supprimer: ")
        
        # Vérifier si le contact existe
        if name in contacts:
            del contacts[name]
        else:
            print("Le contact n'existe pas")

    elif choice == "5":
        # Demander le nom du contact à rechercher
        name = input("Entrez le nom du contact à rechercher: ")
        
        # Vérifier si le contact existe
        if name in contacts:
            print(f"Nom: {name}, Téléphone: {contacts[name]}")
        else:
            print("Le contact n'existe pas")

    elif choice == "6":
        # Quitter le while
        break
    else:
        print("Option invalide")

print("Saving contacts...")
# Save contacts to file
save_contacts(contacts)