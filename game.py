import random

import pygame

from scripts import obstacle
from scripts.obstacle import Block
from scripts.player import Player
from scripts.alien import Alien, Mothership
from scripts.proj import Projectile


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

        # Aliens
        self.aliens = pygame.sprite.Group()
        self.alien_direction = 1
        self.create_aliens(6, 8)
        self.alien_projectiles = pygame.sprite.Group()

        # Mothership
        self.mother = pygame.sprite.GroupSingle()
        self.mothership_spawn_time = random.randint(400,800)

        # Score system
        self.score = 0
        self.high_score = 0

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

    def create_aliens(self, rows, cols, x_distance=64, y_distance=48,
                      x_offset=60, y_offset=50):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index == 0:
                    alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien('green', x, y)
                else:
                    alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite) # type: ignore

    def change_direction(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
                self.change_y(2)
            if alien.rect.left <= 0:
                self.alien_direction = 1
                self.change_y(2)

    def change_y(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shooting(self):
        if self.aliens:
            alien = random.choice(self.aliens.sprites())
            projectile = Projectile(alien, (241, 79, 80),
                                    alien.rect.midbottom, speed=12)
            self.alien_projectiles.add(projectile) # type: ignore

    def mothership_timeout(self):
        self.mothership_spawn_time -= 1
        if self.mothership_spawn_time == 0:
            self.mother.add(Mothership(random.choice(['right', 'left']),# type: ignore
                                       screen_width))

    def collision(self):
        if self.player.sprite.projectiles:
            for projectile in self.player.sprite.projectiles:
                if pygame.sprite.spritecollide(projectile, self.blocks, True):
                    projectile.kill()

                alien_hit = pygame.sprite.spritecollide(projectile, self.aliens, True)
                if alien_hit:
                    for alien in self.aliens:
                        if alien in alien_hit:
                            self.score += alien.value
                    projectile.kill()

                if pygame.sprite.spritecollide(projectile, self.mother, True):
                    projectile.kill()

        if self.alien_projectiles:
            for projectile in self.alien_projectiles:
                if pygame.sprite.spritecollide(projectile, self.blocks, True):
                    projectile.kill()

                if pygame.sprite.spritecollide(projectile, self.player, False):
                    projectile.kill()
                    self.player.hitpoints -= 1
                    if self.player.hitpoints <= 0:
                        self.player.kill()

        if self.aliens:
            for alien in self.aliens.sprites():
                if pygame.sprite.spritecollide(alien, self.player, True):
                    pygame.quit()

    def run(self):
        # update all sprites
        self.player.update()
        self.aliens.update(self.alien_direction)
        self.alien_projectiles.update()
        self.change_direction()
        self.mothership_timeout()
        self.mother.update()
        self.collision()

        # draw all sprites
        self.player.sprite.projectiles.draw(screen)
        self.alien_projectiles.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.mother.draw(screen)

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    fps = 60
    game = Game()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == ALIENLASER:
                game.alien_shooting()

        screen.fill((0, 0, 0))
        game.run()
        pygame.display.flip()
        clock.tick(fps)