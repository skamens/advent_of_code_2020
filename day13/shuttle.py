#!/usr/bin/python

import sys
import re
import math
import functools

filename = '/home/skamens/advent_of_code_2020/day13/input.txt'

departureTime = 0
busTimes = []

# STOLEN FROM REDDIT. THANK YOU!

def sync(buses):
    for i in range(0, len(buses)) :
        if (buses[i] == 'x') :
            buses[i] = 0
        else :
            buses[i] = int(buses[i])

    indices = [i for i, bus in enumerate(buses) if bus]
    diff = indices[-1] - indices[0]
    prod = functools.reduce(lambda a, b: a * b, filter(None, buses))
    return sum((diff - i) * pow(prod // n, n - 2, n) * prod // n
               for i, n in enumerate(buses) if n) % prod - diff


with open(filename) as f_obj:

    departureTime = int(f_obj.readline())

    line = f_obj.readline()
    line.rstrip()

    busTimes = line.split(',')
    allBusTimes = line.split(',')

    print (sync(allBusTimes))

    busTimes[:] = (value for value in busTimes if value != "x")

diffTimes = dict()
for t in busTimes :
    c = departureTime//int(t)
    diffTimes[((c + 1) * int(t)) - departureTime] = t

theTime = min(diffTimes.keys())

print(theTime, diffTimes[theTime], theTime * int(diffTimes[theTime]))



# Part 2
print (allBusTimes)
busData = []
biggestTime = 0
biggestIndex = 0

for i in range(0, len(allBusTimes)) :
    if (allBusTimes[i] != 0) :
        d = dict()

        t = int(allBusTimes[i])
        d["id"] = t        
        d["interval"] = i
        d["current"] = t
        busData.append(d)
        
        if (t > biggestTime) :
            biggestTime = t
            biggestIndex = len(busData) - 1

print(biggestTime)
print (busData)
#biggestValue = biggestTime
biggestValue = 195042100631
biggestValue = 2231847000631

biggestValue = (100000000000000//busData[biggestIndex]["id"] + 1) * busData[biggestIndex]["id"]
biggestValue = (894954360380000//busData[biggestIndex]["id"] + 1) * busData[biggestIndex]["id"]
busData[biggestIndex]["current"] = biggestValue
cnt = 0
while (True) :
    # We're going to step in increments of the biggest route

    for i in range(0, len(busData)) :
        if (i < biggestIndex) :
            # Set the current time as close to the biggestValue as possible without going over
            v = biggestValue // busData[i]["id"]
            busData[i]["current"] = v * busData[i]["id"]
        elif (i > biggestIndex) :
            v = biggestValue // busData[i]["id"] + 1
            busData[i]["current"] = v * busData[i]["id"]

    if (cnt % 100000) == 0:
        print(busData)  

    cnt += 1
    # OK, now let's see if we're done
    done = True

    for i in range(0, len(busData) - 1) :
        if ((busData[i]["current"] + busData[i+1]["interval"]) != busData[i+1]["current"]) :
            done = False
            break

    if (done) :
        print("DONE!: ", busData)
        exit()

    # OK, if we're not done, bounce to the next iteration of the biggest value
    busData[biggestIndex]["current"] += busData[biggestIndex]["id"]
    biggestValue = busData[biggestIndex]["current"]

        




