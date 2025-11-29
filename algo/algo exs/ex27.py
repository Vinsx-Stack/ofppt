#une serie d'entiers pairs entre deux entiers saisi par l'utilisateur
print()
a=int(input("taper le nombre de depart:"))
b=int(input("taper le nombre d'arrive:"))
i=a
while i<b:
  if i%2==0:
    print(i, end=" ")
  i +=1