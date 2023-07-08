#!/usr/bin/env python3
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

p = Point(3, 5)
print(repr(p))


class Tester:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience
    
    def __repr__(self):
        if self.experience<1:
            return f'junior'
        elif self.experience<4:
            return f'middle'
        else:
            return f'senior'
        
test = Tester('Lada', 2)
print(repr(test))