#!/usr/bin/python

import sys
import re
import math

filename = '/home/skamens/advent_of_code_2020/day12/input.txt'

# Read the input

x=0
y=0


# slopes of directions
directions = {
    'E' : [1, 0],
    'W' : [-1, 0],
    'N' : [0,1],
    'S' : [0,-1]
}

# Turn right - add 1
# Turn left - subtract 1
directionOrder = ['N', 'E', 'S', 'W']

currentDirectionIdx = 1

with open(filename) as f_obj:

    for line in f_obj:
        line = line.rstrip()

        a = re.match(r'([A-Z])(\d+)', line)
        direction = a.group(1)
        count=int(a.group(2))

        if direction in directions :
            directionToGo = direction
        elif direction == 'F':
            directionToGo = directionOrder[currentDirectionIdx]
        elif direction == 'L':
            currentDirectionIdx = (currentDirectionIdx - int(count/90)) % 4
            print(line, '->', directionOrder[currentDirectionIdx])
            continue
        elif direction == 'R' :
            currentDirectionIdx = (currentDirectionIdx + int(count/90)) %4
            print(line, '->', directionOrder[currentDirectionIdx])
            continue            
        
        x = x + directions[directionToGo][0] * count
        y = y + directions[directionToGo][1] * count

        print (line, x, y)

print (abs(x) + abs(y))