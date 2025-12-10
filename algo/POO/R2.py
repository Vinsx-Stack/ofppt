class Stagiaier:
    def __init__(self, nemuro, name, filier):
        self.__nemuero=nemuro
        self.__name=name
        self.__filier=filier
    @property
    def Neumero(self):
        return self.__nemuero
    @Neumero.setter
    def Neumero(self,new):
        self.__nemuero=new
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,new):
        self.__name=new
    @property
    def Filier(self):
        return self.__filier
    @Filier.setter
    def Filier(self,new):
        self.__filier=new
    
    def __str__(self):
        return f"{self.__nemuero}\t{self.__name}\t{self.__filier}"
    
class Etablissement:
    c = 1
    def __init__(self,efp,ville):
        self.code=Etablissement.c
        self.efp=efp
        self.ville=ville
        self.Lstg=[]
        Etablissement.c+=1

    def Ajouter(self):
        saiser = "Y"
        while saiser:
            num = int(input("Taper le numero : "))
            name = input("Taper le nom : ")
            filier = input("taper la filier : ")
            stg = Stagiaier(num,name,filier)
            self.Lstg.append(stg)
            print("Ajouer avec succes ")
            saiser = input(" voulez-vous ajouter un autre stagiaire? Y/N : ")
    def Afficher(self):
        print(f"{self.code}\t{self.efp}\t{self.ville}")
        print("Listes des Stagiaire")
        print ("Nemuro \t Nom \t filier")
        for s in self.Lstg:
            print(s)
        print(f"ily a {len(self.Lstg)} Stagaiere")

    def Rechercher(self,num):
        for s in self.Lstg:
            if s.Numero==num:
                return s
            
    def Supprimer(self,num):
        s=self.Rechercher(num)
        if s is not None:
            rep = bool(int(input("Voulez-vous vraiment supprimer ? 1=oui 0=non")))
            if rep:
                self.Lstg.remove(s)
                print("Suppression avec succes")
            else:
                print("Introvable")
    def Main(self):
        sasier = True
        while sasier:
            print("*****Menu Génèral*****")
            print("1******Ajouter les stagiaires****")
            print("2******Afficher tout les stagiaire****")
            print("3******Rechercher un stagiaire****")
            print("4******Supprimer un stagiaire****")
            print("5*****Quitter*****")
            rep = int(input("Taper Votre choix : "))
            if rep==1:
                self.Afficher()
            elif rep == 2: 
                self.Ajouter()
            elif rep==3:
                N=int(input("Taper a numero a rechercer : "))
                stg = et1.Rechercher(N)
                if stg is not None:
                    print(stg)
                else:
                    print("Introvable")
            elif rep == 4:
                A = int(input("Taper le numero a supprimer : "))
                et1.Supprimer(A)
            elif rep == 5:
                print("FIN DE PROGRAMME")
                sasier = False
            else:
                print("Operation invalide")




if __name__ == '__main__':
    et1=Etablissement("isfo", "Casablanca")
    et1.Main()