class Salaries:
  def __init__(self, matricule, nom, prenom, salaire, taux):
    self.__matricule=matricule
    self.__nom=nom
    self.__prenom=prenom
    self.__salaire=salaire
    self.__taux=taux
  def getmatricule(self):
    return self.__matricule
  def setmatricule(self, newValue):
    self.__matricule = newValue
  def getnom(self):
    return self.__nom
  def setnom(self, newValue):
    self.__nom = newValue
  def getprenom(self):
    return self.__prenom
  def setprenom(self, newValue):
    self.__prenom = newValue
  def getsalaire(self):
    return self.__salaire
  def setsalaire(self, newValue):
    self.__salaire = newValue
  def salairenet(self):
    return self.__salaire-(self.__salaire * self.__taux)
  def __str__(self):
    return f"{self.__matricule}\t{self.__nom}\t{self.__prenom}\t{self.__salaire} dhs\t{self.__taux}\t{self.salairenet():.0f} dhs"
  
if __name__=='__main__':
  
  s1=Salaries(5868510, "Lasfar", "Mohammed Adnane", 5000, 0.25)
  print(f"Salaire  net du 1er Salarie: {s1.salairenet()} dhs")
  s2=Salaries(5976543, "Lasfar", "Rayane", 10000, 0.25)
  print(f"Salaire  net du 2e Salarie: {s2.salairenet()} dhs")
  print(s1)
  print(s2)