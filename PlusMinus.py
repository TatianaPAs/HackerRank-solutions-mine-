# https://www.hackerrank.com/challenges/plus-minus/problem

arr=[-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    #initialise count of zero, positive and negative to zero
    count0=0
    countPositive=0
    countNegatvie=0
    for x in arr:
        #if number is 0, increase zero count
        if x==0:
            count0+=1
            x+=1
        elif x>0:
            #if number positive increase positive count
            countPositive+=1
            x+=1
        else:
            # leftover is negative
            countNegatvie+=1
            x+=1
            #print result with 6 numbers after coma
    print( "{:.6f}".format(countPositive/len(arr)))
    print( "{:.6f}".format(countNegatvie/len(arr)))
    print( "{:.6f}".format(count0/len(arr)))



plusMinus(arr)
