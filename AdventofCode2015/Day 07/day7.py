
inputFile = open('input.txt', 'r')

commandList = list()
destValues = dict()
calcedValues = dict()

for instruct in inputFile :
    instruct = instruct[:-1]
    commandList.append(instruct)

print(commandList)

for command in commandList :
    comSplit = command.split(' -> ')
    if comSplit[1] == 'b' :
        comSplit[0] = '46065'
    destValues[comSplit[1]] = comSplit[0]

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def calc(var) :
    if isNumber(var) :
        return int(var)
    else :
        commands = destValues[var].split(" ")
        print(commands)
        toReturn = 0
        
    if var not in calcedValues :
        if len(commands) == 1 :
            toReturn = calc(commands[0])
        else :
            if commands[0] == 'NOT' :
                toReturn = ~calc(commands[1]) & 0xffff
            elif commands[1] == 'RSHIFT' :
                toReturn = calc(commands[0]) >> int(commands[2])
            elif commands[1] == 'LSHIFT' :
                toReturn = calc(commands[0]) << int(commands[2])
            elif commands[1] == 'AND' :
                toReturn = calc(commands[0]) & calc(commands[2])
            elif commands[1] == 'OR' :
                toReturn = calc(commands[0]) | calc(commands[2])
        calcedValues[var] = toReturn
    return calcedValues[var]

    
print(calc('a'))

