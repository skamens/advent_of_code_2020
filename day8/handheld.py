#!/usr/bin/python

import sys
import re
import math

filename = '/usr/local/google/home/skamens/advent_of_code_2020/day8/input.txt'

# Read the input

instructions = []


with open(filename) as f_obj:

    for line in f_obj:
        line = line.rstrip()

        a = re.match('([^ ]+) ([+-])(\d+)', line)

        if (a.group(2) == '+') :
            inc = int(a.group(3))
        else:
            inc = -1 * int(a.group(3))
        
        instructions.append([a.group(1), inc, 0])

lastChanged = -1
acc = 0
pc = 0

while True :
    if (instructions[pc][0] == "acc") :
        acc += instructions[pc][1]
        nextPc = pc + 1
    elif (instructions[pc][0] == "jmp") :
        nextPc += instructions[pc][1]
    elif (instructions[pc][0] == "nop") :
        nextPc = pc + 1
    
    if (nextPc >= len(instructions)) :
        print("DONE! acc=", acc)
        break

    instructions[pc][2] = 1
    if ((nextPc >= len(instructions)) or (instructions[nextPc][2] == 1) ):
        # We hit a loop, so try changing one of the instructions and
        # reset
        # First changed the lastChanged back
        if (lastChanged != -1) :
            if (instructions[lastChanged][0] == "nop") :
                instructions[lastChanged][0] = "jmp"
            else :
                instructions[lastChanged][0] = "nop"

        lastChanged += 1
        while (instructions[lastChanged][0] == "acc") :
            lastChanged += 1

        if instructions[lastChanged][0] == "nop" :
            instructions[lastChanged][0] = "jmp" 
        else :
            instructions[lastChanged][0] = "nop"
            
        acc = 0
        pc = 0
        nextPc = 0
        # Reset all the visited values
        for i in instructions :
            i[2] = 0

    else :
        pc = nextPc

        
