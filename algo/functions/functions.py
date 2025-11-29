# l'instruction return est utilisee pour terminer une fonction et renvoyer une valeur s'il n'est pas utilise retourne None
def Appreciation(Mg):
  if Mg>=10:
    app="Admis"
  else:
    app="Redouble"
  return app

# Maximum
def Maximum(A, B):
  if A>B:
    max=A
  else:
    max=B
  return max


# Factoriel
def Factoriel(a):
  fact=1
  for i in range (1,a+1):
    fact=fact*i
  return fact


# Premier
def EstPremier(a):
  for i in range(1,a):
    if a % i !=0:
      decision="Vrai"
    else:
      decision="Faux"
  return decision



# Premier 2.0
def estpremier(n):
  premier=True
  for i in range (2,n):
    if n%i==0:
      premier=False
      break
  return premier


# Les nombres premiers inferieurs a n
def afficher(n):
  print(f"les nombres premiers inferieur a {n} sont:")
  for i in range (2,n):
    if EstPremier(i):
      print(i, end=" ")
    
# Les params par defaut
# on peut specifier des valeurs par defaut qui seront utilisees si aucun argument
# n'est passe lors de l'appel de la fonction
# exemple
def produit (a,b,c=1,d=2):
  p=a*b*c*d
  return p
print(produit(2,3))
print(produit(2,3,4))
print(produit(2,3,4,5))



def tableau(T=[]):
  max=T[0]
  n=len(T)
  for i in range (1,n):
    if T[i]>max:
      max=T[i]
  return max
# exemple T=[12,10,25,5]
m=max([12,10,25,5])
print(f"Le plus grand element: {m}")
