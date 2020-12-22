#!/usr/bin/python3

import sys
import re
import math
import functools
import copy

filename = 'day22/input.txt'

class Deck:
    
    def __init__(self):
        self.cards = []
        self.playerNum = 0

    def load(self, file_obj):
        line = f_obj.readline()
        a = re.match(r'^Player (\d+).*', line)
        self.playerNum = int(a.group(1))

        line = f_obj.readline()
        while (line and (line != '\n')):
            self.cards.append(int(line))
            line = f_obj.readline()
        print(self.playerNum, ":", self.cards)

    def top(self):
        return self.cards[0]

    def hasLost(self):
        return len(self.cards) == 0

    def play(self, other):
        if (self.top() > other.top()):
            self.cards.append(self.cards.pop(0))
            self.cards.append(other.cards.pop(0))
        else: 
            other.cards.append(other.cards.pop(0))
            other.cards.append(self.cards.pop(0))

    def score(self):
        total = 0
        for mult in range(len(self.cards), 0, -1):
            total += mult * self.cards[(len(self.cards) - mult)]

        return total
 

def game1(deck1, deck2):
    while (not (deck1.hasLost() or deck2.hasLost())) :
        deck1.play(deck2)



def game2(deck1, deck2):
    rounds = []
    
    while (not (deck1.hasLost() or deck2.hasLost())):

        # Before either player deals a card, if there was a previous round in this game that had exactly 
        # the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. 
        # Previous rounds from other games are not considered. (This prevents infinite games of 
        # Recursive Combat, which everyone agrees is a bad idea.)

        for r in rounds:
            if ((r[deck1.playerNum] == deck1.cards) and 
                (r[deck2.playerNum] == deck2.cards)) :
                return 1

        # Add this round to the list of rounds
        arr = []
        arr.append([])
        arr.append(deck1.cards.copy())
        arr.append(deck2.cards.copy())
        rounds.append(arr)

        # Otherwise, this round's cards must be in a new configuration; the players begin the round
        # by each drawing the top card of their deck as normal.

        # If both players have at least as many cards remaining in their deck as the value of
        # the card they just drew, the winner of the round is determined by playing 
        # a new game of Recursive Combat (see below).

        if (deck1.top() <= len(deck1.cards)) and (deck2.top() <= len(deck2.cards)) :
            newDeck1 = Deck()
            newDeck1.playerNum = deck1.playerNum
            newDeck1.cards = deck1.cards[1:deck1.top() + 1]

            newDeck2 = Deck()
            newDeck2.playerNum = deck2.playerNum
            newDeck2.cards = deck2.cards[1:deck2.top() + 1]

            winner = game2(newDeck1, newDeck2)
            if (winner == deck1.playerNum):
                deck1.cards.append(deck1.cards.pop(0))
                deck1.cards.append(deck2.cards.pop(0))
            else: 
                deck2.cards.append(deck2.cards.pop(0))
                deck2.cards.append(deck1.cards.pop(0))  
                
        else:
            deck1.play(deck2)

        print (deck1.playerNum, ":", deck1.cards)
        print (deck2.playerNum, ":", deck2.cards, "\n")

    if deck1.hasLost():
        return deck2.playerNum
    else:
        return deck1.playerNum


            

with open(filename) as f_obj:
    # Assume the matrix starts at 0,0 (z is 0)
    # Read the list and add it to the space

    deck1 = Deck()
    deck2 = Deck()
    deck1.load(f_obj)
    deck2.load(f_obj)

d1 = copy.deepcopy(deck1)
d2 = copy.deepcopy(deck2)
game1(d1, d2)

d3 = copy.deepcopy(deck1)
d4 = copy.deepcopy(deck2)
winner = game2(d3, d4)

print ("winner: ", winner)
print (deck1.playerNum, ":", d3.score())
print (deck2.playerNum, ":", d4.score())
