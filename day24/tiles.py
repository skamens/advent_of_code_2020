class Tile:

    OPPOSITE_DIRECTIONS = {
        'e': 'w',
        'ne' : 'sw',
        'nw' : 'se',
        'w' : 'e',
        'sw' : 'ne',
        'se' : 'nw'
    }

    NEIGHBOR_DIRECTIONS = {
        'e' : ['ne', 'se'],
        'ne': ['nw', 'e'],
        'nw': ['ne', 'w'],
        'w' : ['nw', 'sw'],
        'sw' : ['w', 'se'],
        'se' : ['sw', 'e']
    }

    NEIGHBOR_DIRECTION_MAPPING = {
        'e': { 'ne' : 'nw', 'se': 'sw'},
        'se' : { 'e': 'ne', 'sw': 'w'},
        'sw' : { 'se' : 'e', 'w': 'nw' },
        'w' : { 'sw' : 'se', 'nw': 'ne'},
        'nw' : {'w' : 'sw', 'ne': 'e'},
        'ne' : {'nw': 'w', 'e': 'se'}
    }

    def __init__(self):
        self.color = 'white'
    
        self.neighbors = {
            'e' : None,
            'ne' : None,
            'nw' : None,
            'w' : None,
            'sw' : None,
            'se' : None
        }

    def setDirection(self, t, direction):
        self.neighbors[direction] = t


    def handleExistingNeighbors(self, t, direction):
        # t is being added - need to handle the existing neighbors of self
        # to hook it in

        for n in self.NEIGHBOR_DIRECTIONS[direction]:
            if self.neighbors[n]:

                t_neighbor_d = self.NEIGHBOR_DIRECTION_MAPPING[direction][n]
                neighbor_t_d = self.OPPOSITE_DIRECTIONS[t_neighbor_d]

                # Need set the direction for the new one to point to its
                # new neighbor
                if t.neighbors[t_neighbor_d] :
                    # Already there
                    continue

                t.setDirection(self.neighbors[n], t_neighbor_d)
                self.neighbors[n].setDirection(t, neighbor_t_d)

                # Also have to handle existing neighbors from the neighbor
                self.neighbors[n].handleExistingNeighbors(t, neighbor_t_d)

    def addNeighbor(self, direction):
        # Add a new tile in the given direction

        t = Tile()
        self.setDirection(t, direction)
        t.setDirection(self, self.OPPOSITE_DIRECTIONS[direction])

        self.handleExistingNeighbors(t, direction)
                 
        return t
    
    def flip(self) :
        if self.color == 'white' :
            self.color = 'black'
        else:
            self.color = 'white'

        return self.color

    def move(self, direction):
        t = self.neighbors[direction]
        if t :
            return t
        
        # Need to add a new one
        return self.addNeighbor(direction)


def processLine(line, referencetile):
    direction_order = ['ne', 'nw', 'se', 'sw', 'e', 'w']

    t = referencetile
    while (line != '\n') and (line != ''):
        for d in direction_order:
            if line.startswith(d):
                t = t.move(d)
                line = line.replace(d, '', 1)
                break
    # Now we've finished moving
    return t.flip()


def part1(filename):
    
    # Start with the first tile
    referencetile = Tile()
    blackCount = 0

    with open(filename) as f_obj:
        for line in f_obj:
            if processLine(line, referencetile) == 'black':
                blackCount += 1
            else :
                blackCount -= 1

    print("Total Black Tiles: ", blackCount)


# Main

part1('day24/smallinput.txt')
part1('day24/input.txt')

#processLine('esew', Tile())