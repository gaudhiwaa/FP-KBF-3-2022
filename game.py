import pygame
from constant import BLACK, WHITE, GREEN, SQUARE_SIZE, WIDTH, HEIGHT, BOARDA
from board import Board, Piece

class Game:
    def __init__(self, win, set_random):
        self._init(set_random)
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
        # Piece.check_king(Piece)

    def _init(self, set_random):
        self.selected = None
        self.board = Board(set_random)
        self.turn = BLACK
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()

    def text_exit(self):
        pygame.init()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.textExit = self.font.render('Main Menu', True, BOARDA)
        self.textRect = self.textExit.get_rect()
        self.textRect.center = (0, WIDTH+SQUARE_SIZE)
    
    def get_text_exit(self):
        self.text_exit()
        return self.textExit