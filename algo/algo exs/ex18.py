a=float(input("Taper le 1er nombres: "))
b=float(input("Taper le 2eme nombres: "))
c=float(input("Taper le 3eme nombres: "))
d=b**2-(4*a*c)
if d>0:
    x1=(-b+d**0.5)/(2*a)
    x2=(-b-d**0.5)/(2*a)
    x1=round(x1,2)
    x2=round(x2,2)
    print("Les solutions de l'equation sont: ", x1, "et", x2)
elif a==0 and b==0 and c==0:
    print("les chiffres saisis sont invalides")
elif d==0:
    x =-b/(2*a)
    x=round(x,2)
    print("L'equation admet une seule solution: ", x)
else:
    print("L'equation n'admet pas de solution")