import pygame

from scripts import obstacle
from scripts.obstacle import Block
from scripts.player import Player

class Game:
    def __init__(self):
        # Player
        player = Player([screen_width // 2, screen_height - 50], screen_width)
        self.player = pygame.sprite.GroupSingle(player) # type: ignore

        # Obstacles
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_ammount = 4
        self.obstacle_x_pos = [num * (screen_width/self.obstacle_ammount) for num in range(
            self.obstacle_ammount)]
        self.create_obstacles(screen_width//15, 440, *self.obstacle_x_pos)

    def create_obstacle(self, start_x, start_y, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == "x":
                    x = start_x + col_index * self.block_size + offset_x
                    y = start_y + row_index * self.block_size
                    block = Block(x, y, self.block_size,(241, 79, 80))
                    self.blocks.add(block) # type: ignore

    def create_obstacles(self, start_x, start_y, *offset):
        for offset_x in offset:
            self.create_obstacle(start_x, start_y, offset_x)

    def run(self):
        # update all sprites
        self.player.update()

        # draw all sprites
        self.player.sprite.projectiles.draw(screen)
        self.player.draw(screen)

        self.blocks.draw(screen)

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