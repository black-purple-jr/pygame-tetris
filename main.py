from sys import exit

from settings import *
from game import Game


class Main:
    def __init__(self):
        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")
        self.game = Game()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # display
            self.display_surface.fill(GRAY)

            self.game.run()

            # update the game
            pygame.display.update()
            self.clock.tick()
    

if __name__ == '__main__':
    main = Main()
    main.run()