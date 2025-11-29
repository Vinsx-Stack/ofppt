valid=False
while valid==False:
  note=float(input("taper une note:"))
  if 0<=note<=20:
    valid=True
    print(f"la note du stagiaire est: {note}")
#2e methode
while True: #boucle a l'infinie
  note=float(input("taper une note:"))
  if 0<=note<=20:
    break #sortir de la boucle
  print(f"la note du stagiaire est {note}")