import math

class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m1(self):
        if self.x == 0 or self.y == 0:
           return 0
        elif self.x > 0 and self.y > 0:
           return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
    
    def m2(self, a, b):
        return self.m1() == C(a,b).m1() 
    
    def m3(self, a, b):
        distance = math.sqrt((a-self.x)** 2 + (b - self.y)**2)
        return distance > 5

