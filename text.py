import init
from init import *


class Text:
    def __init__(self, size: int, place_cord, message_str: str, colour):
        self.font = pygame.font.Font(None, size)
        self.message = self.font.render(message_str, True, colour)
        self.rect = self.message.get_rect(center=place_cord)
        self.text = message_str
        self.place_cord = place_cord

    def draw(self):
        init.screen.blit(self.message, self.rect)

    def set_message(self, message_str):
        self.message = self.font.render(message_str, True, init.BLACK)
        self.rect = self.message.get_rect(center=self.place_cord)
        self.text = message_str