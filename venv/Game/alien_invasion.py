import random
from flag import Flags
import numpy as np

from model import Ship,Asteroid
from settings import SETTINGS
from vector import Vector
import sys
import pygame
import math

class ALIENINVASION():
    def __init__(self):
        pygame.init()
        self.vector = Vector()
        self.settings = SETTINGS()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.model_generator()
        self.flag = Flags()


    def model_generator(self):
        self.ship = Ship()
        self.ship.x = 0
        self.ship.y = 0
        self.asteroids = [Asteroid() for _ in range(0,20)]
        for ast in self.asteroids:
            ast.x = random.randint(-500,500)
            ast.y = random.randint(-500,500)

    def limit_screen(self,vector):
        if vector[0] < -self.settings.screen_width/self.settings.scale_factor/2:
            tmp_x = vector[0] + self.settings.screen_width/self.settings.scale_factor
        elif vector[0] > self.settings.screen_width/self.settings.scale_factor/2:
            tmp_x = vector[0] - self.settings.screen_width/self.settings.scale_factor
        else:
            tmp_x = vector[0]

        if vector[1]  < -self.settings.screen_height/self.settings.scale_factor/2:
            tmp_y = vector[1] + self.settings.screen_height/self.settings.scale_factor
        elif vector[1] > self.settings.screen_height/self.settings.scale_factor/2:
            tmp_y = vector[1] - self.settings.screen_height/self.settings.scale_factor
        else:
            tmp_y = vector[1]

        return (tmp_x,tmp_y)

    def to_pixels(self,x,y):
        return (x * self.settings.scale_factor + self.settings.screen_width / 2,
                -y * self.settings.scale_factor + self.settings.screen_height / 2)

    def to_coordinate(self,x,y):
        return ((x - self.settings.screen_width / 2)/self.settings.scale_factor ,
                (y - self.settings.screen_height / 2)/self.settings.scale_factor )

    def draw_poly(self,screen,model,color=(0,0,0)):
        pixel_points = [self.to_pixels(x,y) for x,y in model.calc_move()]
        pygame.draw.aalines(screen, color, True, pixel_points, 10)
        # if self.does_hit(pixel_points):
        #     print("消灭----")
        # else:
        #     pygame.draw.aalines(screen,color,True,pixel_points,10)

    def draw_segment(self,screen,start,end,color=(0,0,0)):
        pygame.draw.line(surface =screen,color=color,start_pos=self.to_pixels(start[0], start[1]) ,end_pos=self.to_pixels(end[0], end[1]))

    def does_hit(self,points):
        # 确保列表不为空
        if not points:
            return []

            # 使用列表生成式处理相邻元素的组合
        pairs = [(points[i], points[i + 1]) for i in range(len(points) - 1)]

        # 将最后一个元素与第一个元素组合，并添加到结果列表中
        # 注意：这里我们使用了pairs列表的append方法，因为列表生成式已经完成了
        pairs.append((points[-1], points[0]))
        # tmp_j = []
        # tmp_i = []
        # for i in pairs:
        #     for j in i:
        #         tmp_j.append(self.to_coordinate(j[0],j[1]))
        #     tmp_i.append(tmp_j[:])
        #     tmp_j.clear()
        for i in pairs:
            result,_ = self.does_intersect(i[0],i[1])
            if result:
                return True

    def does_intersect(self,point1,point2):
        start, end = self.ship.op_attack()
        x1 = start[0]
        y1 = start[1]
        x2 = end[0]
        y2 = end[1]
        x3 = point1[0]
        y3 = point1[1]
        x4 = point2[0]
        y4 = point2[1]
        calc_matrix = np.array([[y2-y1,-(x2-x1)],
                                [y4-y3,-(x4-x3)],])
        output = np.array([[x1*y2-x2*y1],
                           [x3*y4-x4*y3]])

        tmp = np.linalg.solve(calc_matrix, output).T
        try:
            distanc_1 = self.vector.distance((tmp[0][0],tmp[0][1]),point1)
            distanc_2 = self.vector.distance((tmp[0][0],tmp[0][1]),point2)
            distanc_3 = self.vector.distance(point1,point2)

            distance_4 = self.vector.distance((tmp[0][0],tmp[0][1]),start)
            distance_5 = self.vector.distance((tmp[0][0],tmp[0][1]),end)
            distance_6 = self.vector.distance(start,end)

            if (distanc_1 + distanc_2 > distanc_3) or (distance_4 + distance_5 > distance_6):
                return False,np.array([[0],
                                   [0]])
            else:
                return True,tmp.T
        except:
            return False,np.array([[0],
                                   [0]])


    def key_event(self):
        self.flag.clear_all_flags()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if keys[pygame.K_SPACE]:
            self.flag.set_flag(self.flag.FLAG_ATTACK)
            start, end = self.ship.op_attack()
            self.draw_segment(self.screen, start, end, color=(0, 0, 0))

        if keys[pygame.K_a]:  # 飞机进行旋转
            self.ship.rotation_angle -= math.pi / (360 * 4)

        if keys[pygame.K_d]:  # 飞机进行旋转
            self.ship.rotation_angle += math.pi / (360 * 4)

        if keys[pygame.K_w]:
            self.ship.x += math.cos(self.ship.rotation_angle + math.pi / 2) * 0.01
            self.ship.y += math.sin(self.ship.rotation_angle + math.pi / 2) * 0.01

        if keys[pygame.K_s]:
            self.ship.x -= math.cos(self.ship.rotation_angle + math.pi / 2) * 0.01
            self.ship.y -= math.sin(self.ship.rotation_angle + math.pi / 2) * 0.01

    def run_game(self):
        while True:
            self.screen.fill(self.settings.bg_color)

            '''按键操作'''
            self.key_event()

            '''飞船'''
            self.draw_poly(self.screen,self.ship)

            '''辅助线'''
            pygame.draw.line(self.screen,(200,233,10),self.to_pixels(-100,0),self.to_pixels(100,0))
            pygame.draw.line(self.screen, (200,233,10), self.to_pixels(0, -100), self.to_pixels(0, 100))
            pygame.draw.line(self.screen,(200,211,10),self.to_pixels(3,5),self.to_pixels(3,-6))

            '''陨石'''
            for ast in self.asteroids:
                ast.x += random.randint(0,1)*0.01
                ast.y += random.randint(0,1)*0.01
                ast.x = self.limit_screen((ast.x,ast.y))[0]
                if self.flag.is_flag_set(self.flag.FLAG_ATTACK) and self.does_hit(ast.calc_move()):
                    self.asteroids.remove(ast)
                else:
                    self.draw_poly(self.screen,ast)
            pygame.display.flip()


if __name__ == '__main__':
    ai = ALIENINVASION()
    ai.run_game()