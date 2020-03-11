#!/usr/bin/env python3

#from termcolor import colored
#import copy
import sys

sys.setrecursionlimit(5000)

input_template = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
# x, y different lengths possible

puzzle_input = [
        [[2], [1], [3], [3], [3, 1]],
        [[2], [3], [3], [3], [1, 1]]
        ]

puzzle_grid = []
for i in range(0, len(puzzle_input[1]) + 1):
    tmp = []
    for j in range(0, len(puzzle_input[0]) + 1):
        tmp.append(0)
    puzzle_grid.append(tmp)

#puzzle_grid = [
#        [0,0,0,1,1,0],
#        [0,0,1,1,1,0], 
#        [0,0,1,1,1,0], 
#        [1,1,1,0,0,0],
#        [1,0,0,0,1,0],
#        [0,0,0,0,0,0]]

def print_grid():
    y_len = 0
    x_len = 0
    for i in range(0, len(puzzle_input[0])):
        if len(puzzle_input[0][i]) > x_len:
            x_len = len(puzzle_input[0][i])
    for i in range(0, len(puzzle_input[1])):
        if len(puzzle_input[1][i]) > y_len:
            y_len = len(puzzle_input[1][i])
    for x in range(0, x_len):
        for y in range(0, y_len):
            print(" ", end="")
        print("|", end="")
        for i in range(0, len(puzzle_input[0])):
            if len(puzzle_input[0][i]) < x_len - x:
                print(" ", end="")
            else:
                print(puzzle_input[0][i][x - x_len + len(puzzle_input[0][i])], end="")
        print("")
    for i in range(0, y_len):
        print("-", end="")
    print("/", end="")
    for i in range(0, len(puzzle_input[0])):
        print("-", end="")
    print("")
    for i in range(0, len(puzzle_input[1])):
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
    for y in range(0, len(puzzle_input[1])):
        count = 0
        i = 0
        for x in range(0, len(puzzle_input[0]) + 1):
#            print("Row:")
#            print("x,y =", x+1, y+1)
#            print("val =", puzzle_grid[y][x])
            if puzzle_grid[y][x] == 1:
                count += 1
            elif puzzle_grid[y][x - 1] == 1:
#                print("prev =", puzzle_grid[y][x - 1])
                if i >= len(puzzle_input[1][y]):
#                    print("c,i =", count, i)
                    if count > 0:
                        return False
                else:
                    if count == puzzle_input[1][y][i]:
                        i += 1
                        count = 0
                    else:
                        return False
#            print("c =", count)
#            print("i =", i)
#            print("")
        if i < len(puzzle_input[0][y]):
            return False

    for x in range(0, len(puzzle_input[0])):
        count = 0
        i = 0
        for y in range(0, len(puzzle_input[1]) + 1):
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
        if i < len(puzzle_input[1][x]):
            return False
    return True

grid_size = (len(puzzle_grid[0]) - 1) * (len(puzzle_grid) - 1)
size_count = 0
start = 0
found = False

def recursion_old():
    global size_count, start, puzzle_grid, found
    print_grid()
    if size_count == grid_size:
        if check_correct():
            print_grid()
            if found == False:
                found = True
        else:
            start += 1
            if start > grid_size:
                if found == False:
                    print("No solutions found")
                sys.exit()
            size_count = start
            print("Size_count =", size_count)
            puzzle_grid = []
            for i in range(0, len(puzzle_input[1]) + 1):
                tmp = []
                for j in range(0, len(puzzle_input[0]) + 1):
                    tmp.append(0)
                puzzle_grid.append(tmp)
            recursion()
    else:
        puzzle_grid[int((size_count - size_count % (len(puzzle_grid) - 1))/ 
            (len(puzzle_grid) - 1))][size_count % (len(puzzle_grid[0]) - 
                1)] = 1
        size_count += 1;
        recursion()
       # puzzle_grid[int((size_count - 1 - (size_count - 1) % (len(puzzle_grid) - 
        #    1))/(len(puzzle_grid) - 1))][(size_count - 1) % (len(puzzle_grid[0]) 
         #       - 1)] = 0
       # recursion()

last = (len(puzzle_grid[0]) - 1) * (len(puzzle_grid) - 1)
initial_limit = 0

def recursion(limit):
    global last
    place = last - 1;
    while place >= limit:
        for i in range(place, last):
            r = int((place - place % (len(puzzle_grid) - 1))/(len(puzzle_grid) - 1))
            c = place % (len(puzzle_grid[0]) - 1)
            #print("")
            #print("r,c =", r+1, c+1)
            if puzzle_grid[r][c] == 0:
                puzzle_grid[r][c] = 1
                place = last - 1
                #print_grid()
                break
            else:
                puzzle_grid[r][c] = 0
                place -= 1
        if check_correct():
            print_grid()

# Main
print_grid()
recursion(initial_limit)

if found == False:
    print("No solutions found")
