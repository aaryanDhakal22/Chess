
import pygame
from pygame.locals import (
    KEYDOWN,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    MOUSEMOTION,
    QUIT,
    K_ESCAPE
)
class Pieces(pygame.sprite.Sprite):

    def __init__(self,x,y,color,stackr,stackc,board):
        super(Pieces,self).__init__()
        # self.surf = pygame.Surface((40,40))
        # self.color = color
        # if self.color == 'B':
        #     self.surf.fill((255,0,0))
        # else:
        #     self.surf.fill((0,255,255))
        # self.rect = self.surf.get_rect(center = (x,y))
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.stack = [[stackr,stackc]]
        self.dead = False
        self.board = board

    def __repr__(self):
        return self.color

    def move(self):
        print(self.dest_row,self.dest_col)
        self.board.boards[self.dest_row][self.dest_col] = [1,self]
        self.rect.centerx,self.rect.centery = self.board.boxes[self.dest_rect_pos].center
        self.stack.append([self.dest_row,self.dest_col])
        if len(self.stack) >1:
            self.old_row ,self.old_col = self.stack.pop(0)
            self.board.boards[self.old_row][self.old_col] = [0,0]

    def die(self):
        self.dead = True
        self.kill()
        if len(self.stack) > 0 :
            self.old_row ,self.old_col = self.stack.pop(0)
            self.board.boards[self.old_row][self.old_col] = [0,0]
        

    def update(self,event):
        if not self.dead:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.old_pos = (self.rect.x,self.rect.y)
                    if self.rect.collidepoint(event.pos):
                        self.dragging = True
                        mouse_x ,mouse_y = event.pos
                        self.offset_x = self.rect.x - mouse_x
                        self.offset_y = self.rect.y - mouse_y

            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:            
                    self.dragging = False
                    self.dest_rect_pos = self.rect.collidelist(self.board.board_view)
                    if self.dest_rect_pos != -1:
                        self.dest_row = self.dest_rect_pos%8
                        self.dest_col = self.dest_rect_pos//8

                        if not self.board.board_view[self.dest_row][self.dest_col][0] :
                            print("hi")
                            self.move()

                        elif self.color != self.board.boards[self.dest_row][self.dest_col][1].color:
                            print("hi fff")
                            self.board.boards[self.dest_row][self.dest_col][1].die()
                            self.move()
                        else:
                            print("hi im in else")
                            self.rect.x ,self.rect.y = self.old_pos
                    else:
                        print("hi im in else")
                        self.rect.x ,self.rect.y = self.old_pos

            elif event.type == MOUSEMOTION:
                if self.dragging:
                    mouse_x, mouse_y = event.pos
                    self.rect.x = mouse_x + self.offset_x
                    self.rect.y = mouse_y + self.offset_y
            print(self.board.boards)