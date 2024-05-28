#--------------------------------------------------------------------------------
print("\n# Gestion des listes : modifiables et doublons possibles") 
print(dir(list))

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
print("Nombre de 4:", ma_liste.count(4))
ma_liste.remove(4)
print("Ma liste:", ma_liste)
ma_liste.extend([5, 6, 7])
print("Ma liste:", ma_liste)
ma_liste.pop()
print("Ma liste:", ma_liste)
ma_liste.reverse()
print("Ma liste:", ma_liste)

print("Ma liste index 2:", ma_liste[2])
ma_liste[2]= 8
print("Ma liste index 2:", ma_liste[2])

while ma_liste:
    print(ma_liste.pop())

#--------------------------------------------------------------------------------
print("\n# Gestion des sets : non modifiables et sans doublons")
print(dir(set))

mon_set = {"F", "B", 2, "E"}
print("Mon set:", mon_set)

mon_set.update([5, 6, 7])
print("Mon set after update [5,6,7]:", end="\t"); mon_set.update([5, 6, 7]); print(mon_set)

print("Mon set after add 4:", end="\t"); mon_set.add(4); print(mon_set)

print("Mon set after add 4:", end="\t"); mon_set.add(4); print(mon_set)

print("Mon set after remove(4):", end="\t"); mon_set.remove(4); print(mon_set)

print("Mon set after pop:", end="\t"); mon_set.pop(); print(mon_set)

print("Mon set after discard(4):", end="\t"); mon_set.discard(4); print(mon_set)

print("Mon set if 5 in mon_set:", end="\t"); print(5 in mon_set)

print("Mon set after clear:", end="\t"); mon_set.clear(); print(mon_set)


#--------------------------------------------------------------------------------
print("\n# le tuple : non modiable")
print(dir(tuple))

mon_tuple = (1, 2, 3)
print("Mon tuple:", mon_tuple)
print("Mon tuple index 0:", mon_tuple[0])
mon_tuple = mon_tuple + (4, 5, 6)
print("Mon tuple:", mon_tuple)
var1, var2, var3, var4, var5, var6 = mon_tuple
print("var1:", var1)
for i in mon_tuple:
    print(i)

#--------------------------------------------------------------------------------
print("\n# le dictionnaire : clé/valeur modifiables et sans doublons de clé")
print(dir(dict))

mon_dict = {"nom": "DUPUY", "prenom": "Jérémy", "age": 40}
print("Mon dictionnaire values:", mon_dict.values())
print("Mon dictionnaire keys:", mon_dict.keys())
print("Mon dictionnaire items:", mon_dict.items())

for cle, valeur in mon_dict.items():
    print(f"{cle} -> {valeur}")
print()

mon_tuple = tuple(mon_dict.items())
print("Mon tuple:", mon_tuple)
for cle, valeur in mon_tuple:
    print(f"{cle} -> {valeur}")
print()

for mon_tuple in mon_dict.items():
    (cle, valeur) = mon_tuple
    print(f"{cle} -> {valeur}")
print()

print("Mon dictionnaire:", mon_dict)

print("Nom:", mon_dict["nom"])


print("Mon dictionnaire after modify age:", end="\t"); mon_dict["age"] = 41; print(mon_dict)


print("Mon dictionnaire after modify ville:", end="\t"); mon_dict["ville"] = "Toulouse"; print(mon_dict)

print("Mon dictionnaire after pop ville:", end="\t"); mon_dict.pop("ville"); print(mon_dict)

print("Mon dictionnaire after modify ville:", end="\t"); mon_dict["ville"] = "Marseille"; print(mon_dict)

print("Mon dictionnaire after popitem:", end="\t"); mon_dict.popitem(); print(mon_dict)

print("Ville:", mon_dict.get("ville", "Ville inconnue"))


print("Mon dictionnaire after modify ville:", end="\t"); mon_dict["ville"] = "Paris"; print(mon_dict)
print("Ville:", mon_dict.get("ville", "Ville inconnue"))


print("Mon dictionnaire after clear:", end="\t"); mon_dict.clear(); print(mon_dict)


