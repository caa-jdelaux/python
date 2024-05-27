NB_PADDING_CHARS = 5

print("Affichage d'une table de multiplication de 1 à N")
max_number = int(input("Saisir N: "))

# imprimer l'entête
for num in range(1, max_number + 1):
    print(f"{num:{NB_PADDING_CHARS}}", end='')

print()
# imprimer une ligne de séparation
print("-"*max_number*NB_PADDING_CHARS)

# imprimer la table de multiplication
for i in range(1, 10 + 1):
    for j in range(1, max_number + 1):
        print(f"{i*j:{NB_PADDING_CHARS}}", end='')
    print()