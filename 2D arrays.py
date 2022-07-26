

arr=[[-9,-9,-9,1,1,1],
    [0,-9,0,4,3,2],
    [-9,-9,-9,1,2,3],
     [0,0,8,6,6,0],
     [0,0,0,-2,0,0],
     [0,0,1,2,4,0]];


def hourglassSum(arr):
    # Write your code here
    maxResult=-64
    for i in range(4):
        for j in range(4):
            topSum = sum(arr[i][j:j+3])
            middleSum = arr[i+1][j+1]
            bottomRowSum = sum(arr[i+2][j:j+3])
            
            hourglusSum = topSum+ middleSum+bottomRowSum;
            if hourglusSum>maxResult:
                maxResult = hourglusSum
    return maxResult
        
    
          
    
            
    

hourglassSum(arr)




