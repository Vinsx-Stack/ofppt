for i in range(5):
  for j in range(i+1,5):
     print(i+j, end=" ")
  print()
mylist=['Python','PHP','Java','Algorithmique','HTML','React']
print(mylist)
n=len(mylist)
print(n)
mylist.insert(2,"Javascript")
mylist.remove("Java")
print(mylist)
mylist.append('Laravel')
print(mylist)
a=input("Saisissez un langage: ")
for i in mylist:
    if a==i:
      mylist.remove(a)
    else:
       print("Langage introuvable")
print(mylist)
L0=mylist[2:5]
print(L0)
L1=mylist[2:2]
print(L1)
L2=mylist[2:]
print(L2)
L3=mylist[::2]
print(L3)
L4=mylist[::-2]
print(L4)



  