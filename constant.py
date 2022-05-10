import pygame

WIDTH, HEIGHT = 500, 700
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

BOARDA = (250, 232, 167)
BOARDB = (234, 172, 139)

WHITE = (255, 255, 255)

# gambar bidak gelap
BLACK = (229, 107, 111)

RED = (255, 0, 0)
GREEN = (255, 255, 255)

GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))

#level
easy_img = pygame.transform.scale(pygame.image.load('assets/sign.png'), (44, 25))
medium_img = pygame.transform.scale(pygame.image.load('assets/sign-2.png'), (44, 25))
hard_img = pygame.transform.scale(pygame.image.load('assets/sign-3.png'), (44, 25))