#!/usr/bin/env python3

#from termcolor import colored
#import copy
import sys
import os

sys.setrecursionlimit(5000)

input_template = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
# x, y different lengths possible

puzzle_input = [
        [[2], [4], [2], [2, 2], [1]],
        [[4], [4], [2], [1, 1], [1]]
        ]

len_puzzle_input_0 = len(puzzle_input[0])
len_puzzle_input_1 = len(puzzle_input[1])

puzzle_grid = []
for i in range(0, len(puzzle_input[1]) + 1):
    tmp = []
    for j in range(0, len(puzzle_input[0]) + 1):
        tmp.append(0)
    puzzle_grid.append(tmp)

#puzzle_grid = [
#        [1,0,0,0,0,0],
#        [1,1,0,0,1,0],
#        [1,0,0,0,1,0],
#        [1,0,1,1,1,0],
#        [0,0,1,1,1,0],
#        [0,0,0,0,0,0]]
initial_limit = 0

def print_grid():
    y_len = 0
    x_len = 0
    for i in range(0, len_puzzle_input_0):
        if len(puzzle_input[0][i]) > x_len:
            x_len = len(puzzle_input[0][i])
    for i in range(0, len_puzzle_input_1):
        if len(puzzle_input[1][i]) > y_len:
            y_len = len(puzzle_input[1][i])
    for x in range(0, x_len):
        for y in range(0, y_len):
            print(" ", end="")
        print("|", end="")
        for i in range(0, len_puzzle_input_0):
            if len(puzzle_input[0][i]) < x_len - x:
                print(" ", end="")
            else:
                print(puzzle_input[0][i][x - x_len + len(puzzle_input[0][i])], end="")
        print("")
    for i in range(0, y_len):
        print("-", end="")
    print("/", end="")
    for i in range(0, len_puzzle_input_0):
        print("-", end="")
    print("")
    for i in range(0, len_puzzle_input_1):
        for y in range(0, y_len):
            if len(puzzle_input[1][i]) < y_len - y:
                print(" ", end="")
            else:
                print(puzzle_input[1][i][y - y_len + len(puzzle_input[1][i])],
                        end = "")
        print("|", end="")
        for j in range(0, len(puzzle_grid[i]) - 1):
            print(puzzle_grid[i][j], end="")
        print("")
    print("")

def check_correct():
    for y in range(0, len_puzzle_input_1):
        count = 0
        i = 0
        for x in range(0, len_puzzle_input_0 + 1):
      #      print("Row:")
       #     print("x,y =", x+1, y+1)
     #       print("val =", puzzle_grid[y][x])
            if puzzle_grid[y][x] == 1:
                count += 1
            elif puzzle_grid[y][x - 1] == 1:
    #            print("prev =", puzzle_grid[y][x - 1])
                if i >= len(puzzle_input[1][y]):
   #                 print("c,i =", count, i)
                    if count > 0:
                        return False
                else:
                    if count == puzzle_input[1][y][i]:
                        i += 1
                        count = 0
                    else:
                        return False
  #          print("c =", count)
 #           print("i =", i)
 #           print("")
        if i < len(puzzle_input[1][y]):
            return False

    for x in range(0, len_puzzle_input_0):
        count = 0
        i = 0
        for y in range(0, len_puzzle_input_1 + 1):
#            print("Column:")
#            print("x,y =", x+1, y+1)
#            print("val =", puzzle_grid[y][x])
            if puzzle_grid[y][x] == 1:
                count += 1
            elif puzzle_grid[y - 1][x] == 1:
#                print("prev =", puzzle_grid[y - 1][x])
                if i >= len(puzzle_input[0][x]):
#                    print("c,i =", count, i)
                    if count > 0:
                        return False
                else:
                    if count == puzzle_input[0][x][i]:
                        i += 1
                        count = 0
                    else:
                        return False
#            print("c =", count)
#            print("i =", i)
#            print("")
#        print("c,i =", count, i)
        if i < len(puzzle_input[0][x]):
            return False
    return True

last = (len(puzzle_grid[0]) - 1) * (len(puzzle_grid) - 1)
lookup_position = []

for place in range(0, last):
    r = int((place - place % (len(puzzle_grid) - 1))/(len(puzzle_grid) - 1))
    c = place % (len(puzzle_grid[0]) - 1)
    lookup_position.append([r, c])

def recursion(limit, puzzle_grid):
    global last
    place = last - 1;
    while place >= limit:
        for i in range(place, last):
            r = lookup_position[place][0]
            c = lookup_position[place][1]
            #print("")
            #print("r,c =", r+1, c+1)
            if puzzle_grid[r][c] == 0:
                puzzle_grid[r][c] = 1
                #if place <= 5:
                #    print_grid()
                place = last - 1
                break
            else:
                puzzle_grid[r][c] = 0
                place -= 1
        need_check = True
        for i in range(0, len_puzzle_input_1):
            if need_check:
                if sum(puzzle_grid[i]) != sum(puzzle_input[1][i]):
                    need_check = False
        if need_check:
            if check_correct():
                print_grid()
                sys.exit()

# Main
print_grid()
recursion(initial_limit, puzzle_grid)

if found == False:
    print("No solutions found")
