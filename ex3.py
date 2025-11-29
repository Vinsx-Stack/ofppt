class salaire:
    def __init__(self, name, pernom, matrucule, salaire, taux):
        self.__name=name
        self.__pernom=pernom
        self.__matrucule=matrucule
        self.__salaire=salaire
        self.__taux=taux

    def getName(self):
        return self.__name
    def getPernom(self):
        return self.__pernom
    def getMatrucule(self):
        return self.__matrucule
    def getSalaire(self):
        return self.__salaire
    def getTaux(self):
        return self.__taux
    def setName(self, new):
        self.__name=new
    def setPernom(self, new):
        self.__pernom=new
    def setMatrucule(self, new):
        self.__matrucule=new
    def setSalaire(self, new):
        self.__salaire=new
    def setTaux(self, new):
        self.__taux=new
    def calculerSalaire(self):
        return self.__salaire - (self.__salaire * self.__taux / 100)
    def __str__(self):
        return f"{self.__name}\t {self.__pernom}\t {self.__matrucule}\t {self.calculerSalaire()} DH"
employe = salaire
c1=salaire('Yahya','bellefkih', 1, 10000, 25)
c2=salaire('Reda','bellefkih', 2, 5000, 25)
c3=salaire('Hind','bellefkih', 3, 7000, 20)
print(c1)
print(c2)
print(c3)