#un stagiaire est defini par son numero, son nom et sa note a l'examen
#les attribute doivent etre prives
class Stagiaire:

  def __init__(self,numero,nom,note):
    self.__numero=numero
    self.__nom=nom
    self.__note=note
  #GETTER pour le numero
  def getNumero(self):
    return self.__numero
  #SETTER pour le numero
  def setNumero(self, newValue):
    self.__numero=newValue
  #GETTER pour le nom
  def getNom(self):
    return self.__nom
  #SETTER pour le nom
  def setNom(self, newValue):
    self.__nom=newValue
  #GETTER pour le note
  def getNote(self):
    return self.__note
  #SETTER pour le note
  def setNote(self, newValue):
    self.__note = newValue
  def afficher(self):
    print(f"Numero: {self.__numero}")
    print(f"Nom: {self.__nom}")
    print(f"Note: {self.__note}")
  def __str__(self):
    return f"{self.__numero}\t{self.__nom}\t{self.__note}"
  
if __name__=='__main__':
  stg=Stagiaire(1000,"Ali", 13.55)
  stg.afficher()
  print("---------------------------------------")
  #for numero
  print(stg.getNumero())
  stg.setNumero(2000)
  print(f"Nouveau numero: {stg.getNumero()}")
  print("---------------------------------------")
  print(stg.getNom())
  stg.setNom("Mohamed")
  print(f"Nouveau nom: {stg.getNom()}")
  print("---------------------------------------")
  print(stg.getNote())
  stg.setNote(15.75)
  print(f"Nouvelle note: {stg.getNote()}")
  print("---------------------------------------")
  stg.afficher()
  print("---------------------------------------")
  print(stg)