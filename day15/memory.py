#!/usr/bin/python3


turns = { 1 : [1], 
          0 : [2],
          15: [3],
          2 : [4],
          10 : [5],
          13 : [6]}

# turns = { 0 : [1],
#           3 : [2],
#           6 : [3]}
turn = len(turns) + 1
number = 13
while (True) :
    if len(turns[number]) == 1 :
        number = 0
    else :
        number = turns[number][-1] - turns[number][-2]

    if not number in turns:
        turns[number] = []

    turns[number].append(turn)
    if (turn % 10000) == 0 :
        print ("Turn ", turn, ": ", number)
    if turn == 30000000 :
        print("Turn 30000000: ", number)
        exit(0)
    turn += 1
