import numpy as np
from time import sleep


class Tetris:

    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = [[-1] * num_cols for _ in range(num_rows)]
        self.is_complete = False

    def display_board(self):
        for row in range(self.num_rows):
            print(self.board[row])

    def add_piece(self, piece='square'):
        self.is_complete = False
        if piece == 'square':
            self.board[0][0] = 0
            self.board[0][1] = 0
            self.board[1][0] = 0
            self.board[1][1] = 0

    def update_board(self):
        temp_board = [[-1] * self.num_cols for _ in range(self.num_rows)]
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.board[row][col] == '*':
                    temp_board[row][col] = '*'
        for row in range(self.num_rows - 1):
            for col in range(self.num_cols):
                if (self.board[row][col] == 0) & (self.board[row+1][col] != '*'):
                    temp_board[row+1][col] = 0
                # elif self.board[row+1][col] == '*':
                #     self.is_complete = True
        self.board = temp_board

    def check_board(self):
        if not self.is_complete:
            last_row = self.board[-1]
            if 0 in last_row:
                self.is_complete = True
                for row in range(self.num_rows):
                    for col in range(self.num_cols):
                        if self.board[row][col] == 0:
                            self.board[row][col] = '*'
        else:
            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    if self.board[row][col] == 0:
                        self.board[row][col] = '*'



tetris = Tetris(20, 10)
# tetris.board
tetris.add_piece()
tetris.display_board()
print('##################')

# for i in range(20):
# flag = tetris.is_complete
while not tetris.is_complete:
    sleep(250/1000)
    tetris.update_board()
    tetris.check_board()
    print(f'is_complete = {tetris.is_complete}')
    tetris.display_board()
    print('##################')

tetris.add_piece()
tetris.display_board()

while not tetris.is_complete:
    sleep(250/1000)
    tetris.update_board()
    tetris.check_board()
    print(f'is_complete = {tetris.is_complete}')
    tetris.display_board()
    print('##################')


# for row in range(tetris.num_rows):
#     print(tetris.board[row])
# # tetris.board[0]