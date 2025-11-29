x=int(input("Taper le 1er nombre: "))
y=int(input("Taper le 2e nombre: "))
z=int(input("Taper le 3e nombre: "))
if x>y:
  if x>z:
    print("Le max est: ",x)
  else:
    print("Le max est: ",z)
elif y>z:
  print("Le max est: ",y)
else:
  print("Le max est: ",z)