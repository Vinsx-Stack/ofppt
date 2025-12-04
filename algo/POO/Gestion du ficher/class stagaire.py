import csv

class Stagiaire:
    c = 1
    def __init__(self, nom, prenom, note, filiere):
        self.__code = Stagiaire.c
        self.__nom = nom
        self.__prenom = prenom
        self.__note = note
        self.__filiere = filiere
        Stagiaire.c += 1

    @property
    def code(self):
        return self.__code

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, new):
        self.__nom = new

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, new):
        self.__prenom = new

    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, new):
        self.__note = new

    @property
    def filiere(self):
        return self.__filiere
    @filiere.setter
    def filiere(self, new):
        self.__filiere = new

    def __str__(self):
        return f"{self.__code}\t{self.__nom}\t{self.__prenom}\t{self.__note}\t{self.__filiere}"


if __name__ == "__main__":
    Lstg = []
    s1 = Stagiaire("Anas", "Zaami", 16, "DEV")
    s2 = Stagiaire("Rym", "Jane", 15, "RESEAU")
    s3 = Stagiaire("Brown", "Charlie", 15, "DEV")
    s4 = Stagiaire("Johnson", "Emily", 19, "RESEAU")
    Lstg.append(s1)
    Lstg.append(s2)
    Lstg.append(s3)
    Lstg.append(s4)


    with open("stagiaires.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        
        writer.writerow(["Code", "Nom", "Prenom", "Note", "Filiere"])
        

        for stagiaire in Lstg:
            writer.writerow([
                stagiaire.code,
                stagiaire.nom,
                stagiaire.prenom,
                stagiaire.note,
                stagiaire.filiere
            ])
