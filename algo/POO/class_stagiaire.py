class Stagiaire:
  numero=0
  nom=""
  note=0.0
  def afficher(self):
    print(f"{self.numero}\t{self.nom}\t{self.note}")

if __name__=='__main__':
  stg=Stagiaire()
  stg.numero=100
  stg.nom="Tazi"
  stg.note=15.25