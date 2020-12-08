#!/usr/bin/python

import sys
import re
import math

filename = '/home/skamens/advent_of_code_2020/day5/input.txt'

# Read the input

maxSeatId = 0
allIds = []

with open(filename) as f_obj:

    for line in f_obj:

        line = line.rstrip()

        rowTuple = [0, 127]
        for char in line[0 : 6 : 1]:
            if (char == 'F') :
               rowTuple[1] = math.floor((rowTuple[0] + rowTuple[1])/2)
            else :
                rowTuple[0] = math.ceil((rowTuple[0] + rowTuple[1])/2)

        if (line[6] == 'F') :
            rowNum = rowTuple[0]
        else :
            rowNum = rowTuple[1]

        seatTuple = [0,7]
        for char in line[7:9:1] :
            if (char == 'L') :
                seatTuple[1] = math.floor((seatTuple[0] + seatTuple[1])/2)
            else :
                seatTuple[0] = math.ceil((seatTuple[0] + seatTuple[1])/2)
        
        if (line[9] == 'L'):
            seatNum = seatTuple[0]
        else :
            seatNum = seatTuple[1]

        print (line, ': row:', rowNum, ' seat:', seatNum, ' seatId: ', 8 * rowNum + seatNum)
        maxSeatId = max(maxSeatId, 8 * rowNum + seatNum)

        allIds.append(8 * rowNum + seatNum)

allIds.sort()

for i in range(0, len(allIds) - 1) :
    print allIds[i], allIds[i+1]
    if allIds[i+1] == allIds[i] + 2 :
        print (allIds[i], allIds[i+1])


    