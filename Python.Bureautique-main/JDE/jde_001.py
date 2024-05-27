import math
import getpass
import random


"""
This script demonstrates basic variable initialization, manipulation, and boolean operations.

Variables:
- var_int: an integer variable initialized with the value 1
- var_float: a float variable initialized with the value 3.14
- var_string: a string variable initialized with the value "Hello"
- var_bool: a boolean variable initialized with the value True
- var_vide: a variable initialized with the value None

Prints:
- "Hello" followed by the value of the variable 'a'
- The values of the variables var_int, var_float, var_string, var_bool, and var_vide
- The result of adding 1 to var_int
- The result of boolean operations using the operators AND, OR, and NOT
"""

a = "Jérémy"
print("Hello", a)

# Init des variables
var_int = 1
var_float = 3.14
var_string = "Hello"
var_bool = True
var_vide = None

print()
print("#Affichage des variables")
# Affichage des variables
print("var_int:", var_int)
print("var_float:", var_float)
print("var_string:", var_string)
print("var_bool:", var_bool)
print("var_vide:", var_vide)

print()
print("#Manipulation des données")
# Manipulation des données
print("var_int + 1 :", var_int + 1)

print()
print("#Opérateurs booléens")
# Opérateurs booléens
print("Opé ET:", True and True)
print("Opé OU:", True or False)
print("Opé NEGATION:", not True)

print()
print("#Opérateurs relationnels")
# Opérateurs relationnels
print("opérateur sup:",4>3)
print("opérateur inf:",4<3)
print("opérateur égale:",4==3)
print("opérateur sup:",4>3)
print("opérateur non égale:",4 != 3)
print("opérateur sup ou égale:",4>=3)
print("opérateur inf ou égale:",4<=3)

print()
print("# récupération de valeurs")
# récupération de valeurs
print("#username = input('Enter your name: ')")
print("#print('Username:', username")


print()
print("# récupération du type de la variable")
# récupération du type de la variable
varInt = 1
print("varInt:", varInt, " | Type of varInt:", type(varInt))
varInt = "Test"
print("varInt:", varInt, " | Type of varInt:", type(varInt))


print("\n# Cast de valeur : conversion type variable")
# Cast de valeur : conversion type variable
var1 = "123.4"
var2 = int(float(var1))
#f : formatage d'une chaine de caractère avec des variables {}
print(f"la variable var1 est {var1} | est de type {type(var1)}")
print("var2: " + str(var2) + " | Type of var2: " + str(type(var2)))


pi = math.pi
# Affichage de la valeur de PI avec 2 chiffres après la virgule
print("Valeur de PI: {0:0.2f}".format(pi))
print(f"Valeur de PI: {pi:0.2f}")
print("Valeur de PI:", round(pi, 2))
print(f"Valeur de PI: {pi:5.2f} (avec un affiche de 5 carac)")
print("Valeur de PI:", format(pi, '0>5.2f'))
print(f"Valeur de PI: {pi:0>5.2f} (avec un affiche de 5 carac + un zéro avant le chiffre)")

print("\n# affiche le raccourci CRTL+K et CTRL+C pour commenter le code sélectionné")

#--------------------------------------------------------------------------------
print("\n# Exo 1")
# nom = input("Entrez votre nom: ")
# prenom = input("Entrez votre prénom: ")
# print(f"Bonjour {nom.upper()} {prenom.capitalize()} !")

# Récupération du nom d'utilisateur de l'ordinateur
username = getpass.getuser()
# Affichage du nom d'utilisateur en majuscules
print(f"Nom d'utilisateur: {username.upper()} ou {username.capitalize()}")
print(f"Nom d'utilisateur: {str.upper(username)} ou {str.capitalize(username)}")

# Génération de deux nombres aléatoires
# count = 1
# while count < 4:
#     num1 = input("Entrez un nombre: ")
#     if num1.isdigit():
#         break
#     else:
#         print(f"Erreur: num1 n'est pas un nombre valide. Veuillez réessayer (tentative:{count}).")
#     count += 1
#     if count == 4:
#         print("Erreur: num1 n'est pas un nombre valide. Fin de traitement.")
#         exit()
    
# Conversion de num1 en float
#num1 = float(num1)
num1 = random.uniform(1,100)
num2 = random.uniform(1,100)

# Calcul de la somme des deux nombres
sum = num1 + num2

# Affichage de la somme
print("La somme de", num1, "et", num2, "est égale à", format(sum, '0>6.2f'))

#--------------------------------------------------------------------------------
print("\n# Exo 2")
# Saisie du rayon et de la hauteur
# r = float(input("Entrez le rayon du cône : "))
# h = float(input("Entrez la hauteur du cône : "))
r = random.uniform(1,100)
h = random.uniform(1,100)

# Calcul du volume du cône
B = (math.pi * r**2)
V = (1/3) * B * h

# Affichage du volume du cône
print(f"Le volume du cône est : {format(V, '0.2f')}")

#--------------------------------------------------------------------------------
print("\n# Exo 3")
# Saisie de l'âge
# age = float(input("Entrez votre âge : "))
age= random.randint(1,40)
# Contrôle de l'âge
if age >= 18:
    bMajeure = True
    print(f"{age}:Vous êtes majeur.")
else:
    bMajeure = False
    print(f"{age}:Vous êtes mineur.")

print(f"Vous êtes majeur ? {bMajeure}")
print("Vous êtes majeur ?", "Vrai" if age >= 18 else "Faux")

#--------------------------------------------------------------------------------
print("\n# Exo 3 bis")
# Saisie de l'âge
# age = float(input("Entrez votre âge : "))
age = random.randint(1, 40)
# Contrôle de l'âge
match age:
    case _ if age >= 18:
        bMajeure = True
        print(f"{age}: Vous êtes majeur.")
    case _:
        bMajeure = False
        print(f"{age}: Vous êtes mineur.")

print(f"Vous êtes majeur ? {bMajeure}")

#--------------------------------------------------------------------------------
print("\n# Exo 4")
# Génération d'une température aléatoire entre -100 et 150
temperature = random.randint(-100, 200)

# Affichage du résultat en fonction de la température
if temperature < 0:
    sEtat = "SOLIDE"
elif temperature <= 100:
    sEtat="LIQUIDE"
else:
    sEtat ="GAZEUX"
print("T:", temperature, "Etat:", sEtat)


#--------------------------------------------------------------------------------
print("\n# Gestion des conditions")
random_boolean = bool(random.getrandbits(1))
print("Random Boolean:", random_boolean)
etat = "solide" if random_boolean else "liquide"
print("Etat:", etat)

print("\n# Boucle for")
for i in range(1, 6):
    print("Boucle for:",i)

print("\n# Boucle while")
count = 1
while count <= 5:
    print("Boucle while:",count)
    count += 1
    
#--------------------------------------------------------------------------------
print("\n# Gestion des listes")
liste_vide = []
ma_liste = ["B", "A", "C"]
print("Liste vide:", liste_vide)
print("Ma liste:", ma_liste)
ma_liste.sort()
print("Ma liste:", ma_liste)
ma_liste.append(4)
print("Ma liste:", ma_liste)
ma_liste.append(4)
print("Ma liste:", ma_liste)
ma_liste.remove(4)
print("Ma liste:", ma_liste)
ma_liste.extend([5, 6, 7])
print("Ma liste:", ma_liste)
ma_liste.pop()
print("Ma liste:", ma_liste)
ma_liste.reverse()
print("Ma liste:", ma_liste)

while ma_liste:
    print(ma_liste.pop())

#--------------------------------------------------------------------------------
print("\n# Gestion des sets")
mon_set = {1, 2, 3}
print("Mon set:", mon_set)
mon_set.update([5, 6, 7])
print("Mon set:", mon_set)
mon_set.add(4)
print("Mon set:", mon_set)
mon_set.add(4)
print("Mon set:", mon_set)
mon_set.remove(4)
print("Mon set:", mon_set)

mon_set.pop()
print("Mon set:", mon_set)


#--------------------------------------------------------------------------------
print("\n# le tuple")
mon_tuple = (1, 2, 3)
print("Mon tuple:", mon_tuple)
print("Mon tuple:", mon_tuple[0])
mon_tuple = mon_tuple + (4, 5, 6)
print("Mon tuple:", mon_tuple)
var1, var2, var3, var4, var5, var6 = mon_tuple
print("var1:", var1)
for i in mon_tuple:
    print(i)

#--------------------------------------------------------------------------------
print("\n# le dictionnaire")
mon_dict = {"nom": "DUPUY", "prenom": "Jérémy", "age": 40}
print("Mon dictionnaire:", mon_dict.values())
print("Mon dictionnaire:", mon_dict.keys())
print("Mon dictionnaire:", mon_dict.items())

for cle, valeur in mon_dict.items():
    print(f"{cle} -> {valeur}")

print("Mon dictionnaire:", mon_dict)
print("Nom:", mon_dict["nom"])
mon_dict["age"] = 41
print("Mon dictionnaire:", mon_dict)
mon_dict["ville"] = "Toulouse"
print("Mon dictionnaire:", mon_dict)
mon_dict.pop("ville")
print("Mon dictionnaire:", mon_dict)
mon_dict["ville"] = "Marseille"
print("Mon dictionnaire:", mon_dict)
mon_dict.popitem()
print("Mon dictionnaire:", mon_dict)
print("Ville:", mon_dict.get("ville", "Ville inconnue"))
mon_dict["ville"] = "Paris"
print("Mon dictionnaire:", mon_dict)
print("Ville:", mon_dict.get("ville", "Ville inconnue"))
mon_dict.clear()
print("Mon dictionnaire:", mon_dict)


#--------------------------------------------------------------------------------
print("\n# Exo 5")
# Exo 5
# Affichage de la table de multiplication de 1 à 10
nbPadding = 5
n = 10 #random.randint(1, 10)
print("n:", n)

#Entete de la table
for y in range(1, 11):
    print(f"{1*y:{nbPadding}}", end="")

print()
#Ligne de séparation
print("-" * (nbPadding * 10))

#Calcul de la table
for x in range(1, n+1):
    for y in range(1, 11):
        print(f"{x*y:{nbPadding}}", end="")
    print()

#--------------------------------------------------------------------------------
print("\n# Exo 6")
# Exo 6
epaisseurPaper = 0.1
epaisseurCible = 400 * 1000  # Conversion de mètres en millimètres
nbPliage = 0
# calcul du nombre de pliage pour atteindre 400 m
while epaisseurPaper < epaisseurCible:
    epaisseurPaper *=  2
    nbPliage += 1
#nbPliage = math.ceil(math.log(epaisseurCible / epaisseurPaper, 2))
print("Nombre de pliages nécessaires:", nbPliage)

#--------------------------------------------------------------------------------
print("\n# Exo 7")
# Exo 7
# Initialisation des variables
population = 1000
tauxCroissance = 0.02
populationCible = 2000
print("Population:", population)
print("Taux de croissance:", tauxCroissance * 100, "%")
print("Population à atteindre:", populationCible)
annee = 0
# Calcul de la population
while population < populationCible:
    population = population + (population * tauxCroissance)
    annee += 1
print(f"la population {population} est atteinte en {annee} ans")


#--------------------------------------------------------------------------------
print("\n# Exo 8")
# Exo 8
# Initialisation des variables
nom = "Jeremy"
prenom = "DUPUY"

# fonction pour construire le nom complet
def afficherNom(n, p):
    res = f"Nom complet: {n} {p}"
    return res

# Affichage du nom complet
print(afficherNom(nom, prenom))