import math
class Cercle :
    def __init__(self,x,y,ra):
        self.absci= x
        self.ordon = y
        self.radius = ra 
    
    def surface(self):
        return math.pi*self.radius**2
    
    def perimetre(self):
        return self.radius*2*math.pi
    
    def Afficher(self):
        print(f"Le cercle de rayon: {self.radius}, la position de son centre est O({self.absci},{self.ordon})")
        print(f"La surface est {self.surface(): .2F}")
        print(f"Le perimetre est: {self.perimetre(): .2F}")
    
r=float(input("taper le rayon: "))
xe=float(input("taper l'abscisse du centre: "))
ye=float(input("taper l'ordonnée du centre: "))
cer1=Cercle(xe,ye,r)
cer1.Afficher()

        