# https://www.hackerrank.com/challenges/2d-array/problem


arr=[[-9,-9,-9,1,1,1],
    [0,-9,0,4,3,2],
    [-9,-9,-9,1,2,3],
     [0,0,8,6,6,0],
     [0,0,0,-2,0,0],
     [0,0,1,2,4,0]];


def hourglassSum(arr):
    # Write your code here
    #hourglass made out of 6x6 values, the minimum can ge -9 everywhere, or 6*-9=-63
    maxResult=-64
    for i in range(4):
        for j in range(4):
            #declare summs for each row
            topSum = sum(arr[i][j:j+3])
            middleSum = arr[i+1][j+1]
            bottomRowSum = sum(arr[i+2][j:j+3])
            #find the hourglass sum and comare if thiw is greater that the minimum or not
            hourglusSum = topSum+ middleSum+bottomRowSum;
            if hourglusSum>maxResult:
                maxResult = hourglusSum
    return maxResult
        
    
          
    
            
    

hourglassSum(arr)




