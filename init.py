import pygame
import random
from tile_table import TileTable
from text import Text

WIDTH = 1400  # ширина игрового окна
HEIGHT = 700  # высота игрового окна
FPS = 30  # частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
images = [pygame.image.load('1.png').convert_alpha(), pygame.image.load('2.png').convert_alpha(),
          pygame.image.load('3.png').convert_alpha(), pygame.image.load('4.png').convert_alpha(),
          pygame.image.load('5.png').convert_alpha(), pygame.image.load('6.png').convert_alpha(),
          pygame.image.load('7.png').convert_alpha(), pygame.image.load('8.png').convert_alpha(),
          pygame.image.load('9.png').convert_alpha(), pygame.image.load('10.png').convert_alpha(),
          pygame.image.load('11.png').convert_alpha(), pygame.image.load('12.png').convert_alpha(),
          pygame.image.load('13.png').convert_alpha(), pygame.image.load('14.png').convert_alpha(),
          pygame.image.load('15.png').convert_alpha(), pygame.image.load('16.png').convert_alpha()]
all_sprites = pygame.sprite.Group()
tile_table = TileTable()
tile_table.shuffle()


def is_point_in_rect(rect: pygame.Rect, point):
    return rect.x < point[0] < rect.x + rect.width and rect.y < point[1] < rect.y + rect.height


def rect_intersection(rect1: pygame.Rect, rect2: pygame.Rect):
    point1 = (rect1.x, rect1.y)
    point2 = (rect1.x + rect1.width, rect1.y)
    point3 = (rect1.x, rect1.y + rect1.height)
    point4 = (rect1.x + rect1.width, rect1.y + rect1.height)
    return is_point_in_rect(rect2, point1) or is_point_in_rect(rect2, point2) or \
           is_point_in_rect(rect2, point3) or is_point_in_rect(rect2, point4)


drag_flag = False
game = True

gio_message = Text(54, (WIDTH / 2, HEIGHT / 2 - 30), "GAME IS OVER", BLACK)
pa_message = Text(36, (WIDTH / 2, HEIGHT / 2 + 10), "Play again?", BLACK)
yes_message = Text(36, (WIDTH / 2 - 40, HEIGHT / 2 + 50), "YES", BLACK)
no_message = Text(36, (WIDTH / 2 + 40, HEIGHT / 2 + 50), "NO", BLACK)