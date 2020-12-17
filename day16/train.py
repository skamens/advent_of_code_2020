#!/usr/bin/python3

import sys
import re
import math
import functools

filename = '/usr/local/google/home/skamens/advent_of_code_2020/day16/input.txt'

ranges = []
mine = []
others = []

fields = dict()
with open(filename) as f_obj:

    # First group has the definitions, up to a blank line
    line = ''
    while (True) :
        line = f_obj.readline()
        if (line == '\n') :
            break

        (fieldname, rest) = line.split(':')
        
        fields[fieldname] = dict()
        fields[fieldname]["ranges"] = []
        flds = rest.split()
        for f in flds :
            a = re.match(r'(\d+)-(\d+)', f)
            if (a != None) :
                start = int(a.group(1))
                end = int(a.group(2))

                ranges.append([start,end])
                fields[fieldname]["ranges"].append([start,end])
        fields[fieldname]["ranges"].sort(key = lambda x:x[0])

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
            # Since it's invalid, remove it from the list
            others.remove(t)

for f in fields:
    for t in others:
        matchingIndex = -1
        for i in range(0, len(t)):
            for r in fields[f]["ranges"]:
                if (t[i] >= r[0] and t[i] <= r[1]) :
                    if matchingIndex == -1:
                        matchingIndex = i
                    else :
                        matchingIndex = -1
                        break
        if (matchingIndex != -1):
            fields[f]["position"] = matchingIndex
            break


print (fields)


    



