TVA=0.20
prix_ht=float(input("Veuillez saisir le prix de l'article: "))
Qte=int(input("Taper la quantite recherchee: "))
montant_ht=prix_ht*Qte
montant_tva=montant_ht*TVA
montant_ttc=montant_ht+montant_tva
print("Le montant a payer: ", montant_ttc)