# Exo 14
# Date: 2021/10/17
# Author: JDE
# Description:
# Programme qui permet :
# 1. calculer la mensualite d'un pret immobilier de 100 000 euros sur 10 ans (120 mois) avec un taux de 3%.
# 2. calculer la capacité de credit pour un prêt d'une période de 20 ans (240 mois) avec un taux de 3% et pour une capacité de remboursement de 1200 euros / mois.

# 1. Calculer la mensualite d'un pret immobilier de 100 000 euros sur 10 ans (120 mois) avec un taux de 3%.
loan_amount = 100000
loan_duration = 10 * 12  # 10 years converted to months
interest_rate = 3 / 100

monthly_interest_rate = interest_rate / 12
monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_duration)

print("Mensualite du pret immobilier: ", round(monthly_payment, 2))

# 2. Calculer la capacite de credit pour un pret d'une periode de 20 ans (240 mois) avec un taux de 3% et pour une capacite de remboursement de 1200 euros / mois.
monthly_payment_limit = 1200

loan_duration = 20 * 12  # 20 years converted to months

loan_amount = (monthly_payment_limit * (1 - (1 + monthly_interest_rate) ** -loan_duration)) / monthly_interest_rate

print("Capacite de credit: ", round(loan_amount, 2))