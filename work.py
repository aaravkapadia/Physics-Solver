from vector import Vector
import math

class Work(Vector):
    
    def findWork(self, f, d):
        theta = super().getTheta()
        f = super().magnitude(f)
        d = super().magnitude(d)
        return f * d * math.cos(super().toRadians(theta))
    
    def workKinetic(self, m):
        print("For the inital velocity: ")
        v0 = super().getVector()
        v0 = super().magnitude(v0)
        print("For the final velocity: ")
        vf = super().getVector()
        vf = super().magnitude(vf)
        return (0.5*pow(vf, 2)*m) - (0.5*pow(v0, 2)*m)
    
    def workPower(self, power, t):
        return power * t
    
    def power(self):
        print("For Force")
        f = super().getVector()
        print("For velocity")
        v = super().getVector()
        return super().dotProduct(f, v)
    
    def pEnergy(self, h, m):
        return super().g * h * m
    
    def calcInternalEnergy(self, h):
        m = 1
        k = self.workKinetic(m)
        p = self.pEnergy(h, m)
        return abs(k-p)

        
    
        
        

