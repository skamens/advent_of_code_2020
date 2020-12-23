#!/usr/bin/python3

import sys
import re
import math
import functools
import copy


class Cup:

    def __init__(self, label, prev=None):
        self.label = label
        self.next = None
        self.prev = prev
        if (prev) :
            prev.next = self


class Cups:
    def __init__(self):
        self.cups = None

    def add()


def seenString(current, cups):
    idx = cups.index(1)
    s1 = '-'.join([str(c) for c in cups[idx:]])
    s2 = '-'.join([str(c) for c in cups[:idx]])
    s = s1 + '-' + s2
    s += ':'
    s += str(cups[current])
    return s


def addSeen(current, cups, seen):
    seen[seenString(current, cups)] = 1
    #print(seen[-1])

def isSeen(current, cups, seen):
    str = seenString(current, cups)
    if str in seen:
        return True
    else :
        return False

def printCups(cups, current):
    for i in range(0, len(cups)):
        if (i == current) :
            print(f'({cups[i]}) ', end = '')
        else :
            print(cups[i], end=' ')
 


def move(current, cups):
    #printCups(cups, current)
    #print('')

    remove = []

    destlabel = cups[current] - 1

    for _ in range(0,3) :
        idx = (current + 1) % len(cups)
        remove.append(cups.pop(idx))
        if (idx < current):
            current -= 1

    while(True) :
        try:
            destindex = cups.index(destlabel)
            break
        except ValueError:
            destlabel -= 1
            if destlabel < min(cups):
                destlabel = max(cups)
    
    for i in range(destindex + 1, destindex + 4):
        cups.insert(i, remove.pop(0))
        if i <= current:
            current += 1

    return (current + 1) % len(cups)

def part1(input) :
    cups = list(input)
    cups = [int(x) for x in cups]

    current = 0
    for _ in range(0,100):
        current = move(current, cups)

    str = ''
    idx = cups.index(1)
    idx = (idx + 1) % len(cups)

    for i in range(0, len(cups)-1):
        str += f'{cups[idx]}'
        idx = (idx + 1) % len(cups)

    print(str)


def part2(input):

    seen = {}
    cups = list(input)
    cups = [int(x) for x in cups]

    x = max(cups) + 1
    while (x <= 1000000):
        cups.append(x)
        x += 1

    current = 0
    cnt = 0
    while (not isSeen(current, cups, seen)) and (cnt < 10000000) :
        addSeen(current, cups, seen)
        current = move(current, cups)
        cnt += 1
        if (cnt % 100000) == 0:
            print(cnt)

    print("Seen! Length of seen is", len(seen))
        

    #idx = cups.index(1)
    #num1 = cups[(idx + 1) % len(cups)]
    #num2 = cups[(idx + 2) % len(cups)]

    #print (f'{num1} * {num2} = {num1 * num2}')


# Test version
#part1('389125467')

# Input for part 1
#part1('653427918')

part2('389125467')
#part2('38912')


