import pygame
from pprint import pprint
from pygame.locals import (
    KEYDOWN,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    MOUSEMOTION,
    QUIT,
    K_ESCAPE
)
from board import Board
from Pieces import Pieces
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption(('Chess'))

running = True

board = Board(win)
board.draw_board()
piece1 = Pieces(*board.boxes[0].center,'B',0,0,board)
piece2 = Pieces(*board.boxes[1].center,'W',1,0,board)
board.boards[0][0] = [1,piece1]
board.boards[1][0] = [1,piece2]
all_pieces = pygame.sprite.Group()
all_pieces.add(piece1)
all_pieces.add(piece2)

while running:
    for event in pygame.event.get():
        all_pieces.update(event)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False


    win.fill((0,0,0))
    board.draw_board()
    
    # Draw all sprites
    for entity in all_pieces:
        win.blit(entity.surf, entity.rect)
    # win.blit(piece1.surf,piece1.rect)
    # win.blit(piece2.surf,piece2.rect)
    pygame.display.flip()
    
pygame.quit()
