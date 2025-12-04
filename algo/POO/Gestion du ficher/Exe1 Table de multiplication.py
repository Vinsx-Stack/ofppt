f = open("table.txt", "w")

f.write("\t \tTable de Multiplication \n")
f.write("x\t")

for i in range(1, 10):
    f.write(str(i) + "\t")
f.write("\n")

for i in range(1, 10):
    f.write(str(i) + "\t")
    for j in range(1, 10):
        f.write(str(i * j) + "\t")
    f.write("\n")

f.close()
print("Table de multiplication sauvegardée dans 'table.txt' avec succès.")