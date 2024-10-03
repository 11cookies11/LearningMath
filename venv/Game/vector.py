import math


class Vector():
    def __init__(self):
        pass

    def to_cartersion(self,vector):
        return (vector[0]*math.cos(vector[1]),vector[0]*math.sin(vector[1]))

    def to_polar_coordinate(self,vector):
        return (math.sqrt(vector[0]**2+vector[1]**2),math.atan2(vector[1],vector[0]))

    def distance(self,start_point,end_point):
        return math.sqrt((end_point[0] - start_point[0])**2+(end_point[1] - start_point[1])**2)