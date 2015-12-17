import itertools

names = list()
perms = list()
values = dict()

inputFile = open('input.txt', 'r')

def fillNames() :
    lastName = ''
    
    for line in inputFile :
        words = line.split(" ")
        
        if words[0] != lastName :
            names.append(words[0])
            lastName = words[0]
            
def initValues() :
    for name in names :
        values[name] = dict()

def fillValues() :
    for line in inputFile :
        words = line.split(" ")
        value = int(words[3])
        if words[2] == 'lose' :
            value = -value
        values[words[0]][(words[10])[:-2]] = value

def getHappiness(name1, name2) :
    return values[name1][name2] + values[name2][name1]

def run() :
    maxHappiness = 0

    for perm in perms :
        happiness = getHappiness(perm[0], perm[len(perm) - 1])
        
        for index in range(0, len(perm) - 1) :
            happiness += getHappiness(perm[index], perm[index + 1])

        if happiness > maxHappiness :
            maxHappiness = happiness

       
    return maxHappiness

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

fillNames()
names.append('Sam')

initValues()
inputFile = open('input.txt', 'r')
fillValues()

for name in values :
    values[name]['Sam'] = 0
    values['Sam'][name] = 0
    
print(values)

perms = all_perms(names)
print(perms)

print(run())
