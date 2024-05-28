from lib import jde_003_lib
import os

os.system('cls' if os.name == 'nt' else 'clear')



print(help(jde_003_lib.dire_bonjour), end="\n\n")
print(help(jde_003_lib.get_pi), end="\n\n")
print(help(jde_003_lib.ajouter), end="\n\n")
print(help(jde_003_lib.creer_tuple), end="\n\n")

# Path: Python.Bureautique-main/JDE/jde_003_lib.py
jde_003_lib.dire_bonjour("toto", "titi")
print(jde_003_lib.get_pi())

print(jde_003_lib.ajouter(1, 2))

print(jde_003_lib.creer_tuple(1, 2, 3))

