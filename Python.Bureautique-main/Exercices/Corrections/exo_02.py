import math

rayon = float(input("Entrez le rayon: "))
hauteur = float(input("Entrez la hauteur: "))
base = math.pi*rayon**2
volume = hauteur*base / 3
print(f"Le volume est de {volume}")