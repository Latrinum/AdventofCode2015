bossHealth = 103
bossDamage = 9
bossArmour = 2

weaponList = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
armourList = [(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
ringList = [(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]

def attack(damage, armour) :
    if armour >= damage :
        return 1
    else :
        return (damage - armour)

def fight(health, damage, armour) :
    turn = 0
    global bossHealth, bossDamage, bossArmour
    
    while health > 0 and bossHealth > 0 :
        if turn == 0 :
            bossHealth -= attack(damage, bossArmour)
            #print("bossHealth {}".format(bossHealth))
            turn = 1
        else :
            health -= attack(bossDamage, armour)
            #print("player health {}".format(health))
            turn = 0
    
    if bossHealth <= 0 :
        bossHealth = 103
        return 'win'
    else :
        bossHealth = 103
        return 'loss'

def iterRings(cost, damage, armour) :
    #if fight(100, damage, armour) == 'win' :
        #return cost
    #else :
        maxCost = 0
        for (cost1, damage1, armour1) in ringList :
            if fight(100, damage + damage1, armour + armour1) == 'loss' :
                if cost + cost1 > maxCost :
                    maxCost = cost + cost1

        for (cost2, damage2, armour2) in ringList :
            for (cost3, damage3, armour3) in ringList :
                if cost2 != cost3 :
                    if fight(100, damage + damage2 + damage3, armour + armour2 + armour3) == 'loss' :
                        if cost + cost2 + cost3 > maxCost :
                            maxCost = cost + cost2 + cost3

        return maxCost

def iterArmour(cost, damage, armour) :
    #if fight(100, damage, armour) == 'win' :
        #return cost
    #else :
        maxCost = 0

        ringsCost = iterRings(cost, damage, armour)
        if ringsCost > maxCost :
            maxCost = ringsCost
                
        for (cost1, damage1, armour1) in armourList :
            ringsCost = iterRings(cost + cost1, damage, armour + armour1)
            if ringsCost > maxCost :
                maxCost = ringsCost

        return maxCost

def iterWeapons(cost, damage, armour) :
    maxCost = 0
    for (cost1, damage1, armour1) in weaponList :
        armourCost = iterArmour(cost + cost1, damage + damage1, armour)
        if armourCost > maxCost :
            maxCost = armourCost

    return maxCost

print(iterWeapons(0, 0, 0))
