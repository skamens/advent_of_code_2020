#!/usr/bin/python

import sys
import re
import math

filename = '/home/skamens/advent_of_code_2020/day6/input.txt'

# Read the input



with open(filename) as f_obj:

    d = dict()
    totalCnt = 0
    numInGroup = 0
    for line in f_obj:
        line = line.rstrip()

        if (len(line) == 0):
            for c in d :
               if (d[c] == numInGroup):
                   totalCnt += 1
            d = dict()
            numInGroup = 0
        else :    

            numInGroup += 1
      
            for c in line:
                if (c in d):
                    d[c] += 1
                else:
                    d[c] = 1

            
# At the end there might be some left
for c in d:
    if (d[c] == numInGroup):
        totalCnt += 1
                   
print (totalCnt)