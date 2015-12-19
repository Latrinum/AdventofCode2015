import itertools

ingredients = dict()
values = list()
numbers = [x for x in range(0, 101)]
maxScore = 0
amounts = list()

inputFile = open('input.txt','r')

def fillIngredients() :
    i = 0
    
    for line in inputFile :
        words = line.split(" ")
        name = (words[0])[:-1]
        amounts.append(0)
        values.append(list())

        values[i].append(int((words[2])[:-1]))
        values[i].append(int((words[4])[:-1]))
        values[i].append(int((words[6])[:-1]))
        values[i].append(int((words[8])[:-1]))
        values[i].append(int((words[10])[:-1]))
        
        ingredients[name] = {}

        ingredients[name]['capacity'] = int((words[2])[:-1])
        ingredients[name]['durability'] = int((words[4])[:-1])
        ingredients[name]['flavor'] = int((words[6])[:-1])
        ingredients[name]['texture'] = int((words[8])[:-1])
        ingredients[name]['calories'] = int((words[10])[:-1])

        i += 1
        
    return 0

def solve(count, depth) :
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    score = 0
    
    global maxScore

    if sum(amounts) == 100 :
            for j in range(0, len(amounts)) :
                capacity += values[j][0] * amounts[j]
                durability += values[j][1] * amounts[j]
                flavor += values[j][2] * amounts[j]
                texture += values[j][3] * amounts[j]
                calories += values[j][4] * amounts[j]

            score = capacity * durability * flavor * texture
            
            if capacity < 0 or durability < 0 or flavor < 0 or texture < 0 :
                score = 0
            elif calories != 500 :
                score = 0
                
            if score > maxScore :
                maxScore = score

    elif depth > 0 :
        for i in range(0, count+1) :
            amounts[len(amounts) - depth] = i
            solve(count - i, depth - 1)

fillIngredients()
solve(100, len(amounts))
print(maxScore)
