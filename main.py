
import pygame
from constant import SQUARE_SIZE, BLACK, WHITE, WIDTH, random_img, BOARDB, WIN, FPS, restart_img, BOARDA, HEIGHT, GREEN, PADDING, easy_img, medium_img, hard_img
from game import Game
from algorithm import minimax
from button import Button
from menu import Menu

pygame.display.set_caption('Checkers VS AI')

random_button = Button(PADDING, WIDTH, random_img)
restart_button = Button(PADDING, WIDTH+SQUARE_SIZE, restart_img)
easy_button = Button(200, 500, easy_img)
medium_button = Button(200, 550, medium_img)
hard_button = Button(200, 600, hard_img)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    main_menu = Menu(WIN)
    start_button = Button(WIDTH//2-SQUARE_SIZE-20, HEIGHT//2, main_menu.getText())
    
    start_game = False
    depth = 3
    level = 'Medium'

    while run:
        clock.tick(FPS)
        
        # level text        
        pygame.init()
        font = pygame.font.Font('freesansbold.ttf', 20)
        textLevel = font.render('Level :'+ level, True, BOARDA)

        if start_game == False:
            WIN.fill(GREEN)
            if start_button.draw(WIN):
                game = Game(WIN, False)
                start_game = True
        else:
            WIN.fill(BOARDB)
            exit_button = Button(WIDTH//2+SQUARE_SIZE, WIDTH+(SQUARE_SIZE+PADDING)*2, game.get_text_exit())
            WIN.blit(textLevel, (PADDING, WIDTH+(SQUARE_SIZE+PADDING)*2))

            if random_button.draw(WIN):
                game = Game(WIN, True)

            if restart_button.draw(WIN):
                game = Game(WIN, False) 
            
            if easy_button.draw(WIN):
                game = Game(WIN, False)
                level = 'Easy'
                print('Easy')
                depth = 1
        
            if medium_button.draw(WIN):
                game = Game(WIN, False)
                level = 'Medium'
                print('Medium')
                depth = 3

            if hard_button.draw(WIN):
                game = Game(WIN, False)
                level = 'Hard'
                print('Hard')
                depth = 4
            
            if exit_button.draw(WIN):
                start_game = False
            
            if game.turn == WHITE:
                value, new_board = minimax(game.get_board(), depth, WHITE, game)
                game.ai_move(new_board)

            if game.winner() != None:
                print(game.winner())
                run = False                 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if start_game==True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    # print(row, col)
                    if(row < 8):
                        game.select(row, col)
                    # game.select(row, col)

        if start_game == False:
            main_menu.update()
        else:
            game.update()
    
    pygame.quit()

main()