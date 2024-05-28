from module.jde_mod import dire_bonjour, get_pi, ajouter, creer_tuple, format_print
from module.jde_class import Eleve, Notes

#autre façon d'Importer
import module.jde_mod as mod

#--------------------------------------------------------------------------------
mod.clear_terminal()


#--------------------------------------------------------------------------------
format_print("Exo Perso : Gestion des classes")
#------------------------------------------------------------------------------------------------
print("Exo 11 : Traitement de données")
exo11 = Notes()
while True:
    note = float(input("Saisissez une note entre 0 et 20 : "))
    if note < 0 or note > 20:
        # raise ValueError(f"La note doit être comprise entre 0 et 20. La note '{note}'n'a pas été ajoutée.")
        print(f"La note '{note}'n'a pas été ajoutée.")
        
        print("\n\n")
        
        print("Traitements sur les notes")
        if not exo11.notes:
            print("Aucune note n'a été ajoutée.")
            exit()
        else:
            print("Voici les notes : ")
            exo11.voir_notes()
            print("la note maximale est de : ", exo11.get_max())
            print("la note minimale est de : ", exo11.get_min())
            print("La moyenne est de : ", exo11.get_moyenne())
            exit()
    else:
        # print(f"La note '{note}' a été ajoutée.", end="\n\n")
        exo11.ajouter(note)
    



#--------------------------------------------------------------------------------
print("\n\n"); exit() 











# Test
john = Eleve("Doe", "John")
john.ajouter_note("Maths", 15)
john.ajouter_note("Français", 12)
john.ajouter_note("Histoire", 10)

print("#Voir la moyenne"); print(john.voir_moyenne()); print()

print("#Voir les notes"); john.voir_notes(); print()


print("#Supprimer une note");
john.supprimer_note("Français")

print("#Voir les notes"); john.voir_notes(); print()

print("#Ajouter une note");
john.ajouter_note("Anglais", 18)

print("#Voir les notes"); john.voir_notes(); print()

print("#Voir la moyenne"); print(john.voir_moyenne()); print()

print("#Modifier la note de math"); 
john.modifier_note("Maths", 17)
print("Voir les notes"); john.voir_notes(); print()
print("Voir la moyenne"); print(john.voir_moyenne()); print()

jane = Eleve("Doe", "Jane")
print("#Voir les notes de Jane"); jane.voir_notes(); print()
print("#Voir la moyenne de Jane"); print(jane.voir_moyenne()); print()

eleves = [john, jane]
print("#Voir les notes de tous les élèves")
for eleve in eleves:
    # print(f"\n{eleve.nom} {eleve.prenom}")
    print(eleve)
    eleve.voir_notes()
    print()


#--------------------------------------------------------------------------------


print("\n\n"); exit() 





#--------------------------------------------------------------------------------


#print("\n\n"); exit() 



#--------------------------------------------------------------------------------


mod.format_print("Exo 9 : compter les letters dans un texte")



def compter_lettres(texte: str, lettre: str) -> int:
    """


    Compte le nombre de fois que la lettre est présente dans le texte.



    Args:


        texte (str): Le texte dans lequel compter les lettres.


        lettre (str): La lettre à compter.



    Returns:


        int: Le nombre de fois que la lettre est présente dans le texte quelque soit la casse.
    """


    nb_lettres = 0


    for c in texte:


        if c.lower() == lettre.lower():


            nb_lettres += 1


    return nb_lettres



# Test


texte = "Bonjour tout le monde"


lettre = "b"


print(f"Le texte \"{texte}\" contient {compter_lettres(texte, lettre)} fois la lettre \"{lettre}\"")




# Test


print(f"Le texte \"{texte}\" contient {texte.count(lettre)} fois la lettre \"{lettre}\"")


print(f"Le texte \"{texte}\" contient {texte.upper().count(lettre.upper())} fois la lettre \"{lettre}\"")






#--------------------------------------------------------------------------------


mod.format_print("Exo 8 : Gestion des modules")



# Help


print(help(mod.dire_bonjour), end="\n--------\n\n")


print(help(mod.get_pi), end="\n--------\n\n")


print(help(mod.ajouter), end="\n--------\n\n")


print(help(mod.creer_tuple), end="\n--------\n\n")





#--------------------------------------------------------------------------------


mod.format_print("Résultat des fonctions du module jde_mod")



mod.dire_bonjour("toto", "titi")


print(mod.get_pi())


print(mod.ajouter(1, 2))


print(mod.creer_tuple(1, 2, 3))





