# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from pygame import mixer
from constant import WIDTH, BOARDA, SQUARE_SIZE, BOARDB, WHITE, FPS, WIN, PADDING, random_img, restart_img, easy_img, medium_img, hard_img
from game import Game
from gamemenu import GameMenu
from algorithm import minimax
from button import Button

pygame.display.set_caption('Checkers VS AI')

mixer.init()
mixer.music.load('assets/AthleticTheme.wav')
mixer.music.play(-1)

random_button = Button(PADDING, WIDTH, random_img)
restart_button = Button(PADDING, WIDTH+SQUARE_SIZE, restart_img)
easy_button = Button(100, 500, easy_img)
medium_button = Button(100, 550, medium_img)
hard_button = Button(100, 600, hard_img)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    play = False
    clock = pygame.time.Clock()
    gm = GameMenu(WIN)
    # game = Game(WIN)
    depth = 3
    level = 'Medium'

    while run:
        clock.tick(FPS)
        
         # level text        
        pygame.init()
        font = pygame.font.Font('assets/8-BIT WONDER.TTF', 16)
        textLevel = font.render('Level ' + level, True, BOARDA)
        textLevelEasy = font.render('Easy ', True, BOARDA)
        textLevelMedium = font.render('Medium ', True, BOARDA)
        textLevelHard = font.render('Hard ', True, BOARDA)

        # if gm.get_run_main() == False:
        if gm.playing == True:
            WIN.fill(BOARDB)

            if play == False:
                game = Game(WIN, False)
                play = True
                
            #exit_button = Button(WIDTH//2+SQUARE_SIZE, WIDTH+(SQUARE_SIZE+PADDING)*2, game.get_text_exit())
            #WIN.blit(textLevel, (PADDING, WIDTH+(SQUARE_SIZE+PADDING)*2)) 
            exit_button = Button(WIDTH//2+SQUARE_SIZE+40, WIDTH+(SQUARE_SIZE+PADDING)*2+30, game.get_text_exit())
            WIN.blit(textLevel, (WIDTH//2+SQUARE_SIZE-10, WIDTH+SQUARE_SIZE-60)) 
            WIN.blit(textLevelEasy, (155, 505))      
            WIN.blit(textLevelMedium, (155, 552)) 

            WIN.blit(textLevelHard, (155, 605))
            
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
                gm.playing = False

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
                    if(row < 8 and col<8):
                        game.select(row, col)

            game.update()

        if gm.playing == False:
            gm.curr_menu.display_menu()
        
        if gm.running == False:
            run =  False
    
    pygame.quit()

main()