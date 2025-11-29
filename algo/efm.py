mondict={}
maliste=[]
stg1={"code":10,"nom":"Mohamed","filiere":"DEV","note":12.45}
stg2={"code":20,"nom":"Sara","filiere":"RES","note":18.25}
stg3={"code":30,"nom":"Ali","filiere":"DEV","note":8.25}
maliste.append(stg1); maliste.append(stg2)
maliste.append(stg3)
def afficher(): #procedure
  print("code\tnom\tfiliere\tnote")
  for stg in maliste:
    print(f"{stg['code']}\t{stg['nom']}\t{stg['filiere']}\t{stg['note']}")
def ajouter(): #procedure
  stg={}
  stg["code"]=int(input("donner le code: "))
  stg["nom"]=input("donner le nom: ")
  stg["filiere"]=input("donner la filiere: ")
  stg["note"]=float(input("donner la note: "))
  maliste.append(stg)
  print("Stagiaire ajoute avec succes.")

def rechercher(code): #fonction
    s=None
    for stg in maliste:
      if stg["code"]==code:
        s=stg
        break
    return s
def supprimer(code): #fonction
    stg=rechercher(code)
    if stg is not None:
      maliste.remove(stg)
      print("Stagiaire supprime avec succes.")
    else:
      print("Stagiaire n'existe pas.")

def display():
  L=[]
  fil=input("donner la filiere a rechercher: ")
  for stg in maliste:
    if stg["filiere"]==fil:
      L.append(stg)
  n=len(L)
  if n>0:
    som=0
    print("code\tnom\tfiliere\tnote")
    for stg in L:
      print(f"{stg['code']}\t{stg['nom']}\t{stg['filiere']}\t{stg['note']}")
      som=som+stg["note"]
      mc=som/n
      print(f"la moyenne de la classe est:{mc:.2f}")
  else:
    print("Aucun stagiaire dans cette filiere.") 

saisi=True
while saisi:
  print("*************MENU*************")
  print("1-----------Afficher les stagiaires")
  print("2-----------Afficher les stagiaires d'une filiere")
  print("3-----------Ajouter un stagiaire")
  print("4-----------Rechercher un stagiaire")
  print("5-----------Supprimer un stagiaire")
  print("6-----------Quitter")
  rep=int(input("choisir une operation:"))
  if rep==1:
    afficher()
  elif rep==2:
    display()
  elif rep==3:
    ajouter()
  elif rep==4:
    cde=int(input("donner le code a rechercher: "))
    stg=rechercher(cde)
    if stg is not None:
      print(f"code:{stg['code']}")
      print(f"nom:{stg['nom']}")
      print(f"filiere:{stg['filiere']}")
      print(f"note:{stg['note']}")
    else:
      print("Stagiaire n'existe pas.")
  elif rep==5:
    supprimer()
  else:
      saisi=False
