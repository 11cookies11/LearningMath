from settings import SETTINGS
import sys
import pygame

class ALIENINVASION():
    def __init__(self):
        self.settings = SETTINGS()
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ai = ALIENINVASION()
    ai.run_game()