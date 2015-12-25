
inputFile = open('input.txt', 'r')

instructions = list()

registerA = 1
registerB = 0

for line in inputFile :
    instruction = line.strip()
    instructions.append(instruction)

def getRegister(register) :
    global registerA, registerB
    if register == 'a' :
        return registerA
    else :
        return registerB

def isEven(register) :
    if register == 'a' :
        if registerA % 2 == 0 :
            return True
        else :
            return False
    else :
        if registerB % 2 == 0 :
            return True
        else :
            return False

def hlf(register) :
    global registerA, registerB
    
    if register == 'a' :
        registerA = int(registerA / 2)
    else :
        registerB = int(registerB / 2)

def tpl(register) :
    global registerA, registerB
    
    if register == 'a' :
        registerA = registerA * 3
    else :
        registerB = registerB * 3

def inc(register) :
    global registerA, registerB
    
    if register == 'a' :
        registerA += 1
    else :
        registerB += 1

def interpret(line) :
    words = line.split(" ")

    if words[0] == 'inc' :
        inc(words[1])
    elif words[0] == 'hlf' :
        hlf(words[1])
    elif words[0] == 'tpl' :
        tpl(words[1])

def run() :
    i = 0

    global registerA, registerB
    
    while i <= (len(instructions) - 1) :
        words = instructions[i].split(" ")
        #print(words)
        #print(registerA)
        #print(" ")
        #print(registerB)
        instruct = words[0]
        
        if instruct == 'jmp' :
            i += int(words[1])
        elif instruct == 'jie' :
            if getRegister((words[1])[:-1]) % 2 == 0:
                i += int(words[2])
            else :
                i += 1
        elif instruct == 'jio' :
            if getRegister((words[1])[:-1]) == 1 :
                i += int(words[2])
            else :
                i += 1
        else :
            interpret(instructions[i])
            i += 1
        
run()
print(registerB)
