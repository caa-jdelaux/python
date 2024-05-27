def saisir_notes():
    liste = []
    note = 0
    while note >= 0:
        note = float(input("Saisir note: "))
        if note >= 0:
            liste.append(note)
    
    return liste

liste_notes = saisir_notes()
print("Note minimale:", min(liste_notes))
print("Note maximale:", max(liste_notes))
print("Note moyenne:", sum(liste_notes) / len(liste_notes))