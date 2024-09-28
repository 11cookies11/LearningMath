import random
from vector import Vector
import math
from settings import SETTINGS

class PolygonModel():
    def __init__(self,points):
        self.points = points
        self.rotation_angle = math.pi/2
        self.x = 0
        self.y = 0
        self.length = 0
        self.settings = SETTINGS()
        self.vector = Vector()

class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(3,-3),(3,0),(4.5,3),(6,0),(6,-3)])

    def calc_move(self):
        tmp_points = self.points
        result_points = []
        for i in tmp_points:
            tmp_polar_coordinate = self.vector.to_polar_coordinate(i)
            tmp_xy_coordinate = self.vector.to_cartersion((tmp_polar_coordinate[0] + self.length,tmp_polar_coordinate[1] + self.rotation_angle))
            result_points.append((tmp_xy_coordinate[0]+self.x,tmp_xy_coordinate[1]+self.y))
        return result_points


        return [(x+self.x,y+self.y) for x,y in self.points]

    def op_attack(self):
        xy_coordinate = self.vector.to_polar_coordinate(self.points[2])
        polar_coordinate = self.vector.to_cartersion((xy_coordinate[0]+self.length,xy_coordinate[1]+self.rotation_angle))
        dist = math.sqrt(self.settings.screen_height**2 + self.settings.screen_width**2)
        attack_origin_coordinate = (polar_coordinate[0] +self.x,polar_coordinate[1]+self.y)
        attack_result_coordinate = (self.vector.to_cartersion((dist,self.rotation_angle+math.pi/2))[0]+self.x,self.vector.to_cartersion((dist,self.rotation_angle+math.pi/2))[1]+self.y)
        return attack_origin_coordinate,attack_result_coordinate

class Asteroid(PolygonModel):
    def __init__(self):
        sides = random.randint(5,9)
        vector = Vector()
        vs = [vector.to_cartersion((random.randint(1,2),2*math.pi*i/sides)) for i in range(random.randint(4,sides))]
        super().__init__(vs)

    def calc_move(self):
        return [(x+self.x,y+self.y) for x,y in self.points]