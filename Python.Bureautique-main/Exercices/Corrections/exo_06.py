epaisseur_papier_mm = 0.1
epaisseur_cible_mm = 1000 * 400
nombre_de_plis = 0

while epaisseur_papier_mm <= epaisseur_cible_mm:
    epaisseur_papier_mm *= 2
    nombre_de_plis += 1

print(f"Nombre de plis nécessaires: {nombre_de_plis}")