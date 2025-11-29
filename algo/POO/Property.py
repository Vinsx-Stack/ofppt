class Person:
  def __init__(self, n, p, a):
    self.__nom=n
    self.__prenom=p
    self.__age=a
  @property
  def Nom(self):
    return self.__nom
  @Nom.setter
  def Nom(self, value):
    self.__nom = value
  def __str__(self):
    return f"{self.__nom}\t{self.__prenom}\t{self.__age} ans"
if __name__=='__main__':
  p1=Person("Amine","Mohamed",22)
  print(p1.Nom)
  p1.Nom="Aicha"
  print(p1.Nom)

