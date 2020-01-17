import numpy as np


class Spreadsheet:

    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = [[''] * num_cols for _ in range(num_rows)]

    def update_val(self, val, n_row, n_col):
        self.data[n_row][n_col] = val

    def display_sheet(self):
        for row in range(self.num_rows):
            print('|'.join(self.data[row]))

    def display_pretty_sheet(self):
        maxx = self.get_max_col_widths()
        for row in range(self.num_rows):
            to_print = ''
            for col in range(self.num_cols):
                value = self.data[row][col]
                if col != self.num_cols - 1:
                    to_print += value.ljust(maxx[col]) + '|'
                else:
                    to_print += value.ljust(maxx[col])
            print(to_print)

    def get_max_col_widths(self):
        maxx = [-1] * self.num_cols
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                widdth = len(self.data[row][col])
                maxx[col] = np.max([widdth, maxx[col]])
        return maxx

    def sum_formulas(self, input_str):
        start_coords = input_str.split('-')[0]
        start_row = int(start_coords.split(',')[0]) - 1
        start_col = int(start_coords.split(',')[1]) - 1

        end_coords = input_str.split('-')[1]
        end_row = int(end_coords.split(',')[0]) - 1
        end_col = int(end_coords.split(',')[1]) - 1

        summ = 0
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                value = self.data[row][col]
                if value.isdigit():
                    summ += int(value)

        return summ


sheet = Spreadsheet(num_rows=4, num_cols=3)
sheet.update_val('bob', 0, 0)
sheet.update_val('10', 0, 1)
sheet.update_val('foo', 0, 2)
sheet.update_val('alice', 1, 0)
sheet.update_val('5', 1, 1)

# sheet.display_sheet()
# sheet.get_max_col_widths()
sheet.display_pretty_sheet()

# sheet.sum_formulas('1,1-2,2')





