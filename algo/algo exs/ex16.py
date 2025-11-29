PF=0.06
PM=0.04
Genre=input("Taper le genre (H/F): ")
anciennete=int(input("Taper l'anciennete: "))
salaire=float(input("Taper le salaire de base: "))
if (Genre == 'H' and anciennete > 20):
    Prime=salaire*PM
    print("La prime est: ", Prime)
elif (Genre == 'F' and anciennete > 18 and anciennete <= 35):
    Prime=salaire*PF
    print("La prime est: ", Prime)
else: 
    print("Vous n'avez pas droit a une prime")
    
