

arr=[63,25,73,1,98,73,56,84,86,57,16,83,8,25,81]


def countingSort(arr):
    countArray=[]
    for x in range(0,100):
        if x in arr:
            y=arr.count(x)
            countArray.append(y)
        else:
            countArray.append(0)
    return countArray

            
print(countingSort(arr))
            