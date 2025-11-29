class stagiaire():
    def __init__(self,numero,nom,note):
        self.__numero=numero
        self.__nom=nom
        self.__note=note
    def getNumero (self):
        return self.__numero

    def setNumero (self, newValue):
        self.__numero=newValue

    def getNom (self):
        return self.__nom
    
    def setNom (self, new):
        self.__nom=new

    def setNote(self, new):
        self.__note=new

    def getNote(self):
        return self.__note
    
    def __str__(self):
        return f"{self.__numero}\t {self.__nom}\t {self.__note}"



stg= stagiaire(10, 'Ali', 13)  

stg.setNom('Anas')
stg.setNote(20)
stg.setNumero(30)

print(stg.__str__())