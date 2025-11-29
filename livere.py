class stagiaire():
    def __init__(self,code,name,note):
        self.code = code
        self.name = name 
        self.note = note 



def decision(self):
    if self.note > 10:
        de = "Admis"
        return de 
    elif self.note>=9 and self.note<10:
        de = "Rachete "
    else:
        de = "Redouble"

    return de


def afficher (self):
    print(f"{self.code}\t{self.name}\t{self.note}")


s1 = stagiaire(10,"Ahmed", 15,25)
s2 = stagiaire(10,"Ilyass", 19,25)

print("Meilleur Stagiaire : ")
if s1.note>s2.note:
    s1.afficher()
else:
    s2.afficher()

