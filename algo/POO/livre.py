class livre:
  def __init__(self, titre, auteur, prix):
    self.titre = titre
    self.auteur = auteur
    self.prix = prix
  def afficher(self):
    print(f"Le livre'{self.titre}', ecrit par '{self.auteur}' se rend a {self.prix} euros")

if __name__=='__main__':
  KHADRA=livre("Ce que le jour doit a la nuit", "Yasmina KHADRA", "39.99")
  KHADRA.afficher()