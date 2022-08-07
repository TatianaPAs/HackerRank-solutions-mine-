matrix = [[112, 42, 83, 119],
           [56, 125, 56, 49],
           [15, 78, 101, 43],
           [62, 98, 114, 108]]
 
def flippingMatrix(matrix):
    # Write your code here
    length = len(matrix)
    total= 0
    for i in range(length//2):
        for j in range(length//2):
            total += max(matrix[i][j], matrix[i][length-j-1], matrix[length-i-1][j], matrix[length-i-1][length-j-1])
    return total
    
    
 
    
    
print(flippingMatrix(matrix))