#!/usr/bin/python

import sys

filename = '/usr/local/google/home/skamens/advent_of_code/day1/expenses.in'

expenses = []
with open(filename) as f_obj:
    for line in f_obj:
        line = line.rstrip()
        expenses.append(int(line))

print (expenses)

for i in expenses[:len(expenses)-1] :
    for j in expenses[1:len(expenses)] :
        for k in expenses[2:] : 
            if ((i + j + k) == 2020):
                print ("Found it! ", 
                        i, " x ",
                        j, " x ",
                        k, 
                        "=",  i * j * k)
                exit(0)
