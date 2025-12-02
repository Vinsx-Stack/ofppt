

class Stagiaire:
    compteur=1
    def __init__(self, n=None, a=None):

        self.__numero=Stagiaire.compteur
        self.__name=n
        self.__age=a
        Stagiaire.compteur+=1

    @property
    def Numero(self):
        return self.__numero
    @Numero.setter
    def Numero(self,new):
        self.__numero=new

    @property
    def Name(self):
        return self.__name
    @Numero.setter
    def Name(self,new):
        self.__name=new
    @property
    def Age(self):
        return self.__age
    @Age.setter
    def Age(self,new):
        self.__age=new

    def __str__(self):
        return f"Number:  {self.Numero}\t Name : {self.Name}\t Age : {self.Age} ans"
    

if __name__ == '__main__':
    stg1=Stagiaire( 'Anas', 21)
    print(stg1)


    stg2=Stagiaire()
    stg2.Name= 'Yasser'
    stg2.Age = 20
    print(stg2) 