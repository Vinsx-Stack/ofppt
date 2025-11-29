class Person:
  def __init__(self, nom, ville='Casablanca'):
    self.nom = nom
    self.ville = ville
  def afficher(self):
    print(f"Nom: {self.nom}")
    print(f"Ville natale: {self.ville}")

if __name__=='__main__':
  p1=Person('Rayane')
  print("Infos sur la premiere personne: ")
  p1.afficher()
  p2=Person('Michelle', 'France')
  print("Infos sur la deuxieme personne: ")
  p2.afficher()