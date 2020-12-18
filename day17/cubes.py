#!/usr/bin/python3

import sys
import re
import math
import functools

filename = 'day17/input.txt'

space = {}

def countActiveNeighbors(x, y, z, w, space):
    cnt = 0

    for x1 in [x-1, x, x+1] :
        for y1 in [y-1, y, y+1] :
            for z1 in [z-1, z, z+1] :
                for w1 in [w-1, w, w+1] :

                    if (x1, y1, z1, w1) == (x, y, z, w) :
                        continue

                    if (x1, y1, z1, w1) in space and space[x1, y1, z1, w1]["state"] == '#':
                        cnt += 1
    
    return cnt

def printSpace(x_min, x_max, y_min, y_max, z_min, z_max, w_min, w_max, space):
    # Loop over z first, then x, then 7

    for z in range(z_min, z_max) :
        for w in range(w_min, w_max) :
            print('z=', z, 'w=',w)
            for x in range(x_min, x_max):
                for y in range(y_min, y_max):
                    print(space[x, y, z, w]['state'], end='')
                print('')
            print(' ')


x_min = 0
x_max = 0
y_min = 0
y_max = 0
z_min = 0
z_max = 1
w_min = 0
w_max = 1

with open(filename) as f_obj:
    # Assume the matrix starts at 0,0 (z is 0)
    # Read the list and add it to the space

    for line in f_obj:
        line = line.rstrip()
        y_max = 0
        for c in line :
            space[x_max, y_max, 0, 0] = {}
            space[x_max, y_max, 0, 0]["state"] = c
            y_max += 1
        x_max += 1

printSpace(x_min, x_max, y_min, y_max, z_min, z_max, w_min, w_max, space)

for i in range(0,6) :

    # Expand the range in each dimension

    x_min -= 1
    x_max += 1
    y_min -= 1
    y_max += 1
    z_min -= 1
    z_max += 1
    w_min -= 1
    w_max += 1

    for x in range(x_min, x_max) :
        for y in range(y_min, y_max) :
            for z in range(z_min, z_max) :
                for w in range (w_min, w_max) :
                    if not (x,y,z,w) in space :
                        space[x,y,z,w] = {}
                        space[x,y,z,w]["state"] = '.'
                    
                    space[x,y,z,w]["active"] = countActiveNeighbors(x, y, z, w, space)

    # Now change the states

    for p in space:
        if space[p]["state"] == '#':
            if not (space[p]["active"] == 2 or space[p]["active"] == 3):
                space[p]["state"] = '.'

        elif space[p]["active"] == 3:
            space[p]["state"] = '#'

    printSpace(x_min, x_max, y_min, y_max, z_min, z_max, w_min, w_max, space)


# Count the total number of active cubes
total = 0
for p in space :
    if space[p]['state'] == '#' :
        total += 1

print(total)
