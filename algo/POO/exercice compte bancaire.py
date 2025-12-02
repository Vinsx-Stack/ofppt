class Client:
    def __init__(self,n:str,p:str,v:str):
        self.__nom=n
        self.__prenom=p
        self.__ville=v

    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,n):
        self.__nom=n
    @property
    def Prenom(self):
        return self.__prenom
    @Prenom.setter
    def Prenom(self,p):
        self.__prenom=p
    @property
    def Ville(self):
        return self.__ville
    @Ville.setter
    def Ville(self,v):
        self.__ville=v


class Compte:
    def __init__(self,numero:int,c:Client,solde:float):
        self.__numero=numero
        self.__client=c
        self.__solde=solde


    def getnumero(self): 
        return self.__numero
    
    def setNumero(self,new): 
        self.__numero=new

    def getclient(self): 
        return self.__client
    
    def setclient(self,new): 
        self.__client=new

    def getsolde(self): 
        return self.__solde
    
    def deposer(self,m):
        self.__solde+=m

    def retirer(self,m):
        if self.__solde>m:
          self.__solde-=m
        else:
            print("ce solde n'est pas suffisent")
    
    def __str__(self):
        return  f"{self.__numero} \t {self.__client.Nom}\t{self.__client.Prenom}\t{self.__solde}"
 

c1=Client("kenza","kenzaa","casablanca")
c2=Client("mouhim","mohamed","casablanca")


cmpte=Compte(1,c2,2000)
print(cmpte)
n=float(input("donner le montant pour deposer:"))
cmpte.deposer(n)
print(cmpte)
n=int(input("donner le montant pour retirer:"))
cmpte.retirer(n)
print(cmpte)