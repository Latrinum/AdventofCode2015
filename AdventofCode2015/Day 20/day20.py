import functools

elves = dict()
factors = list()

def getFactors(n):    
    return set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

houseNumber = 0
houseValue = 0
numPresents = 11
maxPresents = 50

while houseValue < 36000000 :
    houseValue = 0
    houseNumber += 1
    factors = list(getFactors(houseNumber))

    for factor in factors :
        if factor not in elves :
            elves[factor] = 1
            houseValue += factor * numPresents
        elif elves[factor] < maxPresents :
                elves[factor] += 1
                houseValue += factor * numPresents

print("houseNumber: {}, houseValue: {}".format(houseNumber, houseValue))



        
    
