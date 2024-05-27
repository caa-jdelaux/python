try:
    note = float(input("Entrez note: "))
    print(note)
except ValueError as val_error:
    print("ValueError:", val_error)
except Exception as error:
    print("erreur:", error)