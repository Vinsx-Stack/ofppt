a=int(input("Taper l'annee souhaitee: "))
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(a, "est une annee bissextile")
else:
    print(a, "n'est pas une annee bissextile")