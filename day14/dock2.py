#!/usr/bin/python3

import sys
import re
import math
import functools

filename = '/home/skamens/advent_of_code_2020/day14/input.txt'

memory = dict()
with open(filename) as f_obj:

    for line in f_obj:
        line = line.rstrip()
        (cmd, rest) = line.split(' = ', 2)

        if (cmd == "mask") :
            set_bits = 0
            bitnum = 35
            float_bitmasks = [0]
            for b in list(rest) :
                set_bits = set_bits << 1
                # Shift all of the float_bitmasks
                float_bitmasks = [m << 1 for m in float_bitmasks]

                if (b == '1') :
                    set_bits |= 1
                elif (b == 'X') :
                    new_bitmasks = []
                    for m in float_bitmasks:
                        # Shift each element by 1, and add 0, then add 1
                        new_bitmasks.append(m)
                        m |= 1
                        new_bitmasks.append(m)
                    float_bitmasks = new_bitmasks
                        

                
                bitnum -= 1

            print (rest)
            print ('{:b}'.format(set_bits))
            print (float_bitmasks)

        else:
            # It's setting a memory location                
            m = re.match(r'mem\[(\d+)\]', cmd)
            location = int(m.group(1))

            value = int(rest)

            # Set the set_bits in the location
            location |= set_bits

            # Now do the float bits.
            # First clear all the bits that have floating values
            location &= ~ max(float_bitmasks)
            for m in float_bitmasks :
                m = location | m
                memory[m] = value
            


print ("Total: ", sum(memory.values()))
