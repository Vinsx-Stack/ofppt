######################1#########################
f = open("algo/POO/Gestion du ficher/monficher.txt","r")
A = f.read()
f.close()
print(A)
print("*********")
######################2#######################
ch = "algo/POO/Gestion du ficher/monficher.txt"
f = open(ch,"r")
A = f.read()
f.close()
print(A)
########################3######################
print()

ch = "algo/POO/Gestion du ficher/monficher.txt"
f = open(ch,"r")
A = f.readlines()
f.close()
for i in A:
    print(i)


#################################################