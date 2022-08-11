
n="148"
k=3
digit="9875987598759875"
def superDigit(n, k):
    total=0
    for x in n:
        #find the sum of the short number
        total+=int(x)
        #find the number, after first sum of all digits
    newNumber=total*k
    if newNumber<10:
        result=newNumber
        #if number longer than 9, continue summing it digits
    else:
        total=0  
        for y in str(newNumber):
            total+=int(y)
        if total<10:
            result=total
        else:
            newSum=0
            for z in str(total):
                newSum+=int(z)
            result=newSum
    return(result)
            


       
    





print(superDigit(n, k))