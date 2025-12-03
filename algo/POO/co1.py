class Stagiaire:
    def __init__(self, n, nom, f):
        self.__numero = n
        self.__nom = nom
        self.__filiere = f

    @property
    def Numero(self):
        return self.__numero

    @Numero.setter
    def Numero(self, new):
        self.__numero = new

    @property
    def Nom(self):
        return self.__nom

    @Nom.setter
    def Nom(self, new):
        self.__nom = new

    @property
    def Filiere(self):
        return self.__filiere

    @Filiere.setter
    def Filiere(self, new):
        self.__filiere = new

    def __str__(self):
        return f"{self.Numero}\t{self.Nom}\t{self.Filiere}"
    
class Etablissement:
    c=1
    def __init__(self,efp,vilie):
        self.code=Etablissement.c
        self.EFP=efp
        self.Vilie=vilie
        self.Lstg=[]
        Etablissement.c+=1
    def ajouter(self):
        saisie = "Y"
        while saisie=="Y":
            num = int(input("Taper Le Numero : "))
            nom = (input("Taper Le Nom : "))
            filier = (input("Taper La Filier : "))
            stg=Stagiaire(num,nom,filier)
            self.Lstg.append(stg)
            print("Ajouter Avec Succes")
            print("Voulez Vous Ajouter Un Autre Stagiaire ? Y/N")
            saisie=input("voulez-vous ajouter un autre stagiare ?")




    def afficher(self):
        print(f"{self.code}\t{self.EFP}\t{self.Vilie}")
        print("Listes Des Stagiaire : ")
        print("Numero \t Nom \t Filiere ")
        for s in self.Lstg:
            print(s)
        print(f"il y a {len(self.Lstg)} Stagiaire Dans Cet Etablissement")
        
        
if __name__=='__main__':
    et1=Etablissement("isfo", "Casablanca")
    et1.ajouter()
    et1.afficher()