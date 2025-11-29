mois = int(input("Entrez le numéro du mois (1-12) : "))
annee = int(input("Entrez l'année : "))

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    bissextile = True
else:
    bissextile = False
if mois in [1, 3, 5, 7, 8, 10, 12]:
    nb_jours = 31
elif mois in [4, 6, 9, 11]:
    nb_jours = 30
elif mois == 2:
    nb_jours = 29 if bissextile else 28
else:
    print("Mois invalide !")
    exit()
print("Le mois", mois, "de l'année", annee, "a", nb_jours, "jours.")
if bissextile:
    print("L'année est bissextile.")
else:
    print("L'année n'est pas bissextile.")