#!/usr/bin/python

import sys
import re
import math

filename = '/usr/local/google/home/skamens/advent_of_code_2020/day7/input.txt'


bagrules = dict()

def canHoldBag(bagcolor, contentcolor) :
    contents = bagrules[bagcolor]
    for c in contents:
        if (c[1] == contentcolor) :
            return True
        if (canHoldBag(c[1], contentcolor)) :
            return True
    return False


def getTotalBags(bagcolor) :
    total = 0
    contents = bagrules[bagcolor]
    for c in contents:
        total += c[0] + c[0] * getTotalBags(c[1])
    return total


# Read the input

with open(filename) as f_obj:

    for line in f_obj:

        # First parse out the initial color

        a = re.search('^(.*) bags contain (.*bag[s,. ]+)*', line)

        color = a.group(1)
        contains = a.group(2)
        
        if (color == 'faded fuschia') :
            print ('here')
        contents = contains.split(',')

        contentlist = []
        for c in contents :
            c = c.strip()
            if (c == '') :
                continue
            words = c.split()

            count = words[0]

            if (count == "no") :
                continue
            
            subcolor = ""
            for w in words[1:] :
                if (re.match('^bag.*', w) == None) :
                    if (len(subcolor) > 0) :
                        subcolor += " " 
                    subcolor += w
            
            entry = [int(count), subcolor]
            contentlist.append(entry)

        bagrules[color] = contentlist


# Now traverse the sets of bag rules to see which ones eventually contain shiny gold bags

totalColors = 0
for bagcolor in bagrules :
    if canHoldBag(bagcolor, 'shiny gold'):
        totalColors += 1


print(totalColors)
    

print (('shiny gold'), getTotalBags('shiny gold'))

        