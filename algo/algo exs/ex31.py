#ce programme permet de calculer et d'afficher le factoriel d'un nombre entier
x=int(input("taper un nombre:"))
y=1
z=1
while z<=x:
  y *=z
  z +=1
  print(f"le factoriel est {y}")