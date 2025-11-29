a=int(input("Taper un nombre: "))
min=a
max=a
for i in range(1, 10):
  a=int(input("Taper un nombre: "))
  if a>max:
    max=a
  elif a<min:
    min=a
print("Le max est:", max)
print("Le min est:", min)
  