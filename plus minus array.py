
arr1 = [1,1,0,-1,-1]

def plusMinus(arr):
    countPositive = 0
    countNegative=0
    # Write your code here
    for x in arr:
        if x>0:
            countPositive+=1
        elif x<0:
            countNegative+=1
    print(str.format('{0:.6f}',countPositive/len(arr)))
    print(str.format('{0:.6f}',countNegative/len(arr)))
    print(str.format('{0:.6f}',(len(arr)-countPositive-countNegative)/len(arr)))

plusMinus(arr1)
        