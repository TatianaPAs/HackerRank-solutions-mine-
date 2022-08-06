
arr1 = [1,3,5,7,9]

def miniMaxSum(arr):
    sumTotal=0
    # Write your code here
    arr.sort()
    for i in arr:
        sumTotal+=i
    print(sumTotal-arr[-1],sumTotal-arr[0])

miniMaxSum(arr1)      
        
    
    