class bank:
    def __init__(self, code, nom, prenom, sold=0):
        self.__code=code
        self.__nom=nom
        self.__prenom=prenom
        self.__sold=sold

    def get_code(self):
        return self.__code
    def set_code(self, new):
        self.__code=new
    def get_nom(self):
        return self.__nom
    def set_nom(self, new):
        self.__nom=new
    def get_pernom(self):
        return self.__prenom
    def set_prenom(self, new):
        self.__prenom=new
    def get_sold(self):
        return self.__sold
    def set_sold(self,new):
        self.__sold=new

    def afficher(self):
        print(f"Le Code : {self.__code}\t Le Nom : {self.__nom}\t Le Prenom : {self.__prenom}\t Le Sold : {self.__sold}")

    def deposer(self,montant):
        self.__sold+=montant
        print("Operation Avec Succes")

    def retire(self,montant):
        if montant < self.__sold:
            print("SUCCES")
            self.__sold = self.__sold - montant
        else:
            print("impossible")

    def __str__(self):
        return f"{self.__code}\t {self.__nom} \t {self.__prenom} \t {self.__sold}"
    
if __name__ == '__main__' :
    c1=bank(10,"Anas","Zaami",6000)
    c1.afficher()
    montant_de=float(input("taper le sold a deposer : "))
    c1.deposer(montant_de)
    c1.afficher()
    montant_re=float(input("taper le sold a retire : "))
    c1.retire(montant_re)
    c1.afficher()

