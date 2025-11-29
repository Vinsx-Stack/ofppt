#self.numero represente l'attribut d'instance
#cad la variable associee a l'objet qui exist
#a partir de la creation de l'objet jusqu'a
#sa destruction
#la variable numero represente le parametre 
#recu par le constructeur et n'existe que dans le corps de ce dernier

#methode
class Stagiaire:
  def __init__(self,numero,nom,note):
    self.numero = numero
    self.nom = nom
    self.note = note
  def afficher(self):
    print(f"{self.numero}\t{self.nom}\t{self.note}")
#exemple
if __name__=='__main__':
  stg = Stagiaire(100,"Chouaib",12.45)
  stg.afficher()