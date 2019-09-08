import numpy as np

def is_game_finished(board):
    res = False
    for row in board:
        if (row == [False, False, False]) | (row == [True, True, True]):
            return True
    transposed = [[board[0][0], board[1][0], board[2][0]],
                  [board[0][1], board[1][1], board[2][1]],
                  [board[0][2], board[1][2], board[2][2]]]
    for row in transposed:
        if (row == [False, False, False]) | (row == [True, True, True]):
            return True
    for row in board:
        for col in row:
            if col == '':
                return False
    return True


all_boards = set()
for game in range(250000):
    board = [['', '', ''] for i in range(3)]

    flag = True
    kount = 1
    all_boards.add(str(board))

    while not is_game_finished(board):
        switch = False
        while not switch:
            move = np.random.randint(9)
            row_num = move // 3
            col_num = move % 3
            if board[row_num][col_num] == '':
                board[row_num][col_num] = flag
                flag = not flag
            kount += 1
            all_boards.add(str(board))
            switch = True
