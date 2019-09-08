
class Spreadsheet:

    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.data = [[''] * n_cols for _ in range(n_rows)]

    def update_val(self, row, col, new_val):
        self.data[row][col] = new_val

    def display_sheet(self):
        for row in range(self.n_rows):
            print('|'.join(self.data[row]))

    def display_pretty(self):
        max_lens = [-1] * self.n_cols
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                val = self.data[row][col]
                len_val = len(val)
                if len_val > max_lens[col]:
                    max_lens[col] = len_val
        return max_lens


if __name__ == '__main__':

    s = Spreadsheet(4, 3)
    s.update_val(0, 0, 'bob')
    s.update_val(0, 1, '10')
    s.update_val(0, 2, 'foo')
    s.update_val(1, 0, 'alice')
    s.update_val(1, 1, '5')
    s.display_sheet()
    print(s.display_pretty())

