import math
class Kin:
    def storeGivensX(self):
        print("Please type 0 for the values that are to be found")
        print("If this problem involves gravity, please type 1 for the final and initial velocty and -9.8 for acceleration")
        print("What is the acceleration?")
        a = input()
        print("What is the change in time")
        t = input()
        print("What is the distance?")
        d = input()
        print("What is the final velocity?")
        vf = input()
        print("What is the initial velocity?")
        v0 = input()
        dict = {"a" : float(a), "t" : float(t), "d" : float(d), "vf" : float(vf), "v0" : float(v0)}
        return dict
    
    def findvf(self, dict):
        if dict["v0"] == 0:
            dict["v0"] = self.findv0(dict)
            if dict["v0"] == "This problem is not possible":
                return "This problem is not possible"
        if dict["vf"] != 0:
            return dict["vf"]
        elif dict["d"] == 0:
            return dict["v0"] + (dict["a"] * dict["t"])
        elif dict["t"] == 0:
            return math.sqrt(math.pow(dict["v0"], 2) + (2 * dict["a"] * dict["d"]))
        elif dict["a"] == 0:
            return (2*dict["d"] / dict["t"]) - dict["v0"]
        else:
            return "This problem is not possible."
    
    def findv0(self, dict):
        if dict["v0"] != 0:
            return dict["v0"]
        if dict["a"] == 0:
            return (2*dict["d"] / dict["t"]) - dict["vf"]
        elif dict["t"] == 0:
            return math.sqrt(dict["vf"]**2 - (2 * dict["a"] * dict["d"]))
        elif dict["d"] == 0:
            return dict["vf"] - (dict["t"]*dict["a"])
        elif dict["vf"] == 0:
            return (dict["d"] - (0.5 * dict["a"] * (dict["t"]**2))) / dict["t"]
        else:
            return "This problem is not possible."
        
    def finda(self, dict):
        if dict["a"] != 0:
            return dict["a"]
        if dict["v0"] == 0:
            dict["v0"] = self.findv0(dict)
            if dict["v0"] == "This problem is not possible":
                return "This problem is not possible"
        if dict["d"] == 0:
            return (dict["vf"] - dict["v0"]) / dict["t"]
        elif dict["t"] == 0:
            return (math.pow(dict["vf"], 2) - math.pow(dict["v0"], 2)) / (2 * dict["d"])
        elif dict("vf") == 0:
            return ((dict["d"] - (dict["v0"] * dict["t"])) * 2) / (math.pow(dict["t"], 2))
        else:
            return "This problem is not possible."

    def findt(self, dict):
        if dict["t"] != 0:
            return dict["t"]
        if dict["v0"] == 0:
            dict["v0"] = self.findv0(dict)
            if dict["v0"] == "This problem is not possible":
                return "This problem is not possible"
        if dict["d"] == 0:
            return (dict["vf"] - dict["v0"]) / dict["a"]
        elif dict["vf"] == 0:
            if (math.pow(dict["v0"], 2) - (2*dict["a"]*(-dict["d"]))) < 0:
                return "This problem is not possible"
            x = (-dict["v0"] + (math.sqrt(math.pow(dict["v0"], 2) - (2*dict["a"]*(-dict["d"]))))) / (dict["a"])
            if x < 0:
                x = (-dict["v0"] - (math.sqrt(math.pow(dict["v0"], 2) - (2*dict["a"]*(-dict["d"]))))) / (dict["a"])
            return x
        elif dict["a"] == 0:
            return (2*dict["d"]) / (dict["v0"] + dict["vf"])
        else:
            return "This problem is not possible."
    
    def findd(self, dict):
        if dict["d"] != 0:
            return dict["d"]
        if dict["v0"] == 0:
            dict["v0"] = self.findv0(dict)
            if dict["v0"] == "This problem is not possible":
                return "This problem is not possible"
        elif dict["vf"] == 0:
            return (dict["vi"] * dict["t"]) + (0.5*dict["a"]*(math.pow(dict["t"], 2)))
        elif dict["t"] == 0:
            return (math.pow(dict["vf"], 2) - math.pow(dict["v0"], 2)) / (2 * dict["a"])
        elif dict["a"] == 0:
            return (0.5*dict["t"]) * (dict["v0"] + dict["vf"])
        else:
            return "This problem is not possible."
        
    def pickFunction(self):
        dict = self.storeGivensX()
        print("What would you life to find?")
        print("Type 1 for Acceleration")
        print("Type 2 for Final Velcoity")
        print("Type 3 for Initial Velocity")
        print("Type 4 for Distance")
        print("Type 5 for Time")
        x = input()
        if x == "1":
            ans = self.finda(dict)
            print(f"The Acceleration is {ans} m/s^2")
        elif x == "2":
            ans = self.findvf(dict)
            print(f"The final velocty is {ans} m/s")
        elif x == "3":
            ans = self.findv0(dict)
            print(f"The inital velocty is {ans} m/s")
        elif x == "4":
            ans = self.findd(dict)
            print(f"The distance is {ans} m")
        elif x == "5":
            ans = self.findt(dict)
            print(f"The time is {ans} s")
        else:
            print("That wasn't a number between 1-5")
            print("Please type 0 to run this program again")
            x = input()
            if x == "0":
                self.pickFunction()
k = Kin()
k.pickFunction()

            




        
    
    
        
    