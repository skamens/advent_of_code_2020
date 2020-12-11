filename = '/usr/local/google/home/skamens/advent_of_code_2020/day11/input.txt'

slopes = [ [1,1],
           [1,0],
           [1,-1],
           [0, 1],
           [0, -1],
           [-1, 1],
           [-1, 0],
           [-1, -1]
        ]


def printMap(seatMap) :
    for i in seatMap :
        str = ""
        for j in i :
            str += j
        print (str)
    print()





def countOccupied(seatMap, i, j) :
    total = 0

    for s in slopes:
        k = i + s[0]
        l = j + s[1]
        
        while k >= 0 and k < len(seatMap) and l>= 0 and l < len(seatMap[i]) and seatMap[k][l] == '.' :
            k = k + s[0]
            l = l + s[1]

        if k >= 0 and k < len(seatMap) and l>= 0 and l < len(seatMap[i]):
            if (seatMap[k][l] == '#') :
                total += 1
    
    return total

seatMap = []
with open(filename) as f_obj:
    for line in f_obj:
        line = line.rstrip()
        chars = list(line)
        seatMap.append(chars)

printMap(seatMap)

changed = True

totalOccupied = 0

while (changed) :
    changed = False
    totalOccupied = 0
    workMap= []
    for r in seatMap:
        workMap.append(r.copy())

    for i in range(0,len(seatMap)) :
        for j in range(0, len(seatMap[i])) :
            
            occupied = countOccupied(seatMap, i, j)

            if (seatMap[i][j] == 'L') :
                if occupied == 0:
                    workMap[i][j] = '#'
                    changed = True
               
            if seatMap[i][j] == '#':
                totalOccupied += 1
                if occupied >= 5 :
                    workMap[i][j] = 'L'
                    changed = True
    seatMap = workMap
    printMap(seatMap)

print (totalOccupied)



