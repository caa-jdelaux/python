#--------------------------------------------------------------------------------
print("\n# Gestion des listes")
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


while ma_liste:
    print(ma_liste.pop())

#--------------------------------------------------------------------------------
print("\n# Gestion des sets")
print(dir(set))

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
print(dir(tuple))

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
print(dir(dict))

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
