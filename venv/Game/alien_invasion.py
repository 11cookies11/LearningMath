import random
from Game.model import Ship,Asteroid
from settings import SETTINGS
import sys
import pygame
import time

class ALIENINVASION():
    def __init__(self):
        self.settings = SETTINGS()
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.model_generator()


    def model_generator(self):
        self.ship = Ship()

        self.asteroids = [Asteroid() for _ in range(0,10)]
        for ast in self.asteroids:
            ast.x = random.randint(-9,9)
            ast.y = random.randint(-9,9)

    def to_pixels(self,x,y):
        return (x*10,-y*10)

    def draw_poly(self,screen,model,color=(0,0,0)):
        pixel_points = [self.to_pixels(x,y) for x,y in model]
        print(pixel_points)
        pygame.draw.aalines(screen,color,True,pixel_points,10)

    def test_unit(self):
        self.screen.fill((230, 230, 230))
        for ast in self.asteroids:
            self.draw_poly(self.screen,ast.points)
        pygame.display.flip()

        time.sleep(20000)



    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ai = ALIENINVASION()
    ai.test_unit()