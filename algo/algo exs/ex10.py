a=int(input("Taper le premier nombre: "))
b=int(input("Taper le deuxieme nombre: "))
if (a > 0 and b > 0) or (a < 0 and b < 0):
   c = a
   a = b
   b = c
else:
   c = a
   a = a+b
   b = a*b
print("Le nouveau premier nombre est: ", a)
print("Le nouveau deuxieme nombre est: ", b)
