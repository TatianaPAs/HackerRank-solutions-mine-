import sys


s=[[5, 3, 4],
   [1, 5, 8],
   [6, 4, 2]]


def formingMagicSquare(s):
    s= sum(s, [])
    
 #predefine possible magic squares, found from google  
    magic=[[4,9,2,3,5,7,8,1,6],
         [2,7,6,9,5,1,4,3,8],
         [6,1,8,7,5,3,2,9,4],
         [8,3,4,1,5,9,6,7,2],
         [2,9,4,7,5,3,6,1,8],
         [6,7,2,1,5,9,8,3,4],
         [8,1,6,3,5,7,4,9,2],
         [4,3,8,9,5,1,2,7,6]]
    
    count=sys.maxsize
    #compare each number from s with predefined matrix and find difference
    for x in magic:
        difference=0
        for i, j in zip(s,x):
            difference+=abs(i-j)
  
        count=min(count, difference)
    return count
    
    
    
    
print(formingMagicSquare(s))