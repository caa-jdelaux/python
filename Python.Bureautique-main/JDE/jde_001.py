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
print("var_int:", var_int + 1)

print()
print("#Opérateurs booléens")
# Opérateurs booléens
print("Opé ET:", True and True)
print("Opé OU:", True or False)
print("Opé NEGATION:", not True)
