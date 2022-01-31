keyboards=[40,50,60]
drives=[5,8,12]
b=60

def getMoneySpent(keyboards, drives, b):
    total=-1
    for x in keyboards:
        for y in drives:
            z=x+y
            if z<=b and z>=total:
                total=z
    return total
                   
    
    
moneySpent = getMoneySpent(keyboards, drives, b)
print(moneySpent)