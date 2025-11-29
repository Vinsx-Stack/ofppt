#ce programme permet de calculer et d'afficher la moyenne de la classe a partir de la moyenne generale de tous les stagiaires
#le nombre de stgiaire est saisi par l'utilsateur
print()
n=int(input("donner le nombre de satgiaires:"))
i=1
som=0
while i<=n:
  mg=float(input(f"taper la moyenne generale de chaque stagiaire:"))
  som +=mg
  i +=1
mc=som/n
mc=round(mc,2) #arrondit la moyenne de classe a 2 chiffre apres la virgule
print(f"la moyenne generale de la classe est: {mc}")