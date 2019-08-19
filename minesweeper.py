#!/usr/bin/env python3

import numpy as np
import sys


class Board:

    def __init__(self, n_rows=10, n_cols=10, n_mines=10):
        self.num_rows = n_rows
        self.num_cols = n_cols
        self.num_mines = n_mines
        self.size = n_rows * n_cols
        self.board = np.zeros(self.size)
        self.board[np.random.choice(self.size, self.num_mines, replace=False)] = 1.0
        self.board = self.board.reshape((self.num_rows, self.num_cols))


class Tile:

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) == 4:
        num_rows = int(sys.argv[1])
        num_cols = int(sys.argv[2])
        num_mines = int(sys.argv[3])
        b = Board(num_rows, num_cols, num_mines)
    else:
        b = Board()
    print(b.board)
    var = input('Choose a tile in (row, col) format: ')
    print(f'You entered {var}')
    # print('Hi Beth')

