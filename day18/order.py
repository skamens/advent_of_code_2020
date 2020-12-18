#!/usr/bin/python3

import sys
import re
import math
import functools

filename = 'day18/input.txt'

def findMatchingParen(expr, start) :
    # Assumes expr[start] is an open paren
    if (expr[start] != '('):
        return None

    # Find the matching close paren
    numParens = 1
    end = start + 1
    while end < len(expr):
        if expr[end] == '(':
            numParens += 1
        elif expr[end] == ')':
            numParens -= 1
            if numParens == 0 :
                break
        end += 1
    # the new expression is between 0 and end
    newexpr = expr[start + 1:end]
    return newexpr

stack = []
def calculate(expr) :

    if (len(expr) == 1) :
        return int(expr[0])

    for i in range(0, len(expr)) :
        if (expr[i] == '('):
            parenExpr = findMatchingParen(expr, i)
            if (parenExpr == None) :
                exit(-1)

            end = i + len(parenExpr) + 2
            expr[i:end] = [calculate(parenExpr)]
            return calculate(expr)
      
    # By the time we get here, we should have gotten rid of
    # all the parentheses recursively
    # Now do the adds 
    for i in range(0, len(expr)) :
        if (expr[i] == '+') :
            expr[i-1:i+2] = [str(int(expr[i-1])+int(expr[i+1]))]
            return calculate(expr)
        
    # Now there should be no pluses; do the *s    
    for i in range(0, len(expr)) :
        if (expr[i]) == '*':
            expr[i-1:i+2] = [str(int(expr[i-1])*int(expr[i+1]))]
            return calculate(expr)

with open(filename) as f_obj:
    # Assume the matrix starts at 0,0 (z is 0)
    # Read the list and add it to the space

    total = 0
    for line in f_obj:
        line = line.rstrip()
        line = line.replace('(', '( ')
        line = line.replace(')', ' )')

        total += calculate(line.split(' '))

    print(total)