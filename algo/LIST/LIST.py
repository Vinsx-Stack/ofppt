#comment declarer une liste vide
maliste=[]
#maliste=list()
maliste=[12,5,-11,17]
# pour ajouter un element a la liste:
# maliste.append(x)
# l'element x sera ajouter a la fin de la liste
# pour afficher le nombre d'element d'une liste:
N=len(maliste)
# pour afficher un element de la liste:
# maliste[indice]
# pour afficher le premier element:
print("le premier element: ")
print(maliste[0])
print(maliste[-N])
print("le dernier element: ")
print(maliste[N-1])
print(maliste[-1])
# parcourir les elements d'une liste:
# avec les indices
for i in range(N):
  print(maliste[i],end=" ")
print()
# avec les elements
for m in maliste:
  print(m,end=" ")
print()
# avec les indices et valeurs
for i, v in enumerate(maliste):
  print(f"{i+1}====={v}")
print()
# suppression d'un element de la liste
# nomListe.remove(element)
maliste=["anass","nadia","ilyass","taha","ayoub"]
for m in maliste:
  print(m,end=" ")
print()
nom=input("taper le nom a supprimer: ")
trouver=False
for m in maliste:
  if m==nom:
    trouver=True
    maliste.remove(nom)
    print("Suppression avec succes")
    break
if trouver==False:
  print(f"{nom} est introuvable")
print("la liste des stagiaires: ")
for m in maliste:
  print(m,end=" ")
print()
#deuxieme methode:
nom=input("taper le nom a supprimer: ")
if nom in maliste: #test l'existence de l'element dans la liste
  maliste.remove(nom)
  print("Suppression avec succes")
else:
  print(f"{nom} est introuvable")
print("la liste des stagiaires: ")
for m in maliste:
  print(m,end=" ")
print()
# afficher le nombre d'occurrence de l'element X dans la liste
A=[-3,0,4,1,0,10]
for i in A:
  print(i,end=" ")
print()
N=A.count(0)
print(f"le nombre d'occurrences de 0 est: {N}")
print()
#transferer les elements + vers la liste B et les elements - vers la liste C
A=[-5,10,20,15,-18,0,-22]
B=[]
C=[]
for i in A:
  if i<0:
    B.append(i)
  else:
    C.append(i)
print("Les elements du tableau A sont: ")
for i in A:
  print(i,end=" ")
print()
print("Les elements du tableau B sont: ")
for i in B:
  print(i, end=" ")
print()
print("Les elements du tableau C sont: ")
for i in C:
  print(i, end=" ")
print()
#decoupage d'une liste (Extraire une sous-liste a partir d'une liste)
#nomListe[debut:fin:pas]
#debut: indice de debut (inclus)
#fin: indice de fin (exclus)
#pas: valuer de pas (par defaut=1)
maliste=["anass","nadia","ilyass","taha","ayoub","aicha"]
L1=maliste[1:5:2]
print(L1)
L2=maliste[:5]
print(L2)
L3=maliste[3:]
print(L3)
L4=maliste[-3:]
print(L4)
L5=maliste[5:2] # une liste vide
print(L5)
#pour inverser les elements d'une liste:
# methode 1: nomliste.reverse()
# methode 2: L=nomliste[::-1]
L6=maliste[::-1]
print(L6)
# pour trier une liste:
# nomliste.sort() => par defaut en ordre croissant
# nomliste.sort(reverse=True) => Tri en ordre decroissant
A=[0,12,25,35,-12,-20]
print("Avant le tri:")
print(A)
A.sort() 
#A.sort(reverse=True) pour l'ordre decroissant
print("Apres le tri:")
print(A)
# pour declarer un dictionnaire vide
mondict={} #1ere facon
mondict=dict() #2e facon
# Exemple
personne={"code":int(input("taper le code: ")),
          "nom":input("taper le nom: "), 
          "specialite": input("taper la specialite: "),
          "note":float(input("taper la note: "))}
# a partir des cles
# affichage des cles:
for p in personne.keys():
  print(f"{p}===>{personne[p]}")
print()
# affichage uniquement des valeurs du dictionnaire
for v in personne.values():
  print(v)
# Affichage simultanenet les cles et les valures
for c, v in personne.items():
  print(f"{c}===={v}")  



