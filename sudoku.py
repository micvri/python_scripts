#!/usr/bin/env python3

from termcolor import colored
import copy
import sys

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

def check_errors(sudoku):
    for r in range(0,9):
        for c in range(0,9):
            i = sudoku[r][c]
            if i != 0:
                for col in range(0,9):
                    if col != c:
                        if sudoku[r][col] == i:
                            print(colored("Error", "red"))
                            print(i, "In", r, c,"found in col", r, col)
                            sys.exit()
                for row in range(0,9):
                    if row != r:
                        if sudoku[row][c] == i:
                            print(colored("Error", "red"))
                            print(i, "In", r, c, "found in row", row, c)
                            sys.exit()
                square_free = True
                ro, co = 0, 0
                if r in [1, 4, 7]:
                    ro=1
                if r in [2, 5, 8]:
                    ro=2
                if c in [1, 4, 7]:
                    co=1
                if c in [2, 5, 8]:
                    co=2
                for row in range(r,r+3):
                    for col in range(c,c+3):
                        if row-ro != r:
                            if col-co != c:
                                if sudoku[row-ro][col-co] == i:
                                    print(colored("Error", "red"))
                                    print(i, "In", r, c, "found in box", row-ro, col-co)
                                    sys.exit()

def recursion(sudoku, row, col):
        temp = check(sudoku, row, col)
        if temp != 0:
            sudoku[row][col] = temp
            prev.append([row,col])
#            print_sudoku(sudoku)
        else:
            sudoku[row][col] = temp
            length = int (len(prev)-1)
            if length < 0:
                print("Number of solutions:", count)
                sys.exit()
#            print(prev)
#            print_sudoku(sudoku)
            tmp = prev[length]
            prev.remove(tmp)
            recursion(sudoku, tmp[0], tmp[1])
            recursion(sudoku, row, col)


# Main
print_sudoku(sudoku_input)

count = 0

check_errors(sudoku_input)

for row in range(0,9):
    for col in range(0,9):
        if sudoku_input[row][col] == 0:
            recursion(sudoku_input, row, col)
            last = [row, col]
#            print_sudoku(sudoku_input)

count+=1

print_sudoku(sudoku_input)
while True:
#    print(last)
    prev.remove(last)
    recursion(sudoku_input, last[0], last[1])
    print_sudoku(sudoku_input)
    count+=1

print("Number of solutions:", count)
