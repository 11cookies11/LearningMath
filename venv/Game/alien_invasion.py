import random
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


    def model_generator(self):
        self.ship = Ship()
        self.ship.x = 20
        self.ship.y = 20
        self.asteroids = [Asteroid() for _ in range(0,20)]
        for ast in self.asteroids:
            ast.x = random.randint(0,50)
            ast.y = random.randint(0,50)

    def limit_screen(self,vector):
        if vector[0] < 0:
            tmp_x = vector[0] + self.settings.screen_width/10
        elif vector[0] > self.settings.screen_width/10:
            tmp_x = vector[0] - self.settings.screen_width/10
        else:
            tmp_x = vector[0]

        if vector[1]  < 0:
            tmp_y = vector[1] + self.settings.screen_height/10
        elif vector[1] > self.settings.screen_height/10:
            tmp_y = vector[1] - self.settings.screen_height/10
        else:
            tmp_y = vector[1]

        return (tmp_x,tmp_y)

    def to_pixels(self,x,y):
        return (x*10, y*10)

    def draw_poly(self,screen,model,color=(0,0,0)):
        pixel_points = [self.to_pixels(x,y) for x,y in model.calc_move()]
        pygame.draw.aalines(screen,color,True,pixel_points,10)

    def draw_segment(self,screen,start,end,color=(0,0,0)):
        pygame.draw.line(surface =screen,color=color,start_pos=self.to_pixels(start[0], start[1]) ,end_pos=self.to_pixels(end[0], end[1]))

    def test_unit(self):
        while True:
            self.screen.fill(self.settings.bg_color)
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if keys[pygame.K_SPACE]:
                start, end = self.ship.op_attack()
                self.draw_segment(self.screen, start, end, color=(0, 0, 0))

            if keys[pygame.K_a]:#飞机进行旋转
                self.ship.rotation_angle -= math.pi/(360*4)


            if keys[pygame.K_d]:#飞机进行旋转
                self.ship.rotation_angle += math.pi/(360*4)

            if keys[pygame.K_w]:
                self.ship.x += math.cos(self.ship.rotation_angle+math.pi/2)*0.01
                self.ship.y += math.sin(self.ship.rotation_angle+math.pi/2)*0.01

            if keys[pygame.K_s]:
                self.ship.x -= math.cos(self.ship.rotation_angle+math.pi/2)*0.01
                self.ship.y -= math.sin(self.ship.rotation_angle+math.pi/2)*0.01

            self.draw_poly(self.screen,self.ship)
            for ast in self.asteroids:
                ast.x += random.randint(0,1)*0.01
                ast.y += random.randint(0,1)*0.01
                ast.x = self.limit_screen((ast.x,ast.y))[0]
                ast.y = self.limit_screen((ast.x,ast.y))[1]
                self.draw_poly(self.screen,ast)
            pygame.display.flip()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)

            pygame.display.flip()

if __name__ == '__main__':
    ai = ALIENINVASION()
    ai.test_unit()