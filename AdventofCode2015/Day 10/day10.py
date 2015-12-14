inputText = "1113122113"

print(inputText)

def run(input, depth) :
    answer = ""
    lastNum = input[0]
    numCount = 0
    length = 0
    
    if depth == 0 :
        return 0
    else :
        for num in input :
            
            if num != lastNum :
                answer += str(numCount)
                answer += str(lastNum)
                
                numCount = 1
                lastNum = num
            else :
                numCount += 1

        answer += str(numCount)
        answer += str(lastNum)
        
        length = len(answer)
        print("length = {}, depth = {}".format(length, depth)) 
        length += run(answer, depth - 1)
                           
                
    return length


run(inputText, 50)
