#!/usr/bin/python3

import sys
import re
import math
import functools
 
filename = 'day19/input.txt'

rules = {}


with open(filename) as f_obj:
    
    # Load the rules
    while True:
        line = f_obj.readline()

        line = line.rstrip()
        if (len(line) == 0) :
            break

        (rulenum, rest) = line.split(': ', 2)

        # Add a space at the beginning and the end
        rest = rest.replace('"', '')

        # Special cases:
        # 8: 42 | 42 8
        # 11: 42 31 | 42 11 31

        if (int(rulenum) == 8) :
            rest = '( 42 ) +'
        elif int(rulenum) == 11:
            rest = '( 42 31 ) | ( 42 42 31 31 ) | ( 42 42 42 31 31 31 ) | ( 42 42 42 42 31 31 31 31 ) | ( 42 42 42 42 42 31 31 31 31 31 ) ' + \
                   '( 42 42 42 42 42 42 31 31 31 31 31 31 ) ( 42 42 42 42 42 42 42 31 31 31 31 31 31 31 ) ( 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 ) ' +\
                   '( 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 31 ) ( 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 31 )'
                    

        if (rest.find('|') != -1) :
            rest = f'( {rest} )'       

        rules[int(rulenum)] = rest.split()
        rules[int(rulenum)] = [int(x) if x.isdigit() else x for x in rules[int(rulenum)]]
    
    print (rules)

    while len(rules) > 1 :
        print(rules)
        for r in rules:
            # If there are no numbers, this is ready to substitute
            found = [x for x in rules[r] if type(x) == type(1)]
            if len(found) :
                continue
            # Go through and substitute it
            val = ''.join(rules[r])
            for r2 in rules:
                rules[r2] = [val if v==r else v for v in rules[r2]]

            del rules[r]
            break
                    
    print (rules)

    # OK, now join the last one left

    regexp = ''
    for r in rules:
        regexp = ''.join(rules[r])

    regexp = '^' + regexp + '$' 
    print(regexp)

    expr = re.compile(regexp)

    total = 0

    for line in f_obj:
        line = line.rstrip()

        print(line, end=':')
        if (expr.match(line)) :
            print(" MATCH")
            total += 1
        else :
            print ("NO MATCH")

    print(total, " matches")