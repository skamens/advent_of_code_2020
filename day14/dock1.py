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
            clear_bits = 0
            for b in list(rest) :
                set_bits = set_bits << 1
                clear_bits = clear_bits << 1
                if (b == '1') :
                    set_bits |= 1
                elif(b == '0') :
                    clear_bits |= 1

            print (rest)
            print ('{:b}'.format(set_bits))
            print ('{:b}'.format(clear_bits))

        else:
            # It's setting a memory location                
            m = re.match(r'mem[[](\d+)[]]', cmd)
            location = int(m.group(1))

            value = int(rest)
            print ('{:b}'.format(value))

            # Set the bits that should be set
            value |= set_bits
            print ('{:b}'.format(value))

            value &= ~ clear_bits
            print ('{:b}'.format(value))

            memory[location] = value


print ("Total: ", sum(memory.values()))
