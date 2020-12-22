#!/usr/bin/python3

import sys
import re
import math
import functools
 
filename = 'day20/input.txt'

class Tile:
    id: int
    data: list
    def __init__(self, id, data):
       self.id = int(id)
       self.data = data
       self.size = len(self.data)

    def __repr__(self):
        return f'id:{self.id}'

    def show(self):
        print("\n".join(self.data))

    def top(self):
        return self.data[0]
    def bottom(self):
        return self.data[-1]
    def left(self):
        return ''.join(row[0] for row in self.data)
    def right(self):
        return ''.join(row[-1] for row in self.data)


def readTile(file_obj, tiles) :
    line = file_obj.readline()

    if (not line) :
        f_obj.close()
        return

    line = line.replace('Tile ', '')
    line = line.replace(':\n', '')
    
    tileNum = int(line)
    tiles[tileNum] = {}
    tiles[tileNum]["left"] = ''
    tiles[tileNum]["right"] = ''
    tiles[tileNum]['block'] = ''
    tiles[tileNum]['matches'] = []

    # Now read until we get a blank line
    while (True) :
        line = file_obj.readline()
        if((line == '') or (line == '\n')) :
            break

        tiles[tileNum]['block'] = tiles[tileNum]['block'] + line

        line = line.rstrip()

        if (not "top" in tiles[tileNum]):
            tiles[tileNum]["top"] = line
        
        # Make this the bottom; when we get to 
        # the end, it'll be the right "bottom"

        tiles[tileNum]["bottom"] = line

        # Add the first charater to "left"
        tiles[tileNum]['left'] = tiles[tileNum]['left'] + line[0]
        tiles[tileNum]['right'] = tiles[tileNum]['right'] + line[-1]

    print(tileNum)
    print (tiles[tileNum])

with open(filename) as f_obj:
    while (not f_obj.closed) :
        readTile(f_obj, tiles)


    # For each tile, figure out which ones it can be next to, and in which ways

    for t in tiles:
        for t2 in tiles:
            if (t == t2) :
                continue
        
        for a in ['top', 'bottom', 'left', 'right'] :
            for b in ['top', 'bottom', 'left', 'right'] :

                if (((a == 'top') and (b == 'bottom')) or 
                    ((a == 'bottom') and (b == 'top')) or
                    ((a == 'left') and (b == 'right')) or
                    ((a == 'right') and (b == 'left')) or 
                    ((a == 'top' and (b == 'left')) or 
                    ((a == 'left') and (b == 'right)')) or
                    ((a == 'bottom') and )

                if (tiles[t][a] == tiles[t2][b]) :
                    tiles[t]['matches'].append([a, t2, b])
        print(t, ': ', tiles[t])
