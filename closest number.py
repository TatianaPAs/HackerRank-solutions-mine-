arr=[-20,-3916237,-357920,-3620601,7374819,-7330761,30,6246457,-6461594,266854]

def closestNumbers(arr):
    #declare empty array for new pairs
    arrPairs = []
    #sort array
    arr.sort()
    #define minimum difference as highest humber
    minNumber = arr[-1]

    for x in range(len(arr)-1):
        #if difference betwen numbers is smaller than minimumNumber to replace it
        if (abs(arr[x+1]-arr[x])<minNumber):
            minNumber=abs(arr[x+1]-arr[x])
            x+=1
        else:
            continue
        
    #iterate aray to find pairs of numbers with minimum difference

    for x in range(len(arr)-1):
        if(abs(arr[x+1]-arr[x])==minNumber):
            arrPairs.append(arr[x])
            arrPairs.append(arr[x+1])
            x+=1
    print(arrPairs)
                
               
        
    
closestNumbers(arr)