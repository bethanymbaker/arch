import numpy as np


def is_game_finished(bord):
    to_test = [
        bord[0],
        bord[1],
        bord[2],
        [bord[0][0], bord[1][0], bord[2][0]],
        [bord[0][1], bord[1][1], bord[2][1]],
        [bord[0][2], bord[1][2], bord[2][2]],
        [bord[0][0], bord[1][1], bord[2][2]],
        [bord[0][2], bord[1][1], bord[2][0]]
    ]
    for row in to_test:
        if (row == [False, False, False]) | (row == [True, True, True]):
            return True
    for row in bord:
        for col in row:
            if col == '':
                return False
    return True


all_boards = set()
for game in range(50000):
    board = [['', '', ''] for i in range(3)]
    all_boards.add(str(board))

    flag = bool(np.random.randint(2))

    while not is_game_finished(board):
        switch_turn = False
        while not switch_turn:
            move = np.random.randint(9)
            row_num = move // 3
            col_num = move % 3
            if board[row_num][col_num] == '':
                board[row_num][col_num] = flag
                flag = not flag
                switch_turn = True
                all_boards.add(str(board))

print(f'num sets = {len(all_boards)}')
