import pygame
from game import Game
from menu import *
from algorithm import minimax
from constant import WIDTH, HEIGHT, SQUARE_SIZE, BLACK, WHITE

FPS= 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def get_row_col_from_mouse(pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

class GameMenu():
    def __init__(self, win):
        pygame.init()
        self.win = win
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 700, 700
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'assets/8-BIT WONDER.TTF'
        self.PURPLE, self.WHITE = (10,3,11), (255, 255, 255)
        self.main_menu = MainMenu(self, self.win)
        self.options = OptionsMenu(self, self.win)
        self.credits = CreditsMenu(self, self.win)
        self.curr_menu = self.main_menu

    def get_run_main(self):
        return self.main_menu.get_play()

    def game_loop(self):
        clock = pygame.time.Clock()
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False

            while run:
                run = True
                clock = pygame.time.Clock()
                game = Game(WIN)
                
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
                        game.select(row, col)

                game.update()

            self.display.fill(self.BLACK)
            self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
            if self.get_run_main() == True:
                self.playing = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)




