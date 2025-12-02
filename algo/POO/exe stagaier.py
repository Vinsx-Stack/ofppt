

class Stagaire:
    def __init__(self, num=None, n=None, a=None):
        compteur=1
        self.__numero=num
        self.__name=n
        self.__age=a

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
    stg1=Stagaire(1000, 'Anas', 21)
    print(stg1)


    stg2=Stagaire()
    stg2.Numero=2000
    stg2.Name= 'Yasser'
    stg2.Age = 20
    print(stg2) 