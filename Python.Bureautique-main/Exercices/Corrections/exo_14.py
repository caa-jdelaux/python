from sympy import symbols, solve

#fonction utilisée pour le calcul du prêt immobilier
def calcul_pret_immobilier(mortgage, rate, payment, nb_month):
    principal = mortgage
    for _ in range(0, nb_month):
        interest = principal * rate /12
        principal -= payment - interest
    return principal

#recherche de la mensualité pour le paiement du prêt immobilier
def mortgage_montly_payment(mensualite):
    pret = 100000
    taux = 0.03
    nb_mois = 120
    return calcul_pret_immobilier(pret, taux, mensualite, nb_mois)

mensualite = symbols('mensualite')
print("Mensualité: ", solve(mortgage_montly_payment(mensualite)))

#recheche de la capacité d'emprunt
def mortgage_capacity(pret):
    nb_mois = 12*20
    taux = 0.03
    remboursement_par_mois = 1200.0
    return calcul_pret_immobilier(pret, taux, remboursement_par_mois, nb_mois)

pret = symbols('pret')
print("Capacité d'emprunt: ", solve(mortgage_capacity(pret)))
