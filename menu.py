
import pygame
from constant import HEIGHT, WIDTH, BOARDA

class Menu():
    def __init__(self, win):
        self.win = win   
        self.draw(self.win) 
    
    def draw(self, win):
        pygame.init()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('Start Game', True, BOARDA)
        self.textRect = self.text.get_rect()
        self.textRect.center = (WIDTH // 2, HEIGHT // 2)
    
    def update(self):
        self.draw(self.win)
        pygame.display.update()
    
    def getText(self):
        return self.text



