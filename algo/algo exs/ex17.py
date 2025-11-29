a=float(input("Taper un nombre: "))
b=float(input("Taper un autre nombre: "))
if a != 0:
    x = -b / a
    print("La solution de l'equation est: ", x)
else:
    if b == 0:
        print("L'equation admet une toutes les solutions")
    else:
        print("L'equation n'admet pas de solution")