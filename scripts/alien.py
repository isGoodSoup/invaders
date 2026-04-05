import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        path = f"assets/{color}.png"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.values = {'red': 100, 'green': 200, 'yellow': 300}
        self.value = self.values.get(color)

    def update(self, direction):
        self.rect.x += direction

class Mothership(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()
        path = f"assets/extra.png"
        self.image = pygame.image.load(path)
        if side == "right":
            x = screen_width + 50
            self.speed = -5
        else:
            x = -50
            self.speed = 5
        self.rect = self.image.get_rect(topleft=(x,80))

    def update(self):
        self.rect.x += self.speed
