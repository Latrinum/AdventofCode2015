puzzleInput = "hepxcrrq"
maxNumPairs = 2

def consec(a, b) :
    return ord(b) - ord(a) == 1

def incString(inputText) :
    for i in range(len(inputText) - 2) :
        if consec(inputText[i+1], inputText[i+2]) and consec(inputText[i], inputText[i+1]) :
            return True

    return False

def IOL(c) :
    if c == 'i' or c == 'o' or c == 'l' :
        return True
    else :
        return False

def pairs(inputText) :
    numPairs = 0
    lastPairLetter = ''
    
    for i in range(len(inputText) - 1) :
        if inputText[i] == inputText[i+1] and inputText[i] != lastPairLetter :
            numPairs += 1
            lastPairLetter = inputText[i]

    if numPairs > 1 :
        return True
    else :
        return False

def incStr(inputText) :
    length = len(inputText)
    if length == 0 :
        return ''
    
    if inputText[length - 1] == 'z' :
        return incStr(inputText[:-1]) + 'a'
    else :
        inc = chr(ord(inputText[length - 1]) + 1)
        if IOL(inc) :
            inc = chr(ord(inc) + 1)
        return inputText[:-1] + inc

def Test(inputText) :
    
    if incString(inputText) and pairs(inputText) :
        return True
    else :
        return False

def run() :
    testString = puzzleInput
    numPairs = 0
    
    while(numPairs <= maxNumPairs) :
        if Test(testString) :
            print(testString)
            numPairs += 1

        testString = incStr(testString)
        
    

run()
