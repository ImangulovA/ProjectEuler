#!/bin/python3

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20  grid?

import sys


grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)

maximum = 0
for i in range(20):
    for k in range(17):
        a,b,c,d = grid[i][k],grid[i][k+1],grid[i][k+2],grid[i][k+3]
        if 0 not in [a,b,c,d]:
            curma = a*b*c*d
            if maximum < curma:
                maximum = curma
        a,b,c,d = grid[k][i],grid[k+1][i],grid[k+2][i],grid[k+3][i]
        if 0 not in [a,b,c,d]:
            curma = a*b*c*d
            if maximum < curma:
                maximum = curma
        if i < 17:
            a,b,c,d = grid[k][i],grid[k+1][i+1],grid[k+2][i+2],grid[k+3][i+3]
            if 0 not in [a,b,c,d]:
                curma = a*b*c*d
                if maximum < curma:
                    maximum = curma
        if i > 3:
            a,b,c,d = grid[i][k], grid[i-1][k+1], grid[i-2][k+2], grid[i-3][k+3]
            if 0 not in [a,b,c,d]:
                curma = a*b*c*d
                if maximum < curma:
                    maximum = curma
            a,b,c,d = grid[k][i], grid[k+1][i-1], grid[k+2][i-2], grid[k+3][i-3]
            if 0 not in [a,b,c,d]:
                curma = a*b*c*d
                if maximum < curma:
                    maximum = curma

print(maximum)        
        
