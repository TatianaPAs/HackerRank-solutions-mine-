import math


def diagonalDifference(arr):
    diagonal1 = sum((arr[x][x]) for x in range(0, len(arr))) 
    diagonal2 = sum((arr[y][n-1-y]) for y in range (0, len(arr)))
    return abs(diagonal1-diagonal2)



print(diagonalDifference(arr))