from notes import Notes

notes = Notes()
while True:
    note = float(input("Saisir note: "))
    if note >= 0:
        notes.ajouter_note(note)
    else:
        break

print("Note minimale:", notes.min())
print("Note maximale:", notes.max())
print("Note moyenne:", notes.moyenne())