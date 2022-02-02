
n=6
k=3
ar = [1, 3, 2, 6, 1, 2]


def divisibleSumPairs(n, k, ar):
    
    count=0
    #loop thru the array
    for i in range(0, len(ar)-1):
    #loop thru the array starting from second position
        for j in range(i+1,len(ar)):
    #check condition if sum divides by k 
            if (ar[i]+ar[j])%k==0:
                count+=1
    return count


    
        
print(divisibleSumPairs(n, k, ar))      