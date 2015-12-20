
inputFile = open('input.txt','r')

winner = {'children' : [3], 'cats' : [x for x in range(8, 1000)], 'samoyeds' : [2], 'pomeranians' : [x for x in range(0, 3)], 'akitas' : [0], 'vizslas' : [0], 'goldfish' : [x for x in range(0, 5)], 'trees' : [x for x in range(4, 1000)], 'cars' : [2], 'perfumes' : [1]}
potential = dict()

for line in inputFile :
    words = line.split(" ")
    attribute1 = (words[2])[:-1]
    attribute2 = (words[4])[:-1]
    attribute3 = (words[6])[:-1]
    if int((words[3])[:-1]) in winner[attribute1]:
        if int((words[5])[:-1]) in winner[attribute2] :
            if int((words[7])[:-1]) in winner[attribute3] :
                sueNum = (words[1])[:-1]
                potential[sueNum] = {}
                potential[sueNum][attribute1] = int((words[3])[:-1])
                potential[sueNum][attribute2] = int((words[5])[:-1])
                potential[sueNum][attribute3] = int((words[7])[:-1])
                

print(potential)
