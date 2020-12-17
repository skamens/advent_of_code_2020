#!/usr/bin/python3

import sys
import re
import math
import functools

filename = 'day17/smallinput.txt'

space = {}

def countActiveNeighbors(x, y, z, space):
    cnt = 0

    for x1 in [x-1, x, x+1] :
        for y1 in [y-1, y, y+1] :
            for z1 in [z-1, z, z+1] :
                if not (x1, y1, z1) in space:
                    space[x1, y1, z1] = {}
                    space[x1, y1, z1]["state"] = '.'

                if space[x1, y1, z1]["state"] == '#':
                    cnt += 1
    
    return cnt - 1

def printSpace(x_min, x_max, y_min, y_max, z_min, z_max, space):
    # Loop over z first, then x, then 7

    for z in range(z_min, z_max) :
        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                print(space[x, y, z]['state'], end='')
            print('')
        print(' ')


x_min = 0
x_max = 0
y_min = 0
y_max = 0
z_min = 0
z_max = 1

with open(filename) as f_obj:
    # Assume the matrix starts at 0,0 (z is 0)
    # Read the list and add it to the space

    for line in f_obj:
        line = line.rstrip()
        y_max = 0
        for c in line :
            space[x_max, y_max, 0] = {}
            space[x_max, y_max, 0]["state"] = c
            y_max += 1
        x_max += 1

printSpace(x_min, x_max, y_min, y_max, z_min, z_max, space)

new_space = {}
# Now expand the range in each dimension
x_min -= 1
x_max += 1
y_min -= 1
y_max += 1
z_min -= 1
z_max += 1

for x in range(x_min, x_max) :
    for y in range(y_min, y_max) :
        for z in range(z_min, z_max) :
            if not (x,y,z) in space :
                space[x,y,z] = {}
                space[x,y,z]["state"] = '.'
            
            space[x,y,z]["active"] = countActiveNeighbors(x, y, z, space)

# Now change the states



for p in space:
    if space[p]["state"] == '#':
        if not space[p]["active"] == 2 or space[p]["active"] == 3:
            space[p]["state"] = '.'

    elif space[p]["active"] == 3:
        space[p]["state"] = '#'

printSpace(x_min, x_max, y_min, y_max, z_min, z_max, space)
