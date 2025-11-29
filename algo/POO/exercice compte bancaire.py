class Compte:
  def __init__(self, numero, titulaire, solde=0):
    self.__numero = numero
    self.__titulaire = titulaire
    self.__solde = solde
  def get_numero(self):
    return self.__numero
  def set_numero(self, new_value):
    self.__numero = new_value
  def get_titulaire(self):
    return self.__titulaire
  def set_titulaire(self, new_value):
    self.__titulaire = new_value
  def get_solde(self):
    return self.__solde
  def set_solde(self, new_value):
    self.__solde = new_value
  def afficher(self):
    print(f"Numero: {self.__numero}")
    print(f"Nom du client: {self.__titulaire}")
    print(f"Solde du compte: {self.__solde} euros")
  
  def depot(self, montant):
    self.__solde += montant
  def retirer(self, montant):
    if montant < self.__solde:
      print("Montant retirer avec succes !")
      self.__solde = self.__solde - montant
    else:
      print("Fonds insuffisant sur votre compte.")

  def __str__(self):
    return f"{self.__numero}\t{self.__titulaire}\t{self.__solde} euros"

if __name__=='__main__':
  c1=Compte(1001, "Rayane Lasfar", 5000)
  c1.afficher()
  print("-----------------------------------")
  montant_depot = float(input("Tapez le montant a deposer: "))
  c1.depot(montant_depot)
  print("-----------------------------------")
  montant_retrait = float(input("Tapez le montant a retirer: "))
  c1.retirer(montant_retrait)
  print("-----------------------------------")
  print(c1)

