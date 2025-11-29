import math

class Cercle:
  def __init__(self, ra, x, y):
    self.radius = ra
    self.absci = x
    self.ordon = y
  def surface(self):
    return math.pi*self.radius**2
  def perimetre(self):
    return 2*math.pi*self.radius
  def afficher(self):
    print(f"Surface: {self.surface():.2F}\tPerimetre: {self.perimetre():.2F}")

if __name__=='__main__':
  Cercle = Cercle(7, 77, 88)
  Cercle.afficher()