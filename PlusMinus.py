arr=[-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    count0=0
    countPositive=0
    countNegatvie=0
    for x in arr:
        if x==0:
            count0+=1
            x+=1
        elif x>0:
            countPositive+=1
            x+=1
        else:
            countNegatvie+=1
            x+=1
    print( "{:.6f}".format(countPositive/len(arr)))
    print( "{:.6f}".format(countNegatvie/len(arr)))
    print( "{:.6f}".format(count0/len(arr)))



plusMinus(arr)
