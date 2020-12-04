#!/usr/bin/python

import sys
import re
import math

filename = '/usr/local/google/home/skamens/advent_of_code_2020/day4/input.txt'


eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
requiredkeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Read the input

passportList = []

with open(filename) as f_obj:

    done = False
    passportList.append(dict())

    for line in f_obj:
        line = line.rstrip()

        if (len(line) == 0):
            passportList.append(dict())    
        else :
            l = line.split(' ')
            d = dict(s.split(':') for s in l)
            passportList[-1].update(d)

validCount = 0
for passport in passportList :
    # First weed out the invalid ones by count

    if (not all (k in passport for k in requiredkeys)) :
        continue

    # OK, now validate by field

    # Birth year must be between 1920 and 2002
    yr = int(passport['byr'])
    if ((yr < 1920) or (yr > 2002)) :
        continue

    # Issue year
    yr = int(passport['iyr'])
    if ((yr < 2010) or (yr > 2020)) :
        continue

    # Expiration year
    yr = int(passport['eyr'])
    if ((yr < 2020) or (yr > 2030)) :
        continue

    # Height
    m = re.match('^\d+', passport['hgt'])
    value = int(m.group())

    units = passport['hgt'][m.end():]

    if (not units in ['in', 'cm']) :
        continue

    if (units == 'in') :
        if ((value < 59) or (value > 76)) :
            continue
    else :
        if (units == 'cm') :
            if ((value < 150) or (value > 193)) :
                continue

    #Hair Color


    m = re.match('#[0-9a-f]{6,6}', passport['hcl'])
    if (m == None) :
        continue

    # Eye color
    if (not passport['ecl'] in eyecolors) :
        continue

    m = re.match('^[0-9]{9,9}$', passport['pid'])
    if (m == None) :
        continue

    validCount += 1

print(validCount)

