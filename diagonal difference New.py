
arr=[[11,2,4],
     [4,5,6],
     [10,8,-12]]

def diagonalDifference(arr):
    # Write your code here
    fisrt_diagonal = 0
    second_diagonal=0
    k=0
    z=len(arr[0])-1
    for x in arr:
        fisrt_diagonal+=x[k]
        k+=1;
    for y in arr:
        second_diagonal+=y[z]
        z-=1;

    return abs(fisrt_diagonal-second_diagonal)
  
        
print(diagonalDifference(arr))