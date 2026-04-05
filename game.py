import pygame

from scripts.player import Player

class Game:
    def __init__(self):
        player = Player([screen_width // 2, screen_height - 50], screen_width)
        self.player = pygame.sprite.GroupSingle(player) # type: ignore

    def run(self):
        self.player.update()
        self.player.draw(screen)

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    fps = 60
    game = Game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        game.run()
        pygame.display.flip()
        clock.tick(fps)