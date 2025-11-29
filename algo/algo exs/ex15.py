Moy=float(input("Taper la moyenne generale:"))
if (Moy >= 0 and Moy < 10):
    print("Redoublement")
elif (Moy >= 10 and Moy < 12):
    print("Mention Passable")
elif (Moy >= 12 and Moy < 14):
    print("Mention Assez bien")
elif (Moy >= 14 and Moy < 16):
    print("Mention Bien")
elif (Moy >= 16 and Moy <= 20):
    print("Mention Tres bien")
else:
    print("Note non valide")

