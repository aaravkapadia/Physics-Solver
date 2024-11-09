from newtonsLaws import Force
import math

class Friction(Force):
    
    def findFrict(self,m):
        print("What is the frictional coefficient?: ")
        u = input()
        u = float(u)
        return super().findFNorm(m, 0) * u
    
f = Friction()
print(f.findFrict(10))
    
    