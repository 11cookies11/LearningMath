import random


class PolygonModel():
    def __init__(self,points):
        self.points = points
        self.rotation_angle = 0
        self.x = 0
        self.y = 0

class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(0.5,0),(0.25,0.25),(0.25,0.25)])

class Asteroid(PolygonModel):
    def __init__(self):
        sides = random.randint(5,9)
        vs = [(1,4),(-2,5),(-1.2,4)]
        super().__init__(vs)




