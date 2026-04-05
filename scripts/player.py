import pygame

from scripts.utils import now
from scripts.proj import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen_width, scale=4):
        super().__init__()
        self.image = pygame.image.load('assets/ship.png').convert_alpha()
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.width * scale,
                                             self.height * scale))
        self.rect = self.image.get_rect(midbottom=pos)
        self.screen_width = screen_width
        self.velocity = 4

        self.ready = True
        self.shot_time = 0
        self.shot_cooldown = 300

        self.projectiles = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right <= self.screen_width:
            self.rect.x += self.velocity
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot()
            self.ready = False
            self.shot_time = now()

    def shoot(self):
        self.projectiles.add(Projectile(self, (250, 220, 0), self.rect.center)) # type: ignore

    def recharge(self):
        if not self.ready:
            current_time = now()
            if current_time - self.shot_time >= self.shot_cooldown:
                self.ready = True

    def update(self):
        self.get_input()
        self.projectiles.update()
        self.recharge()