
inputFile = open('input.txt', 'r')

scores = dict()
racers = dict()

def populateRacers() :
    for line in inputFile :
        words = line.split(" ")
        name = words[0]
        speed = int(words[3])
        maxMoveTime = int(words[6])
        maxRestTime = int(words[13])

        scores[name] = 0
        racers[name] = {}

        racers[name]['speed'] = speed
        racers[name]['maxMoveTime'] = maxMoveTime
        racers[name]['maxRestTime'] = maxRestTime
        racers[name]['currentMoveTime'] = 0
        racers[name]['currentRestTime'] = 0
        racers[name]['distance'] = 0
        racers[name]['move'] = True
        
    return 0

def updateDistance(name) :
    
    if racers[name]['currentMoveTime'] >= racers[name]['maxMoveTime'] :
        racers[name]['move'] = False
    elif racers[name]['currentRestTime'] >= racers[name]['maxRestTime'] :
        racers[name]['move'] = True
                
    if racers[name]['move'] :
        racers[name]['currentRestTime'] = 0
        racers[name]['distance'] += racers[name]['speed']
        racers[name]['currentMoveTime'] += 1
    else :
        racers[name]['currentMoveTime'] = 0
        racers[name]['currentRestTime'] += 1

    return 0

def run() :
    currentTime = 0
    time = 2503
    
    while currentTime < time :
        for key, value in racers.items() :
            updateDistance(key)

        updateScores()
        currentTime += 1

    return updateScores()

def updateScores() :
    maxDistance = 0
    winningNames = list()
    
    for key, value in racers.items() :
        if racers[key]['distance'] > maxDistance :
            maxDistance = racers[key]['distance']

    for key in racers :
        if racers[key]['distance'] == maxDistance :
            scores[key] += 1

    return maxDistance

inputFile = open('input.txt', 'r')
populateRacers()

print(run())
print(scores)
