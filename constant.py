import imghdr
import pygame

WIDTH, HEIGHT = 500, 700
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

BOARDA = (250, 232, 167)
BOARDB = (140, 125, 71)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (20, 255, 0)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (SQUARE_SIZE/2, SQUARE_SIZE/2))
random_img = pygame.transform.scale(pygame.image.load('assets/random.png'),(SQUARE_SIZE, SQUARE_SIZE))
restart_img = pygame.transform.scale(pygame.image.load('assets/restart.png'),(SQUARE_SIZE, SQUARE_SIZE))
easy_img = pygame.transform.scale(pygame.image.load('assets/sign.png'), (44, 25))
medium_img = pygame.transform.scale(pygame.image.load('assets/sign-2.png'), (44, 25))
hard_img = pygame.transform.scale(pygame.image.load('assets/sign-3.png'), (44, 25))