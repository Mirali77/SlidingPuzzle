import init
from init import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, group: pygame.sprite.Group, key: int):
        pygame.sprite.Sprite.__init__(self)
        self.key = key
        self.image = pygame.transform.scale(init.images[key], (280, 140))
        self.rect = self.image.get_rect()
        self.add(group)
        self.clicked = False
        self.offset = (0, 0)
        self.place = self.rect.center

    def set_place(self, place):
        self.place = place
        self.rect.center = place
