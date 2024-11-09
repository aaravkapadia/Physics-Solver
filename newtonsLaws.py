import math
from vector import Vector
class Force(Vector):
    g = 9.8

    def askForMass(self):
        print("What is the mass? ")
        m = input()
        m = float(m)
        return m
    
    def findF(self, m):
        theta = super().getTheta()
        a = super().getVector()
        if theta == 0:
            print("Type 1 for vector and 2 for magnitude")
            x = input()
            x = int(x)
            if x == 1:
                return super().scale(a, m)
            elif x ==2:
                mag = super().magnitude(a)
                return mag * m
        else:
            return(m * self.g * math.sin(super().toRadians(theta)))
        
    def findA(self, f, m):
        theta = super().getTheta()
        print("Type 1 for vector and 2 for magnitude")
        x = input()
        x = int(x)
        if x == 1:
            return super().scale(f, (1/m))
        elif x ==2:
            mag = super().magnitude(f)
            return mag * (1/m)
    
    def findM(self, f, a):
        return f / a
    
    def findFNorm(self,m,theta):
        super.getTheta()
        return m * self.g * math.cos(super().toRadians(theta))
    
    
            
            
        
    
    
    





    
