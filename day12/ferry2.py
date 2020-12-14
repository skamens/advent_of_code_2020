#!/usr/bin/python

import sys
import re
import math

filename = '/home/skamens/advent_of_code_2020/day12/input.txt'

x=0
y=0

currentWayPoint = [10, 1]


# angle = (angle ) * (Math.PI/180); // Convert to radians
# var rotatedX = Math.cos(angle) * (point.x - center.x) - Math.sin(angle) * (point.y-center.y) + center.x;
# var rotatedY = Math.sin(angle) * (point.x - center.x) + Math.cos(angle) * (point.y - center.y) + center.y;
# return new createjs.Point(rotatedX,rotatedY);

with open(filename) as f_obj:

    for line in f_obj:
        line = line.rstrip()

        a = re.match(r'([A-Z])(\d+)', line)
        direction = a.group(1)
        count=int(a.group(2))

        if direction == 'F':
            x = x + currentWayPoint[0] * count
            y = y + currentWayPoint[1] * count
        elif direction == 'N':
            currentWayPoint[1] += count
        elif direction == 'S':
            currentWayPoint[1] -= count
        elif direction == 'E':
            currentWayPoint[0] += count
        elif direction == 'W':
            currentWayPoint[0] -= count
        elif direction == 'L':
            degrees = count//90
            for _ in range(degrees):
                currentWayPoint = [-currentWayPoint[1], currentWayPoint[0]]
        elif direction == 'R':
            degrees = count//90
            for _ in range(degrees):
                currentWayPoint = [currentWayPoint[1], -currentWayPoint[0]]
        
        print (line, 'Waypoint: ', currentWayPoint, x, y)



print (abs(x) + abs(y))