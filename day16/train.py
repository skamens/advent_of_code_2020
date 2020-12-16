#!/usr/bin/python3

import sys
import re
import math
import functools

filename = '/usr/local/google/home/skamens/advent_of_code_2020/day16/input.txt'

ranges = []
mine = []
others = []

with open(filename) as f_obj:

    # First group has the definitions, up to a blank line
    line = ''
    while (True) :
        line = f_obj.readline()
        if (line == '\n') :
            break

        flds = line.split()
        for f in flds :
            a = re.match(r'(\d+)-(\d+)', f)
            if (a != None) :
                start = int(a.group(1))
                end = int(a.group(2))

                ranges.append([start,end])
        
    # Now we have all the ranges. Sort them
    ranges.sort(key = lambda x: x[0])

    i = 0
    while i < (len(ranges) - 1) :
        if (ranges[i+1][0] < ranges[i][1]) :
            ranges[i][0] = min(ranges[i][0], ranges[i+1][0])
            ranges[i][1] = max(ranges[i][1], ranges[i+1][1])

            # Remove ranges[i+1]
            ranges.remove(ranges[i+1])
            # Don't increment i because we removed an element
        else :
            i += 1


    # Now read my ticket
    line = f_obj.readline() # Will say "your ticket:"
    line = f_obj.readline() # This has the ticket info

    line.rstrip()
    mine = line.split(',')
    mine = [int(x) for x in mine]

    print (mine)

    # Now a blank line, then 'nearby tickets'
    f_obj.readline()
    f_obj.readline()

    # Now a set of tickets
    for line in f_obj:
        line.rstrip()
        t = line.split(',')
        others.append([int(x) for x in t])

    invalid = 0
    for t in others :
        for n in t :
            found = False
            for r in ranges:
                if (n > r[0] and n < r[1]) :
                    found = True
                    break
            
            if (not found) :
                invalid += n

print (invalid)