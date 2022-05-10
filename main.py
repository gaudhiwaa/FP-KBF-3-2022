# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from constant import WIDTH, HEIGHT, SQUARE_SIZE, BLACK, WHITE, BOARDB, easy_img, medium_img, hard_img
from game import Game
from algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers VS AI')

# easy_img = pygame.image.load('assets/sign.png').convert_alpha()
# medium_img = pygame.image.load('assets/sign-2.png').convert_alpha()
# hard_img = pygame.image.load('assets/sign-3.png').convert_alpha()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                # print(action)
                # print('CLICKED')

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        WIN.blit(self.image, (self.rect.x, self.rect.y))
        # print(action)
        return action

easy_button = Button(0, 500, easy_img)
medium_button = Button(0, 550, medium_img)
hard_button = Button(0, 600, hard_img)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    depth = 1

    while run:
        clock.tick(FPS)
        WIN.fill(BOARDB)
        print(depth)

        if easy_button.draw():
            print('Easy')
            depth = 1
        
        if medium_button.draw():
            print('Medium')
            depth = 3

        if hard_button.draw():
            print('Hard')
            depth = 4

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), depth, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                print(row, col)
                if(row < 8):
                    game.select(row, col)

        game.update()
    
    pygame.quit()

main()