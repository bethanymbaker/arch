import numpy as np


class Game:

    def __init__(self, num_rows, num_cols, frac_mines=0.1):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.mines = np.random.choice(num_rows * num_cols,
                                      int(frac_mines * num_cols * num_rows),
                                      replace=False)
        self.tiles = [[''] * num_cols for _ in range(num_rows)]
        for nrow in range(num_rows):
            for ncol in range(num_cols):
                self.tiles[nrow][ncol] = Tile(nrow, ncol)
        for mine in self.mines:
            col_num = mine % num_cols
            row_num = mine // num_cols
            self.tiles[row_num][col_num].is_mine = True


class Tile:
    def __init__(self, row_num, col_num):
        self.row_num = row_num
        self.col_num = col_num
        self.is_visible = False
        self.is_mine = False

    def __repr__(self):
        if self.is_mine:
            return 'X'
        if self.is_visible:
            return '-'
        else:
            return '.'


game = Game(10, 10)
game.tiles
