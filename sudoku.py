#!/usr/bin/env python3

from termcolor import colored
import copy

input_template = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]


sudoku_input = [
        [4, 0, 0, 7, 0, 0, 0, 0, 6],
        [0, 2, 0, 0, 0, 8, 0, 4, 9],
        [0, 0, 9, 0, 0, 0, 0, 5, 1],
        [1, 0, 3, 0, 9, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [8, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 7],
        [0, 7, 2, 9, 5, 0, 0, 0, 4]
        ]

original = copy.deepcopy(sudoku_input)

prev = []

def print_sudoku(sudoku):
    for r in range(0,9):
        for c in range(0,9):
            if original[r][c] == 0:
                col = 'white'
            else:
                col = 'blue'
            print(colored(sudoku[r][c], col), end="")
        print("")
    print("")

def check(sudoku, x, y):
#    print("x, y = ", x,y)
    for i in range(sudoku[x][y]+1,10):
        col_free = True
        for col in range(0,9):
            if sudoku[x][col] == i:
                col_free = False
#                print(i," Found in col ", x, col)
                break
        row_free = True
        for row in range(0,9):
            if sudoku[row][y] == i:
                row_free = False
#                print(i," Found in row ", row, y)
                break
        square_free = True
        xt, yt = x, y
        if xt in [1, 4, 7]:
            xt-=1
        if xt in [2, 5, 8]:
            xt-=2
        if yt in [1, 4, 7]:
            yt-=1
        if yt in [2, 5, 8]:
            yt-=2
        for row in range(xt,xt+3):
            for col in range(yt,yt+3):
                if sudoku[row][col] == i:
                    square_free = False
#                    print(i," Found in box ", row, col)
        if row_free & col_free & square_free:
            return i
    return 0

def recursion(sudoku, row, col):
        temp = check(sudoku, row, col)
        if temp != 0:
            sudoku[row][col] = temp
            prev.append([row,col])
#            print_sudoku(sudoku)
        else:
            sudoku[row][col] = temp
            length = int (len(prev)-1)
#            print(prev)
#            print_sudoku(sudoku)
            tmp = prev[length]
            prev.remove(tmp)
            recursion(sudoku, tmp[0], tmp[1])
            recursion(sudoku, row, col)


# Main
print_sudoku(sudoku_input)

for row in range(0,9):
    for col in range(0,9):
        if sudoku_input[row][col] == 0:
            recursion(sudoku_input, row, col)
            last = [row, col]
#            print_sudoku(sudoku_input)



print_sudoku(sudoku_input)
