
inputFile = open('input.txt', 'r')

totalStore = 150

containers = list()
minNum = 1000

def getPerms(sizeLeft, index, num, key) :
    perms = 0
    global minNum

    if key == 'part2' and num > minNum :
        return 0
    if sizeLeft == 0 :
        if num < minNum :
            minNum = num
        return 1
    elif sizeLeft <= 0 :
        return 0
    
    for j in range(index + 1, len(containers)) :
        perms += getPerms(sizeLeft - containers[j], j, num + 1, key)
            
    return perms

def fillContainers() :

    for line in inputFile :
        containers.append(int(line))

    containers.sort()
    containers.reverse()

fillContainers()
print(containers)

perms = 0

for i in range(0, len(containers)) :
    perms += getPerms(totalStore - containers[i], i, 1, 'part1')

print("part1 = {}".format(perms))

perms = 0

for i in range(0, len(containers)) :
    perms += getPerms(totalStore - containers[i], i, 1, 'part2')
    
print("part2 = {}".format(perms))
