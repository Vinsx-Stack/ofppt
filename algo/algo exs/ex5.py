CM=5
CPC=5
CN=4
CA=3
CF=2
maths=float(input("Veuillez saisir la note de mathematiques: "))
physique=float(input("Veuillez saisir la note de physique: "))
SN=float(input("Veuillez saisir la note de sciences naturelles: "))
Arabe=float(input("Veuillez saisir la note d'arabe: "))
Francais=float(input("Veuillez saisir la note de francais: "))
MG=(maths*CM+physique*CPC+SN*CN+Arabe*CA+Francais*CF)/(CM+CPC+CN+CA+CF)
MG=round(MG,2)
print("La moyenne generale est: ", MG)

