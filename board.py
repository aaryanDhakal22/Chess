import pygame
from pygame.locals import RLEACCEL
from board_config import board

class Box(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Box,self).__init__()
        self.blockSize = 90
        self.rect = pygame.Rect((x*self.blockSize)+40, (y*self.blockSize)+40,self.blockSize, self.blockSize)
        self.row = x
        self.col = y
    
    def __hash__(self):
        return int(str(self.row)+str(self.col))

class Board(pygame.sprite.Sprite):

    def __init__(self):
        super(Board,self).__init__()

        # self.surf = pygame.image.load("asset/download.png").convert()
        # self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf_rect = self.surf.get_rect()

        # self.win = win
        self.board = board

        self.board_view = dict()

        for x in range(8):
            for y in range(8):
                # rect = pygame.Rect((x*blockSize)+40, (y*blockSize)+40,blockSize, blockSize)
                # rect.row , rect.col = x , y
                # rect.__repr__ = lambda self: (self.row,self.col)
                self.board_view.setdefault(Box(x,y),board[y][x])
        print(self.board_view)
        print("bo")

    # def draw_board(self):
    #     self.win.blit(self.surf, (35,35))

Board()