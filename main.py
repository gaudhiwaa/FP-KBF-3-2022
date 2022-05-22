# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from constant import SQUARE_SIZE, BLACK, WHITE, WIDTH, random_img, BOARDB, WIN, FPS, restart_img
from game import Game
from algorithm import minimax
from button import Button

pygame.display.set_caption('Checkers VS AI')

random_button = Button(0, WIDTH, random_img)
restart_button = Button(0, WIDTH+SQUARE_SIZE, restart_img)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN, False)

    while run:
        clock.tick(FPS)
        WIN.fill(BOARDB)
        
        if random_button.draw(WIN):
            game = Game(WIN, True)

        if restart_button.draw(WIN):
            game = Game(WIN, False)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
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
                # print(row, col)
                if(row < 8):
                    game.select(row, col)
                # game.select(row, col)

        game.update()
    
    pygame.quit()

main()