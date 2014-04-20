import math
 
class Exponential:
    def __init__(self, beta):
        self.beta = beta
        
    def value(self, aNumber):
        return 1.0/(1.0+math.exp(-2 * self.beta * aNumber))
 
    def isSigmoid(self):
        return True
 
    def derive(self, aNumber):
        gValue = self.value(aNumber)
        return 2 * self.beta * self.value(1-gValue)
        
class Identity:
    
    def value(self, value):
        return value
    
    def isSigmoid(self):
        return True
    
class Sign:
    
    def value(self, value):
        if value >= 0:
            return 1.0
        return -1.0
        
    def isSigmoid(self):
        return True