arr=[5,1,2,3,4,5]

k=1
def findNumber(arr, k):
    arr.sort()
    for i in arr:
        if i==k:
            return "YES"
        else:
            return "NO"

#print(findNumber(arr,k))


l=3
r=9
oddNumbersArray=[]
def oddNumbers(l, r):
    for x in range(l,(r+1)):
        if(x%2!=0):
            oddNumbersArray.append(x)
            x+=1;
    return oddNumbersArray
    
        
array =   oddNumbers(1, 6)
for x in array:
    print (x)
    