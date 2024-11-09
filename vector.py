import math
class Vector:
    vector = [1, 1, 1]
    
    def toRadians(self, theta):
        return theta * math.pi / 180
    
    def magnitude(self, vector):
        return math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    
    def angle(self): #2D only
        print("Please remember this only works in 2D space, so make sure to enter 0 for the last value")
        vector = self.getVector()
        return (math.atan(vector[1]/vector[0])) * (180/math.pi)
    
    def dotProduct(self, vector1, vector2):
        return (vector1[0]*vector2[0]) + (vector1[1]*vector2[1]) + (vector1[2]*vector2[2])
    
    def angleBetween(self):
        vector1 = self.getVector()
        vector2 = self.getVector()
        return math.acos((self.dotProduct(vector1, vector2)) / (self.magnitude(vector1) * self.magnitude(vector2))) * (180/math.pi)
    
    def sum(self, vector1, vector2):
        arr = [(vector1[0] + vector2[0]), (vector1[1] + vector2[1]), (vector1[2] + vector2[2])]
        return arr
    
    def scale(self, vector, scalar):
        arr = [vector[0] * scalar, vector[1] * scalar, vector[2] * scalar]
        return arr
    
    def getTheta(self):
        print("What is the angle of elevation in degrees?: ")
        theta = input()
        theta = float(theta)
        return theta
    
    def getVector(self):
        print("Please type in 3 numbers that correspond to the x, y, and z components of the vector: ")
        x, y, z = input().split()
        x, y, z = float(x), float(y), float(z)
        return [x, y, z]
    

    
