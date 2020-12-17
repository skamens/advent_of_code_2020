#!/usr/bin/python3

import sys
import re
import math
import functools

filename = 'day16/input.txt'

ranges = []
mine = []
others = []

def matchRanges(value, ranges):
    for r in ranges:
        if (value >= r[0] and value <= r[1]) :
            return True
    return False

def matchesOnlyOne(value, fields):
    matchingField = ''
    matches = 0
    for f in fields:
        if ("position" in fields[f]) :
            continue

        if matchRanges(value, fields[f]["ranges"]) :
            matches += 1
            matchingField = f
            
    if (matches == 1) :
        return matchingField
    else:
        return ''



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
        fields[fieldname]["positions"] = []
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

# Start with the first field
# Go through all tickets position by position and see 
# if they all match


for f in fields :
    for pos in range(0, len(fields)) :
        found = True
        for t in others :
            if (not matchRanges(t[pos], fields[f]["ranges"])) :
                found = False
                break
        # If I get here, they all matched, so the position for this field
        # is "pos"

        if (found) :
            fields[f]["positions"].append(pos)
        

# OK, now go through the fields iteratively, finding one with 
# a single position value

done = False
while (not done):

    foundField = ''
    for f in fields:
        if len(fields[f]["positions"]) == 1 :
            foundField = f
            break

    if len(foundField):
        toRemove = fields[foundField]["positions"][0]
        fields[foundField]["pos"] = toRemove

        for f in fields:
            if toRemove in fields[f]["positions"] :
                fields[f]["positions"].remove(toRemove)
    else :
        done = True


# 
# Now find the 6 values I need
#
result = 1

for f in fields:
    if (re.match(r'^departure', f)) :
        pos = fields[f]["pos"]
        print (f, ': pos=', pos, ' value=', mine[pos])
        result *= mine[pos]

print(result)



            


print (fields)