import pygame
from constant import WIDTH, HEIGHT
# from board import set_random, get_random

class Button():
    def __init__(self, x, y, image):
        # print("random!!!!")
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, win):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                # print(action)
                # print('CLICKED')
                # set_random(True)
                # get_random

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        win.blit(self.image, (self.rect.x, self.rect.y))
        # print(action)
        return action