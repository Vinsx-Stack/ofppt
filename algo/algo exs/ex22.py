n=int(input("saisissez le nombre de photocopie:"))

if n<=10:
  n=n*0.30 
  print("le prix est:", n," dhs")
elif n<=30:
  n=n*0.25
  print("le prix est:", n," dhs")
else:
  n=n*0.20
  print("le prix est", n," dhs")
