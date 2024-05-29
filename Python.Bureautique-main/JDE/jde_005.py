import csv

# Programme permettant à un utilisateur de sauvegarder un texte secret dans un fichier CSV
# Si le fichier n'existe pas, il est créé avec le nouveau texte secret
# l'utilisateur pourra voir le secret, modifier, quitter le programme
# le fichier sera lu et écris qu'une seule fois à l'ouverture et à la fermeture du programme

# Path: Python.Bureautique-main/JDE/jde_005.py
#-------------------------------------------------------------
# Définition des variables
file_path = 'Python.Bureautique-main/JDE/data/secret.csv'

#-------------------------------------------------------------
# Définition des fonctions

# Vérification si le fichier existe
def check_file_exists(file_path):
    try:
        with open(file_path, 'r') as file:
            return True
    except FileNotFoundError:
        return False
    
def save_secret_text(secret_text):  
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([secret_text])
    
    print("Secret text saved successfully!")

def read_secret_text():
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        secret_text = next(reader)[0]
    
    return secret_text

def create_file(file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([""])
        
    
# Vériication si le fichier existe
if check_file_exists(file_path):
    print("File exists")
else:
    print("File does not exist -> On va le créer")
    create_file(file_path)



while True:
    # Demande à l'utilisateur le choix de l'action
    print("\n\nMenu")
    print("1. Read the secret text")
    print("2. Save the secret text")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        existing_secret_text = read_secret_text()
        print("Existing secret text:", existing_secret_text)
    elif choice == "2":
        secret_text = input("Enter the secret text: ")

        try:
            existing_secret_text = read_secret_text()
            print("Existing secret text:", existing_secret_text)
        except FileNotFoundError:
            print("No existing secret text found.")

        save_secret_text(secret_text)
    elif choice == "3":
        print("Quitting the program...")
        exit()
    else:
        print("Invalid choice. Please try again.")




