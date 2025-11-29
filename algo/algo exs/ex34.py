#un programme qui affiche une serie d'entiers de 1 a 10 
#pour en algo = for en python
for x in range(1,11):
  print(x, end=" ")
#affiche une serie d'entiers de 1 a 10 dans le sens inverse
print()
for x in range(10,0,-1):
  print(x, end=" ")
#les entiers pairs entre 1 et 20
print()
for x in range(2,21,2):
  print(x, end=" ")
#les entiers pairs entre deux entiers donnes par l'utilisateur
print()
a=int(input("taper le nombre de depart:"))
b=int(input("taper le nombre d'arrive:"))
for x in range(a,b+1):
  if x%2==0:print(x, end=" ")
#la moyenne de classe a partir de la moyenne generale de tous les stagiaires
print()
n=int(input("taper le nombre de stagiaire:"))
som=0
for i in range(1,n+1):
  mg=float(input(f"taper la moyenne du stagiaire {i}:"))
  som +=mg
mc=round(som/n,2)
print(f"la moyenne du groupe est {mc}")

