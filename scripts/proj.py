import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, sprite, color, pos, speed=-12):
        super().__init__()
        self.image = pygame.Surface([4, 20], pygame.SRCALPHA)
        self.image.fill((*color, 255))
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.kill()