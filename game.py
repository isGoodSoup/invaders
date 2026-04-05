import pygame

class Game:
    def __init__(self):
        pass

    def run(self):
        pass

game = Game()

if __name__ == '__main__':
    pygame.init()
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    fps = 60

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        game.run()
        pygame.display.flip()
        clock.tick(fps)