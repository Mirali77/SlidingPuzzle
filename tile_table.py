import init
from tile import *


class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in Singleton.__instance:
            Singleton.__instance[cls] = cls.__new__(cls)
            Singleton.__instance[cls].__init__(*args, **kwargs)
        return Singleton.__instance[cls]


class TileTable(metaclass=Singleton):
    def __init__(self):
        self.table = []
        for idx1 in range(4):
            four_tiles = []
            for idx2 in range(4):
                four_tiles.append(Tile(init.all_sprites, idx1 * 4 + idx2))
                four_tiles[idx2].set_place(((idx2 + 1) * 280, (idx1 + 1) * 140))
            self.table.append(four_tiles)
        self.clicked_tile = []
        self.void_tile = (0, 0)

    def clear(self):
        for idx1 in range(4):
            for idx2 in range(4):
                self.table[idx1][idx2].kill()
        self.table.clear()

    def repair(self):
        for idx1 in range(4):
            four_tiles = []
            for idx2 in range(4):
                four_tiles.append(Tile(init.all_sprites, idx1 * 4 + idx2))
                four_tiles[idx2].set_place(((idx2 + 1) * 280, (idx1 + 1) * 140))
            self.table.append(four_tiles)
        self.clicked_tile = []
        self.void_tile = (0, 0)
        self.shuffle()

    def shuffle(self):
        for times in range(4):
            for idx1 in range(4):
                for idx2 in range(4):
                    pos1 = random.randint(0, 3)
                    pos2 = random.randint(0, 3)
                    if (pos1, pos2) == self.void_tile:
                        self.void_tile = (idx1, idx2)
                    elif (idx1, idx2) == self.void_tile:
                        self.void_tile = (pos1, pos2)
                    self.swap((idx1, idx2), (pos1, pos2))

    def check(self):
        for idx1 in range(4):
            for idx2 in range(4):
                if self.table[idx1][idx2].key != idx1 * 4 + idx2:
                    return False
        return True

    def swap(self, pos1, pos2):
        first_pos = self.table[pos1[0]][pos1[1]].place
        second_pos = self.table[pos2[0]][pos2[1]].place
        self.table[pos1[0]][pos1[1]].set_place(second_pos)
        self.table[pos2[0]][pos2[1]].set_place(first_pos)
        self.table[pos1[0]][pos1[1]], self.table[pos2[0]][pos2[1]] = self.table[pos2[0]][pos2[1]], self.table[pos1[0]][pos1[1]]

    def tile_clicked(self, click):
        if len(self.clicked_tile) == 0:
            for idx1 in range(4):
                for idx2 in range(4):
                    if self.table[idx1][idx2].rect.collidepoint(click.pos):
                        x = click.pos[0]
                        y = click.pos[1]
                        self.table[idx1][idx2].clicked = True
                        self.table[idx1][idx2].offset = (x - self.table[idx1][idx2].rect.x, y - self.table[idx1][idx2].rect.y)
                        self.clicked_tile.append((idx1, idx2))
            init.drag_flag = True

    def tile_unclicked(self):
        if len(self.clicked_tile) > 0:
            idx = self.clicked_tile[0]
            self.table[idx[0]][idx[1]].clicked = False
            if abs(idx[0] - self.void_tile[0]) == 1 and idx[1] == self.void_tile[1] or abs(idx[1] - self.void_tile[1]) == 1 and idx[0] == self.void_tile[0]:
                if init.rect_intersection(self.table[idx[0]][idx[1]].rect, self.table[self.void_tile[0]][self.void_tile[1]].rect):
                    self.table[idx[0]][idx[1]].rect.center = self.table[idx[0]][idx[1]].place
                    self.swap(idx, self.void_tile)
                    self.void_tile = idx
            else:
                self.table[idx[0]][idx[1]].rect.center = self.table[idx[0]][idx[1]].place
            self.clicked_tile.clear()
        init.drag_flag = False

    def tile_dragging(self):
        if len(self.clicked_tile) > 0:
            for idx in self.clicked_tile:
                if self.table[idx[0]][idx[1]].clicked:
                    pos = pygame.mouse.get_pos()
                    self.table[idx[0]][idx[1]].rect.x = pos[0] - self.table[idx[0]][idx[1]].offset[0]
                    self.table[idx[0]][idx[1]].rect.y = pos[1] - self.table[idx[0]][idx[1]].offset[1]
