
arr=[5,3,1,2,4]

def findMedian(arr):
    # Write your code here
    arr.sort()
    index = int((len(arr)-1)/2+1)
    return arr[index-1]

print(findMedian(arr))