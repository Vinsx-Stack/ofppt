import math

class point:
    def __init__(self, x=None, y=None):
        self.__ab=x
        self.__ord=y

    @property
    def ab(self):
        return self.__ab
    
    @ab.setter
    def ab(self,new):
        self.__ab=new

    @property
    def ord(self):
        return self.__ord
    
    @ord.setter
    def ord(self,new):
        self.__ord=new

    
    def distance(self):
        return math.sqrt(self.__ab**2+self.__ord**2)
    
    def __str__(self):
        return f"{self.__ab}\t{self.__ord}\t{self.distance()}"


if __name__ == '__main__':
    A=point(12,10)
    print(A)
    B=point(4,3)
    print(B)
    A = point(B.ab, B.ord)
    print(A)