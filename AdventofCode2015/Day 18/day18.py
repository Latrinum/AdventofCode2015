
inputFile = open('input.txt', 'r')

width = 100
height = 100
steps = 100

grid = list()
updates = list()

row = 0

for line in inputFile :
    grid.append([])
    for i in range(0, height) :
        grid[row].append(line[i])
    row += 1

grid[0][width - 1] = '#'
grid[width - 1][width - 1] = '#'
grid[0][0] = '#'
grid[width - 1][0] = '#'

def swap(ch) :
    if ch == '#' :
        return '.'
    else :
        return '#'

def getLower(num) :
    if num - 1 < 0 :
        return num
    else :
        return num - 1
    
def getUpper(num) :
    if num > width - 1 :
        return num - 1
    else :
        return num

def getNeighbours(y, x, key) :
    count = 0
    
    lowerY = getLower(y)
    upperY = getUpper(y + 1)
    lowerX = getLower(x)
    upperX = getUpper(x + 1)

    for i in range(lowerY, upperY + 1) :
        for j in range(lowerX, upperX + 1) :
            if i != y or j != x :
                if grid[i][j] == key :
                    count += 1

    return count

def notCorner(y, x) :
    if x == 0 or x == width - 1:
        return not (y == 0 or y == width - 1)
    if y == 0 or y == width - 1:
        return not (x == 0 or x == width - 1)
    
    return True

def populateUpdates() :
    updates.clear()
    
    for y in range(0, height) :
        for x in range(0, width) :
            command = ''
            if notCorner(y, x) :
                if grid[y][x] == '#' :
                    if getNeighbours(y, x, '#') != 2 and getNeighbours(y, x, '#') != 3 :
                        command = str(y) + "|" + str(x)
                        updates.append(command)
                else :
                    if getNeighbours(y, x, '#') == 3 :
                        command = str(y) + "|" + str(x)
                        updates.append(command)

def executeUpdates() :
    for command in updates :
        nums = command.split("|")
        y = int(nums[0])
        x = int(nums[1])

        grid[y][x] = swap(grid[y][x])

def printGrid() :
    for row in grid :
        print(row)

def countOn() :
    count = 0
    for row in grid :
        for light in row :
            if light == '#' :
                count += 1

    return count

for step in range(0, steps) :
    populateUpdates()
    executeUpdates()

printGrid()
print(countOn())

        
