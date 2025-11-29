x=int(input("Saisir un premier nombre:"))
y=int(input("Saisir un deuxieme nombre:"))
z=int(input("saisir un troisieme nombre:"))

if x>y and y>z:
  print("voici l'order croissant:", x,y,z)
elif x>z and z>y:
  print("voici l'ordre croissant:", x,z,y)
elif y>x and x>z:
  print("voici l'ordre croissant:", y,x,z)
elif y>z and z>x:
  print("voici l'ordre croissant:", y,z,x)
elif z>x and x>y:
  print("voici l'order croissant", z,x,y)
else:
  print("voici l'ordre croissant:", z,y,x)