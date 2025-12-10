class Stagiaire:
    def __init__(self, n, nom, f):
        self.__numero = n
        self.__nom = nom
        self.__filiere = f

    # get et set pour Numero
    @property
    def Numero(self):
        return self.__numero

    @Numero.setter
    def Numero(self, new):
        self.__numero = new

    # get et set pour Nom
    @property
    def Nom(self):
        return self.__nom

    @Nom.setter
    def Nom(self, new):
        self.__nom = new

    # get et set pour Filiere
    @property
    def Filiere(self):
        return self.__filiere

    @Filiere.setter
    def Filiere(self, new):
        self.__filiere = new

    def __str__(self):
        return f"{self.__numero}\t{self.Nom}\t{self.Filiere}"


class Etablissement:
    c = 1

    def __init__(self, efp, ville):
        self.code = Etablissement.c
        self.EFP = efp
        self.ville = ville
        self.Lstg = []
        Etablissement.c += 1

    def Ajouter(self):
        saisie = "Y"
        while saisie.upper() == "Y":
            num = int(input("Taper le numéro : "))
            nom = input("Taper le nom : ")
            filiere = input("Taper la filière : ")

            stg = Stagiaire(num, nom, filiere)
            self.Lstg.append(stg)

            print("Ajout avec succès.")
            saisie = input("Voulez-vous ajouter un autre stagiaire ? (Y/N) : ")

    def Afficher(self):
        print(f"{self.code}\t{self.EFP}\t{self.ville}")
        print("Liste des stagiaires :")
        print("Numéro\tNom\tFilière")

        for s in self.Lstg:
            print(s)

        print(f"Il y a {len(self.Lstg)} stagiaires.")

    def Rechercher(self, num):
        for s in self.Lstg:
            if s.Numero == num:
                return s
        return None

    def Supprimer(self, num):
        s = self.Rechercher(num)
        if s is not None:
            rep = input("Voulez-vous vraiment supprimer ? (1=oui / 0=non) : ")
            if rep == "1":
                self.Lstg.remove(s)
                print("Suppression avec succès.")
        else:
            print("Stagiaire introuvable.")

    def Main(self):
        saisie = True
        while saisie:
            print("\n************ Menu Général **************")
            print("1 - Ajouter les stagiaires")
            print("2 - Afficher tous les stagiaires")
            print("3 - Rechercher un stagiaire")
            print("4 - Supprimer un stagiaire")
            print("5 - Quitter")
            rep = int(input("Choisissez une opération : "))

            if rep == 1:
                self.Ajouter()
            elif rep == 2:
                self.Afficher()
            elif rep == 3:
                N = int(input("Taper le numéro à rechercher : "))
                stg = self.Rechercher(N)
                if stg is not None:
                    print(stg)
                else:
                    print("Stagiaire introuvable.")
            elif rep == 4:
                A = int(input("Taper le numéro à supprimer : "))
                self.Supprimer(A)
            elif rep == 5:
                print("FIN DU PROGRAMME.")
                saisie = False
            else:
                print("Opération invalide.")


if __name__ == "__main__":
    et1 = Etablissement("isfo", "Casablanca")
    et1.Main()
