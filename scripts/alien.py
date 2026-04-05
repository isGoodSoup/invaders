import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        path = f"assets/{color}.png"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self, direction):
        self.rect.x += direction