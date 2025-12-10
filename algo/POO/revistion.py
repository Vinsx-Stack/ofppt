class Stagiaire:
    def __init__(self, numero, name, filiere ):
        self.__numero=numero
        self.__name=name
        self.__filiere=filiere
    @property
    def Numero(self):
        return self.__numero
    @Numero.setter
    def Numero(self,new):
        self.__numero=new
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,new):
        self.__name=new
    @property
    def Filiere(self):
        return self.__filiere
    @Filiere.setter
    def Filiere(self,new):
        self.__filiere=new

    def __str__(self):
        return (f"{self.__numero}\t{self.__name}\t{self.__filiere}")
    
class Etablissment:
    compt = 1
    def __init__(self,efp, ville ):
        self.code=Etablissment.compt
        self.efp=efp
        self.ville=ville
        self.Lstg=[]
        Etablissment.compt +=1
    def ajouter(self):
        saisie = "Y"
        while saisie.upper() =="Y":
            num = int(input("Taper le numero : "))
            nom = input("Taper le nom : ")
            filiere = input("Taper la filiere : ")
            stg=Stagiaire(num,nom,filiere)
            self.Lstg.append(stg)
            print("Ajouer avec succes")
            saisie=(input("vouler-vous ajouter un autre stagiaire (Y/N) : "))

    def afficher(self):
        print(f"{self.compt}\t{self.efp}\t{self.ville}")
        print("Listes des stagiaire : ")
        print("Numero \t Nom \t Filiere")
        for s in self.Lstg:
            print(s)
        print(f"il y a {len(self.Lstg)} stagiaire ")
    def rechecher(self,num):
        for s in self.Lstg:
            if s.Numero==num:
                return s
        return None
    def supprimer(self,num):
        s = self.rechecher(num)
        if s is not None:
            rep = input("Voulez-vous vraiment supprimer ? (1=oui / 0=non) : ")
            if rep=="1":
                self.Lstg.remove(s)
                print('Suppression avec succès.')
        else:
            print("Stagiaire introuvable.")
    def main(self):
        saisie = True
        while saisie:
                print("\n************ Menu Général **************")
                print()
                print("1 - Ajouter les stagiaires")
                print("2 - Afficher tous les stagiaires")
                print("3 - Rechercher un stagiaire")
                print("4 - Supprimer un stagiaire")
                print("5 - Quitter")
                print("\n************ Menu Général **************")
                rep = int(input("Taper un choix : "))
                if rep==1:
                    self.ajouter()
                elif rep==2:
                    self.afficher()
                elif rep==3:
                    N = int(input("Taper un numero a rechercher : "))
                    stg = self.rechecher(N)
                    if stg is not None:
                        print(stg)
                    else:
                        print("Stagiaire introvable ")
                elif rep == 4:
                    A = int(input("Taper a Numero a Supprimer : "))
                    self.supprimer(A)
                elif rep == 5:
                    print("Quttier")
                else:
                    print('Error')
if __name__=='__main__':
            et1=Etablissment("isfo", "Casablanca")
            et1.main()          