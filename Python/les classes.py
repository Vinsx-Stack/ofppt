class Stagiare :
    numero = 0
    nom=""
    note=0.0
    def afficher(self):
        print(f"{self.numero}\t{self.nom}\t{self.note}")

if __name__ == '__main__' :
    stg=Stagiare()
    stg.numero=100
    stg.nom="tazi"
    stg.note = 15.25
    stg.afficher()
##################################################
class Stagiare :
    def __init__(self,numero,nom,note):
        self.numero=numero
        self.nom=nom
        self.note=note
#self.numero represent lattribut dinstance
#cad la vraible associee a lobjet qui existe
#a partire de la creation de lobject jusqu a  sa destruction
# la varaible numero represente le parametre recu par le constructeur et n existe que 
# dans le crops de ce dernier 

if __name__ == '__main__' :
    stg=Stagiare()
    stg.afficher()