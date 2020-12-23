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
    maxlabel = 0
    head = None
    tail = None
    lookup = {}


    def __init__(self):
        self.cups = None

    def add(self, label):
        self.tail = Cup(label, self.tail)
        self.lookup[label] = self.tail
        self.maxlabel = max(self.maxlabel, label)
        if (not self.head) :
            self.head = self.tail


    def close(self):
        self.tail.next = self.head
        self.head.prev = self.tail

    def move(self):

        # Find the segment to remove
        segstart = self.head.next
        segend = segstart.next.next

        # snip it out of the current list
        self.head.next = segend.next
        segend.next.prev = self.head

        # figure out where to put it
        destlabel = self.head.label - 1
        if destlabel == 0:
            destlabel = self.maxlabel
        while ((segstart.label == destlabel) or \
                (segstart.next.label == destlabel) or \
                (segstart.next.next.label == destlabel)) :
            destlabel -= 1
            if destlabel == 0:
                destlabel = self.maxlabel

        dest = self.lookup[destlabel]
        segend.next = dest.next
        dest.next.prev = segend
       
        dest.next = segstart
        segstart.prev = dest
        
        self.head = self.head.next

    def print(self):
        m = self.head
        
        while(True):
            if m == self.head :
                print (f'({m.label})', end=' ')
            else:
                print(m.label, end=' ')

            if (m.next == self.head) :
                break
            
            m = m.next

        print('')

    
    def part1ans(self):
        m = self.lookup[1]
        m = m.next
        while(m.label != 1):
            print (m.label, end='')
            m = m.next
        print ('')


    def part2ans(self):
        one = self.lookup[1]
        n1 = one.next.label
        n2 = one.next.next.label

        print(f'{n1} * {n2} = {n1 * n2}')


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

    cups = Cups()

    for c in [int(x) for x in list(input)] :
        cups.add(c)
    
    cups.close()

    cups.print()

    for _ in range(0,100):
        cups.move()
        cups.print()

    cups.part1ans()


def part2(input):
    cups = Cups()

    for c in [int(x) for x in list(input)] :
        cups.add(c)

    for x in range(cups.maxlabel+1,1000000):
        cups.add(x)

    cups.close()

    for _ in range(0,10000000):
        cups.move()

    cups.part2ans()

# Test version
#part1('389125467')

# Input for part 1
#part1('653427918')

#part2('389125467')
part2('653427918')


#part2('38912')


