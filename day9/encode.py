#!/usr/bin/python

import sys
import re
import math

filename = '/usr/local/google/home/skamens/advent_of_code_2020/day9/input.txt'

last25 = []

def check25(value):
    for i in last25[0:24] :
        for j in last25[1:] :
            if ((i != j) and ((i+j) == value)) :
                return True

    return False


# Read the input

preambleSize = 25
currentPos = 0
preambleRemaining = preambleSize

keyNumber = 0

with open(filename) as f_obj:

    for line in f_obj:

        if (preambleRemaining > 0) :
            last25.append(int(line))
            preambleRemaining -= 1
            continue

        # Now we've pre-seeded the 25, so now we can check

        if not check25(int(line)) :
            keyNumber = int(line)
            break

        last25[currentPos] = int(line)
        currentPos = (currentPos + 1) % preambleSize


# 
# Part 2 - now we have the key number. Let's look for a contiguous range that
# equals that number. 
#
# Try to do it a little efficiently, just for fun

contiguousNumbers = []

sumOfNumbers = 0

with open(filename) as f_obj:

    for line in f_obj:

        num = int(line)
        contiguousNumbers.append(num)
        sumOfNumbers += num

        if ((sumOfNumbers == keyNumber) and (len(contiguousNumbers) > 1)):
            print (contiguousNumbers)
            print(contiguousNumbers[0] + contiguousNumbers[-1])
            break

        while sumOfNumbers > keyNumber :
            print (contiguousNumbers, sumOfNumbers, keyNumber)
            sumOfNumbers -= contiguousNumbers.pop(0)

        if (sumOfNumbers == keyNumber) :
            print ("DONE", contiguousNumbers, min(contiguousNumbers) + max(contiguousNumbers))
            break

        

