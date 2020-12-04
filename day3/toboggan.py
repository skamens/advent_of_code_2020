#!/usr/bin/python

import sys
import re
import math

filename = '/usr/local/google/home/skamens/advent_of_code_2020/day3/map.txt'


# Read the input

i = 0
treeMap = []
with open(filename) as f_obj:
    for line in f_obj:
        line = line.rstrip()
        chars = list(line)
        treeMap.append(chars)


slopesToCheck = [ [1, 1],
                  [3, 1],
                  [5, 1],
                  [7, 1],
                  [1, 2]]


width = len(treeMap[0])        

results = []
for slope in slopesToCheck :
    treeCount = 0

    x = slope[1]
    y = slope[0]

    while(x < len(treeMap)) :

        if (treeMap[x][y] == '#') :
            treeCount += 1

        y = (y + slope[0] ) % width
        x += slope[1]

    results.append(treeCount)

final = math.prod(results)   

print (final)




