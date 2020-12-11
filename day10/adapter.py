#!/usr/bin/python

import sys
import re
import math

filename = '/usr/local/google/home/skamens/advent_of_code_2020/day10/input.txt'

adapters = dict()
sortedKeys = []

currentJolts = 0

def buildTree(keys):
    tree = dict()

    entry = dict()
    entry["canReach"] = [keys[0]]
    entry["total"] = 0
    tree[0] = entry

    for i in range (0, len(keys)) :
        
        # Can always get to the next one
        if (not keys[i] in tree) :
            tree[keys[i]] = dict()
            tree[keys[i]]["canReach"] = list()
            tree[keys[i]]["total"] = 0

        if ((i+1) < len(keys)) :
            tree[keys[i]]["canReach"].append(keys[i+1])

        if ((i + 2) < len(keys)) and ((keys[i+2] - keys[i]) < 3) :
            tree[keys[i]]["canReach"].append(keys[i+2])

        if ((i + 3) < len(keys)) and ((keys[i+3] - keys[i]) <= 3) :
            tree[keys[i]]["canReach"].append(keys[i+3])

    return tree
        


def findPath(tree, key) :

    if len(tree[key]["canReach"]) == 0 :
        tree[key]["total"] = 1
        return 1

    for t in tree[key]["canReach"] :
        tree[key]["total"] += findPath(tree, t)

    return tree[key]["total"]



def findDif(last_number):
    dif = []
    for n in sortedKeys:
        dif.append(n-last_number)
        last_number = n
    dif.append(3)
    return dif

def findArrs(dif):
    temp_list = []
    mult_list = []
    for n in dif:
        if n != 3:
            temp_list.append(n)
        
        elif n == 3:
            if len(temp_list) > 3:
                mult_list.append((len(temp_list)-1)*2+(len(temp_list)-3))
            elif len(temp_list) > 1:
                mult_list.append((len(temp_list)-1)*2)
            temp_list = []
            
    r2 = 1
    for x in mult_list:
            r2 = r2 * x 
    return r2






with open(filename) as f_obj:


    for line in f_obj:
        # Populate the list of adapters
        
        adapters[int(line)] = 0

print(adapters)
last = 0
for k in sorted(adapters.keys()) :
    if ((k - currentJolts) > 3) :
        print("ERROR: ", adapters[k], currentJolts)
        exit()
    
    adapters[k] = k - last
    last = k
    currentJolts += k

# Add mine at the end
#adapters[currentJolts + 3] = 3

ones = sum(1 for i in adapters.values() if i == 1) 
threes = sum(1 for i in adapters.values() if i == 3) 

print (ones, threes, ones * threes)


#
# Try to figure out the number of combinations
#

sortedKeys = sorted(adapters.keys())
#total = findPath(0, sortedKeys)

#tree = buildTree(sortedKeys)

#findPath(tree, 0)
#print(tree)

# Find the disjoint subsets
subsets = []
currentSubset = []
for k in sortedKeys :
    if (len(currentSubset) == 0) :
        currentSubset.append(k)
    elif (k - currentSubset[0] <= 3) :
        currentSubset.append(k)
    else:
        print(currentSubset)
        subsets.append(currentSubset)
        currentSubset = [k]

dif = findDif(0)
r1 = dif.count(1)*(dif.count(3))
print("Result part 1: ", r1)

print("Result part 2: ", findArrs(dif))


#print (total)

# combos = [1]
# sortedKeys = sorted(adapters.keys())
# currentJolts = 0
# i = 0
# while (i < len(sortedKeys)) :
#     print(i, currentJolts, combos)
#     if (sortedKeys[i] - currentJolts ) == 3 :
#         currentJolts = sortedKeys[i] # Only one combination works here
#         i += 1
#     elif ((sortedKeys[i] - currentJolts) == 2) :
#         if ((sortedKeys[i+1] - currentJolts) == 3) :
#             # There are 2 combinations that get us to that spot
#             combos.append(2)
#             currentJolts = sortedKeys[i+1]
#             i += 2
#     elif ((sortedKeys[i] - currentJolts) == 1) :
#         if ((sortedKeys[i+1] - currentJolts) == 2) :
#             if ((sortedKeys[i+2] - currentJolts) == 3) :
#                 combos.append(3)
#                 currentJolts = sortedKeys[i+2]
#                 i += 3
#             else :
#                 combos.append(2)
#                 currentJolts = sortedKeys[i+1]
#                 i += 2
#         elif((sortedKeys[i+1] - currentJolts) == 3) :
#             combos.append(2)
#             currentJolts = sortedKeys[i+1]
#             i += 2
#         else :
#             currentJolts = sortedKeys[i]
#             i += 1

# print (combos)
# print (math.prod(combos))

